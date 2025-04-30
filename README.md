# ROB 499 Robot Software Frameworks HW4

This package contains three nodes for a two part assignment.

oscope.py

nasa.py
nasa_client.py
_____________________________________________________________________________________
_____________________________________________________________________________________
# oscope.py 
_____________________________________________________________________________________
_____________________________________________________________________________________

The first part consists of a single node and a launch file that publishes sin waves of
various frequencies and can clamp the amplitute to a certain value.

oscope.py has parameters 'frequency' and 'clamp' and a service to start and stop publishing

Frequency: controls the frequency of the sin wave.
Clamp: clamps the sin wave to a maxium amplitude.

This package is driven by the wave.py launch file, which spawns three instances of 
the oscope node producing 1 Hz, 5 Hz, and 10 Hz sine waves. The 10 Hz wave is clamped 
to ±0.7, and each node is remapped to its own topic: 
    (e.g. /oscope_1Hz, /oscope_5Hz, /oscope_10Hz).
____________________________________________________________________________________

To start, build packages, source and run the launch file

colcon build --packages-select hw4_interfaces hw4
source install/setup.bash
ros2 launch hw4 wave.py

Data is published by default to start. If you want to start or stop publishing use 
the following command format, just change 1hz to 5hz or 10hz:

ros2 service call /send_data_1hz hw4_interfaces/srv/SendData "{ send_data: false }"
_____________________________________________________________________________________
_____________________________________________________________________________________
# nasa.py
_____________________________________________________________________________________
_____________________________________________________________________________________

The second part has two nodes nasa.py, nasa_client.py and a launch file. These nodes 
run an action client and server that countdown from a number as determined my a 
parameter in the launch.py file in the launch folder. The countdown can be canceled
as described below.
_____________________________________________________________________________________
To start, build packages, source and run the launch file

colcon build --packages-select hw4_interfaces hw4
source install/setup.bash
ros2 launch hw4 launch.py

If you are interested in canceling the launch run the following command in a new 
sourced terminal

ros2 service call /cancel hw4_interfaces/srv/CancelLaunch "{ cancel: true }"
_____________________________________________________________________________________
Maintainer - Nathan Martin - martnat8@oregonstate.edu
_____________________________________________________________________________________
License - BSD 3-Clause
_____________________________________________________________________________________
References:
Code largely iterative of class given example code, action_client.py and 
action_server.py.


