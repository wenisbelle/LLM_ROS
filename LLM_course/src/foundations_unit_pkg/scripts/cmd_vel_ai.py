#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from rclpy.qos import ReliabilityPolicy, QoSProfile
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from rclpy.executors import MultiThreadedExecutor
# AI Imports
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration


class AiCmdVel(object):

    def __init__(self):
        self.MODEL_PATH = '/LLM_course/src/gen_ai_basics/robot_ai_exercise_1/custom_t5_robot_model'
        self.MAX_LENGTH = 512
        # Load the trained model and tokenizer
        self.model = T5ForConditionalGeneration.from_pretrained(self.MODEL_PATH)
        self.tokenizer = T5Tokenizer.from_pretrained(self.MODEL_PATH)

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        self.model.eval()  # Ensure the model is in evaluation mode

    def generate_robot_command(self, description):
        '''Generate robot command from a given movement description'''

        with torch.no_grad():
            input_text = description
            input_tensor = self.tokenizer(input_text, return_tensors="pt", truncation=True, padding='max_length', max_length=self.MAX_LENGTH).input_ids.to(self.device)
            output_tensor = self.model.generate(input_tensor, max_length=self.MAX_LENGTH)  # Adjust as needed
            output_text = self.tokenizer.decode(output_tensor[0], skip_special_tokens=True)
            command = output_text

            return command

    def prompt_to_cmd_vel(self, description):

        command = self.generate_robot_command(description)
        print("Description="+description+",Generated Command="+command)

        return command



class SimpleSubscriber(Node):

    def __init__(self, cmd_vel_topic_name = "/robot_base_controller/cmd_vel_unstamped", lin_speed = 0.5, angular_speed = 0.5):

        super().__init__('cmd_vel_republisher')

        self._cmd_vel_topic_name = cmd_vel_topic_name
        self._lin_speed = lin_speed
        self._angular_speed = angular_speed

        self.group1 = MutuallyExclusiveCallbackGroup()
        self.group2 = MutuallyExclusiveCallbackGroup()

        self.ai_cmd_vel_obj = AiCmdVel()

        self.subscriber= self.create_subscription(
            String,
            '/ai_command',
            self.listener_callback,
            QoSProfile(depth=1, reliability=ReliabilityPolicy.BEST_EFFORT),
            callback_group=self.group1)

        self.publisher_ = self.create_publisher(Twist, self._cmd_vel_topic_name, 1)
        
        self.init_vars()
        self.timer = self.create_timer(
            self.timer_period, self.timer_callback, callback_group=self.group2)  

    def init_vars(self):
        self.executing_movement_flag = False
        self.movement_list = []
        self.timer_period = 0.1
        self.sequence_time = 0.0
        self.current_seq = None
        self.publisher_.publish(Twist())
        self.get_logger().warning("--> STOP INIT COMMAND SENT")  

    def timer_callback(self):

        if not self.executing_movement_flag:
            self.get_logger().debug("---> Waiting for Human Command...")
        else:
            if self.current_seq:
                self.sequence_time += self.timer_period
                seq_duration = self.current_seq.linear.z
                

                if self.sequence_time >= seq_duration:
                    self.get_logger().info("---> Change Seq")
                    if len(self.movement_list) == 0:
                        self.init_vars()
                    else:
                        self.sequence_time = 0.0
                        self.current_seq = self.movement_list.pop(0)
                        self.publisher_.publish(self.current_seq)
                else:
                    self.get_logger().info("---> Waiting for Seq to finish="+str(self.sequence_time)+"/"+str(seq_duration))
                    self.publisher_.publish(self.current_seq)
            else:
                # Non assigned, we have to assign fisrt sequence
                self.get_logger().info("---> Asign First seq")
                if len(self.movement_list) == 0:
                    self.init_vars()
                else:
                    self.sequence_time = 0.0
                    self.current_seq = self.movement_list.pop(0)
                    self.publisher_.publish(self.current_seq)
            

    def listener_callback(self, msg):        
        self.get_logger().info('I receive: "%s"' % str(msg.data))

        ai_cmd_vel_string = self.ai_cmd_vel_obj.prompt_to_cmd_vel(msg.data)
        self.get_logger().info("Ai COMMAND="+str(ai_cmd_vel_string))
        self.unstringify_cmd_msg(ai_cmd_vel_string)
        self.get_logger().info("Generated Sequence="+str(self.movement_list))
        self.executing_movement_flag = True
        self.get_logger().info("Execution activated="+str(self.executing_movement_flag))

        

    
    def unstringify_cmd_msg(self,cmd_vel_msg):
        sequence_cmd_list = cmd_vel_msg.split(", ")

        for seq in sequence_cmd_list:
            cmd_vel_list = seq.split("_")
            
            left_wheel = float(cmd_vel_list[0])
            right_wheel = float(cmd_vel_list[1])
            duration = float(cmd_vel_list[2])
            cmd_vel_msg = self.wheel_to_cmdvel(left_wheel, right_wheel, duration)

            self.movement_list.append(cmd_vel_msg)


    def wheel_to_cmdvel(self, left, right, duration):
        cmdvel = Twist()
        # We place duration isndie linear Z because we wont have robots flying for the moment
        cmdvel.linear.z = duration

        linear_speed = self._lin_speed
        angular_speed = self._angular_speed
        
        self.get_logger().warning("IN VALUES=["+str(left)+"|"+str(right)+"|"+str(duration)+"]")


        if left > 0 and right > 0:
            if left > right:
                # Slighly Right movement
                cmdvel.linear.x = linear_speed
                cmdvel.angular.z = -angular_speed
            elif left < right:
                # Slighly Left movement
                cmdvel.linear.x = linear_speed
                cmdvel.angular.z = angular_speed
            else:
                # Forwards Right movement
                cmdvel.linear.x = linear_speed
        elif left < 0 and right < 0:
            # Backwards
            cmdvel.linear.x = -linear_speed
        elif left > 0 and right < 0:
            # Right
            cmdvel.angular.z = -angular_speed
        elif left < 0 and right > 0:
            # Left
            cmdvel.angular.z = angular_speed
        elif left == 0 and right == 0:
            # Stop
            pass
        else:
            self.get_logger().error("WRONG VALUES="+str(left)+","+str(right))


        self.get_logger().warning("OUT VALUES="+str(cmdvel))

        return cmdvel

      
            
def main(args=None):
    rclpy.init(args=args)
    simple_subscriber = SimpleSubscriber()
    num_threads = 2
    executor = MultiThreadedExecutor(num_threads=num_threads)
    executor.add_node(simple_subscriber)
    try:
        executor.spin()
    finally:
        executor.shutdown()
        simple_subscriber.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()