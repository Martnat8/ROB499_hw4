# The launch file for nasa.py and nasa_client.
#
# launch.py
#
# Nathan Martin


# We need to import the launch system modules.  There's a generic launch
# system, in launch, and some ROS-specific stuff, in launch_ros.
import launch
import launch_ros.actions


# You need to define this function, which is loaded by the launch system.  The function
# returns a list of nodes that you want to run.
def generate_launch_description():
    return launch.LaunchDescription([

        # Runs the oscope nodes
        launch_ros.actions.Node(
            package='hw4',
            executable='nasa',
            name= 'nasa',           
        ),

        launch_ros.actions.Node(
            package='hw4',
            executable='nasa_client_no_cancel',
            name= 'nasa_client',
            
            # Change this value to change launch goal
            parameters = [{'count_down_goal': 5}],
        ),
        ])
