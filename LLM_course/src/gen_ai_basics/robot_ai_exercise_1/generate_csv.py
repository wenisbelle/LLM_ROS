import csv
import random

def generate_movement_commands(num_commands=1000, max_num_of_sentences=5):
    actions = ["go", "turn", "move", "stop"]
    directions = ["straight", "backwards", "slightly left", "slightly right", "sharp left", "sharp right", "pivot left", "pivot right"]    
    connectors = [",", "and", "then", "."]
    durations = ["for {} seconds", "for a short while", "for a bit", "for a long time", ""]

    forward_speed = 10
    reduced_speed = 5
    backward_speed = -10
    stop_speed = 0

    human_commands = []
    robot_commands = []

    for _ in range(num_commands):
        human_command = ""
        robot_command = ""
        sep = "_"
        for sentence_index in range(max_num_of_sentences):
            primary_action = random.choice(actions)
            if primary_action == "stop":
                direction = ""
            else:
                direction = random.choice(directions)
                if "left" in direction or "right" in direction:
                    primary_action = "turn"

            duration = random.choice(durations).format(random.randint(1, 10))

            human_command += " "+primary_action+" "+direction+" "+duration

            # For simplicity, we will set default values for robot command. 
            # You may adjust these values based on the complexity you desire.
            left_wheel_speed = forward_speed
            right_wheel_speed = forward_speed

            # We set time based on words
            command_duration = random.uniform(1, 10)  # In seconds
            if "short" in duration:
                command_duration = random.uniform(0, 2)
            elif "bit" in duration:
                command_duration = random.uniform(0.0, 5.0)
            elif "long" in duration:
                command_duration = random.uniform(5, 10)
            elif "seconds" in duration:
                command_duration = float(duration.split(" ")[-2])
            else:
                pass

            command_duration = round(command_duration,1)
            #######

            if "slightly left" in direction:
                left_wheel_speed = reduced_speed
            elif "sharp left" in direction or "pivot left" in direction:
                left_wheel_speed = backward_speed
            elif "slightly right" in direction:
                right_wheel_speed = reduced_speed
            elif "sharp right" in direction or "pivot right" in direction:
                right_wheel_speed = backward_speed
            elif "backwards" in direction:
                left_wheel_speed = backward_speed
                right_wheel_speed = backward_speed
            elif "stop" in primary_action:
                left_wheel_speed = stop_speed
                right_wheel_speed = stop_speed




            # We see if we continue adding commands or we stop
            connector_chosen = random.choice(connectors)



            robot_sep = ", "
            space = " "
            finish_sentence = False
            if connector_chosen == "." or sentence_index >= (max_num_of_sentences-1):
                # We stop sentence gen
                robot_sep = ""
                connector_chosen = "."
                space = ""             
                finish_sentence = True
            else:
                pass

            human_command += space+connector_chosen
            # We clean any double spaces that got in the mix
            human_command = " ".join(human_command.split())

            robot_command += str(left_wheel_speed)+sep+str(right_wheel_speed)+sep+str(command_duration)+robot_sep



            if finish_sentence:
                break

        # We put capital letters randomly , because people sometimes do it sometimes don't
        if random.random() < 0.5:
            human_command = human_command.capitalize()
        else:
            pass

        human_commands.append(human_command)
        robot_commands.append(robot_command)

    return human_commands, robot_commands

num_commands = 100000
human_cmds, robot_cmds = generate_movement_commands(num_commands)

# Save commands to a CSV file
with open('train.csv', 'w', newline='') as csvfile:
    with open('test.csv', 'w', newline='') as csvfile_test:
        csv_writer = csv.writer(csvfile)
        csvfile_test = csv.writer(csvfile_test)

        # Write header
        csv_writer.writerow(["Human Command", "Robot Command"])
        csvfile_test.writerow(["Human Command", "Robot Command"])
        i = 0

        for h_cmd, r_cmd in zip(human_cmds, robot_cmds):
            test_num = num_commands*0.9
            if i< test_num:
                csv_writer.writerow([h_cmd, r_cmd])
            else:
                csvfile_test.writerow([h_cmd, r_cmd])
            i+= 1

print(f"Generated {len(human_cmds)} commands and saved to 'train.csv' and 'test.csv'.")