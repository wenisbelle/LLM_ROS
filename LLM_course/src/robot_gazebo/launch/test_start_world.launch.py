#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_prefix


def generate_launch_description():

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_ai_bot_gazebo = get_package_share_directory('robot_gazebo')

    # Where the dummy barista description models of the robots are
    description_package_name = "robot_description"
    install_dir = get_package_prefix(description_package_name)

    

    gazebo_models_path = os.path.join(pkg_ai_bot_gazebo, 'models')

    # Plugins
    gazebo_plugins_name = "gazebo_plugins"
    gazebo_plugins_name_path_install_dir = get_package_prefix(
        gazebo_plugins_name)

    gazebo_plugins_name = "gazebo_plugins"
    gazebo_plugins_name_path_install_dir = get_package_prefix(
        gazebo_plugins_name)

    # The slot car plugin is inside here
    plugin_pkg = "rmf_robot_sim_gz_classic_plugins"
    try:
        plugin_dir = get_package_prefix(plugin_pkg)
    except:
        plugin_dir = ""
        print("No package found="+str(plugin_pkg))

    plugin_building_pkg = "rmf_building_sim_gz_classic_plugins"
    try:
        plugin_building_dir = get_package_prefix(plugin_building_pkg)
    except:
        plugin_building_dir = ""
        print("No package found="+str(plugin_building_dir))
    


    if 'GAZEBO_MODEL_PATH' in os.environ:
        os.environ['GAZEBO_MODEL_PATH'] = os.environ['GAZEBO_MODEL_PATH'] + ':' + install_dir + \
            '/share' + ':' + gazebo_models_path
    else:
        os.environ['GAZEBO_MODEL_PATH'] = install_dir + \
            "/share" + ':' + gazebo_models_path

    if 'GAZEBO_PLUGIN_PATH' in os.environ:
        os.environ['GAZEBO_PLUGIN_PATH'] = os.environ['GAZEBO_PLUGIN_PATH'] + ':' + install_dir + '/lib' + ':' + \
            gazebo_plugins_name_path_install_dir + '/lib' + ':' + \
            plugin_dir + '/lib' + '/rmf_robot_sim_gz_classic_plugins' + ':' + \
            plugin_building_dir + '/lib' + '/rmf_building_sim_gz_classic_plugins'
    else:
        os.environ['GAZEBO_PLUGIN_PATH'] = install_dir + '/lib' + ':' + gazebo_plugins_name_path_install_dir + \
            '/lib' + ':' + plugin_dir + '/lib' + '/rmf_robot_sim_gz_classic_plugins' + \
            ':' + plugin_building_dir + '/lib' + '/rmf_building_sim_gz_classic_plugins'

    print("GAZEBO MODELS PATH=="+str(os.environ["GAZEBO_MODEL_PATH"]))
    print("GAZEBO PLUGINS PATH=="+str(os.environ["GAZEBO_PLUGIN_PATH"]))

    # Gazebo launch
    gzserver = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py'),
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=[os.path.join(
                pkg_ai_bot_gazebo, 'worlds', 'room.world'), ''],
            description='SDF world file'),
        DeclareLaunchArgument(
            'verbose', default_value='true',
            description='Set "true" to increase messages written to the terminal.'
        ),
        gzserver
    ])
