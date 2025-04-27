# An example Python launch file for ROS.
#
# doubler_launch.py
#
# Bill Smart


# We need to import the launch system modules.  There's a generic launch
# system, in launch, and some ROS-specific stuff, in launch_ros.
import launch
import launch_ros.actions


# You need to define this function, which is loaded by the launch system.  The function
# returns a list of nodes that you want to run.
def generate_launch_description():
    return launch.LaunchDescription([
        # Runs the oscope node with new names and defining parameters
        launch_ros.actions.Node(
            package='hw4',
            executable='oscope',
            name= 'oscope_1Hz',
            parameters = {'frequency': 1.0},
        ),

        launch_ros.actions.Node(
            package='hw4',
            executable='oscope',
            name= 'oscope_5Hz',
            parameters = {'frequency': 1.0},
        ),
        
        launch_ros.actions.Node(
            package='hw4',
            executable='oscope',
            name= 'oscope_10Hz',
            parameters = {'frequency': 1.0,
                        'clamp': 0.7},
        ),
        launch_ros.actions.Node(
            package='plotjuggler',
            executable='plotjuggler',
            name='plotjuggler'
        ),
        ])
