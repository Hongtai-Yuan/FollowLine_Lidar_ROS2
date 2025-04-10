from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    linefollow_node = Node(
        package='njau_line',
        executable='follow_line_a1_X3',
    )

    launch_description = LaunchDescription([linefollow_node]) 
    return launch_description
