import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the path to the launch files
    
    slam_launch_file = os.path.join(
        get_package_share_directory('slam'), 'launch', 'online_async_launch.py')
    
    nav2_launch_file = os.path.join(
        get_package_share_directory('slam'), 'launch', 'navigation2_launch.py')

    return LaunchDescription([
        # Launch first_launch.py
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_launch_file),
            launch_arguments={}.items(),
        ),

        # Delay before launching the robot_state_publisher
        TimerAction(
            period=2.0,  # Adjust the delay time as needed
            actions=[
                # Launch second_launch.py
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(nav2_launch_file),
                    launch_arguments={}.items(),
                ),
            ],
        ),
        ])
