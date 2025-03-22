from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    rviz_config = Path(get_package_share_directory('turtle_tf2_py')) / 'rviz' / 'turtle_rviz.rviz'

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config]
        )
    ])
