from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='c2_serial',
            executable='c2_input',
            name='c2_input'
        ),
        Node(
            package='c2_serial',
            executable='c2_serial',
            name='c2_serial'
        ),
        Node(
            package='c2_serial',
            executable='c2_logger',
            name='c2_logger'
        ),
    ])
