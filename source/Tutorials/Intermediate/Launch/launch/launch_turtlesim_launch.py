from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription


def generate_launch_description():
    launch_dir = Path(get_package_share_directory('launch_tutorial')) / 'launch'
    return LaunchDescription([
        IncludeLaunchDescription(launch_dir / 'turtlesim_world_1_launch.py'),
        IncludeLaunchDescription(launch_dir / 'turtlesim_world_2_launch.py'),
        IncludeLaunchDescription(
            launch_dir / 'broadcaster_listener_launch.py',
            launch_arguments={'target_frame': 'carrot1'}.items(),
        ),
        IncludeLaunchDescription(launch_dir / 'mimic_launch.py'),
        IncludeLaunchDescription(launch_dir / 'fixed_broadcaster_launch.py'),
        IncludeLaunchDescription(launch_dir / 'turtlesim_rviz_launch.py'),
    ])
