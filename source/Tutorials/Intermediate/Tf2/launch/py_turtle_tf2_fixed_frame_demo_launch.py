from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    launch_dir = Path(get_package_share_directory('learning_tf2_py'))

    return LaunchDescription([
        IncludeLaunchDescription(launch_dir / 'turtle_tf2_demo_launch.py'),
        Node(
            package='learning_tf2_py',
            executable='fixed_frame_tf2_broadcaster',
            name='fixed_broadcaster',
        ),
    ])
