from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

package_name = 'ackerman_robot'

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time')

    urdf_path = '/home/danilinux/Escritorio/Robot_ackerman/src/ackerman_robot/urdf/Robot_ackerman.urdf'

    pub = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output='screen',
        parameters=[{
            'robot_description': Command(['xacro ', urdf_path])
        }]
    )

    gazebo = ExecuteProcess(
        cmd=[
            'gazebo',
            '--verbose',
            '-s',
            'libgazebo_ros_init.so',
            '-s',
            'libgazebo_ros_factory.so'
            ],
            output= 'screen'
    )

    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=['-entity', 'robot', '-topic','robot_description'],
        output='screen'
    )

    rviz = ExecuteProcess(
        cmd=['rviz2'],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        gazebo,
        pub,
        spawn_entity
    ])