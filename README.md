# ROB 499 Robot Software Frameworks HW3

This package contains two nodes each with their own service that controls their
utility.

data_sender - Sends a test packet of arbitrary information and it's send time.

data_receiver - Subscribes to data_sender and calculates latency of the packet. 
Reports raw and averaged latency.

_____________________________________________________________________

To start run these two commands in separate terminals:

- `ros2 run hw3 data_receiver`
- `ros2 run hw3 data_sender`

In two new terminals use the following commands to start and stop data and logging. 
The filename logging.csv can be anything you want and will either create a file or 
append on to an existing one. The file name can also be a file path

ros2 service call /send_data hw3/srv/SendData "{ send_data: true }"
ros2 service call /send_data hw3/srv/SendData "{ send_data: false }"

ros2 service call /enable_logging hw3/srv/EnableLogging "{ enable_logging: true, file_name: 'logging.csv' }"
ros2 service call /enable_logging hw3/srv/EnableLogging "{ enable_logging: false, file_name: 'logging.csv' }"

_____________________________________________________________________________________
Maintainer - Nathan Martin - martnat8@oregonstate.edu
_____________________________________________________________________________________
License - BSD 3-Clause
_____________________________________________________________________________________
References:
ROS2 Time - https://docs.ros.org/en/iron/p/rclpy/api/time.html
ROS2 Builtin_interfaces - https://github.com/ros2/rcl_interfaces/blob/rolling/builtin_interfaces
Python Append to file - https://www.geeksforgeeks.org/python-append-to-a-file/

I spoke with classmate MJ Santos about enabling python scripts in the CMakeLists. Further 
I "spoke" with ChatGPT to understand formatting and building the hybrid package since 
this was created using cmake and not python as in the tutorial.


