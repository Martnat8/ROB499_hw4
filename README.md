# ROB 499 Robot Software Frameworks HW4

This package contains one node that publishes sin waves. 
It has parameters 'frequency' and 'clamp'.

Frequency controls the frequency of the sin wave.
Clamp, clamps the sin wave to a maxium amplitude.

This package is driven by the wave.py launch file, which spawns three instances of 
the oscope node producing 1 Hz, 5 Hz, and 10 Hz sine waves. The 10 Hz wave is clamped 
to ±0.7, and each node is remapped to its own topic: 
    (e.g. /oscope_1Hz, /oscope_5Hz, /oscope_10Hz).
    
This package also contains a service to start and stop publishing data.

oscope.py 

_____________________________________________________________________________________

To start, build packages, source and run the launch file

colcon build --packages-select hw4_interfaces hw4
source install/setup.bash
ros2 launch hw4 wave.py

Data is published by default to start or stop publishing use the following command 
format:

ros2 service call /send_data_1hz hw4_interfaces/srv/SendData "{ send_data: false }"


_____________________________________________________________________________________
Maintainer - Nathan Martin - martnat8@oregonstate.edu
_____________________________________________________________________________________
License - BSD 3-Clause
_____________________________________________________________________________________
References:
Code largely iterative of class given example code, particulary rob599_basic params.py.


