#!/usr/bin/env python3


# Publishes values of a sin wave in Float32 at a frequency of 100 Hz.
#
# oscope.py
#
# Nathan Martin



# Basic Ros2 setup
import rclpy
from rclpy.node import Node

# Publishing in Float32
from std_msgs.msg import Float32

# Importing math and sign
import math
from numpy import sign

# Importing services
from hw4_interfaces import SendData

class OscopePublisher(Node):
	def __init__(self, frequency, clamp):

		# Initialize the parent class of name oscope
		super().__init__('oscope')

		# Create a publisher, and assign it to a member variable. 
		self.pub = self.create_publisher(Float32, 'oscope', 10)

		# Create a timer at a rate of 100 Hz
		self.timer = self.create_timer(0.01, self.callback)

		# Create a service, with a type, name, and callback.
		self.service = self.create_service(SendData, 'send_data', self.service_callback)

		# Bool to control publishing, off by default
		self.OscopePubBool = False

		# Set up a counter that we can increment.
		self.counter = 0
		
        # Set up a variable to hold sin wave values
		self.sinwave = 0.0

		# Set up a variable for frequency
		self.frequency = frequency

		# Set up a variable to hold clamp range
		self.clamp_range = clamp

	# This callback will be called every time the timer fires.
	def callback(self):
		
		# Only publish if turned on
		if self.OscopePubBool:

			# Make an Float32 message, and fill in the information.
			msg = Float32()
			
			# Calculate new sinwave value
			self.sinwave = math.sin(2 * math.pi * self.frequency * self.counter)

			if abs(self.sinwave) > self.clamp:
				self.sinwave = self.clamp * sign(self.signwave)
			
			# Increment Counter at the same rate as the timer
			self.counter += 0.01

			# Assign data for message
			msg.data = self.sinwave

			# Publish the message
			self.pub.publish(msg)

			# Log that we published something. 
			self.get_logger().info('Published {0}'.format(self.sinwave))

	# This callback will be called every time that the service is called.  
	def service_callback(self, request, response):

		# Turnin on or off data_sender based on service call
		self.OscopePubBool = request.send_data

		# Fill in the data in the response type.
		response.sending = request.send_data

		# Log a message.
		self.get_logger().info(f'Send data bool set to  {response.sending}')

		# The idiom is to return the response at the end of the callback.
		return response


# Basic ROS2 Setup function used for 1 Hz frequecy sin 
def main(args=None):
	
	# Initialize rclpy.  We should do this every time.
	rclpy.init(args=args)

	# Make a node class.
	publisher = OscopePublisher(frequency=1)

    # Handover to ROS2
	rclpy.spin(publisher)

	# Make sure we shutdown everything cleanly.  
	rclpy.shutdown()



# If we run the node as a script, then we're going to start here.
if __name__ == '__main__':
	
	main()