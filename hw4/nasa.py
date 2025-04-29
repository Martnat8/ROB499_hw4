#!/usr/bin/env python3

# Nasa action server for ROB499 HW4
#
# nasa.py
#
# Nathan Martin


# Pull in the stuff we need from rclpy.
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse

# These are needed if we're going to enable action cancelation.
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

# Pull in the action definition. 
from hw4_interfaces.action import LaunchRocket

# We're going to use sleep to slow down the action server.  This will let us see the
# feedback coming into the client.
from time import sleep


# The idiom in ROS2 is to use a function to do all of the setup and work.  This
# function is referenced in the setup.py file as the entry point of the node when
# we're running the node with ros2 run.  The function should have one argument, for
# passing command line arguments, and it should default to None.
class LaunchActionServer(Node):
	def __init__(self):
		# Initialize the superclass
		super().__init__('launch_rocket')

		# Set up a simple action server with action cancelling.
		self.server = ActionServer(self, LaunchRocket, 'launch_rocket', self.callback, 
			callback_group=ReentrantCallbackGroup(), cancel_callback=self.cancel_callback)

	# This is the callback that services the action request.
	def callback(self, goal):

		# This holds what number we're going to countdown from
		countdown = goal.request.number

		# Grab the logger and send a message to it.
		self.get_logger().info(f'Received countdown goal: {countdown}')

		# Initialize result message
		result = LaunchRocket.Result()
		result.countdown = countdown

		# Countdown to zero from goal
		for i in range(countdown):

			# Check to see if we have a cancellation request. 
			if goal.is_cancel_requested:
				goal.canceled()
				self.get_logger().info('Launch is canceled.')
				return LaunchRocket.Result()
			
			# Decrement countdown and publish feedback
			result.countdown -= 1

			goal.publish_feedback(LaunchRocket.Feedback(progress=result.countdown))

			self.get_logger().info(f'Countdown: {result.countdown}')

			# 1 second between countdowns
			sleep(1)

		# Let the action server know that we've succeeded in the action.  It it doesn't
		# succeed, you can set other values here.
		goal.succeed()
		self.get_logger().info(f'Launch Successful!')

		# Return the result to the action server.
		return result

	# This callback fires when a cancellation request comes in.
	def cancel_callback(self, goal_handle):
		self.get_logger().info('Canceling goal')
		return CancelResponse.ACCEPT


# This is the entry point.
def main(args=None):

	# Initialize rclpy.
	rclpy.init(args=args)

	# Set up a node to do the work.
	server = LaunchActionServer()

	# Give control over to ROS2.  To make the goal cancelation work, we need a
	# multithreaded executor here.  If we don't need goal cancelation, we can
	# use the default executor.
	rclpy.spin(server, MultiThreadedExecutor())

	# Make sure we shut down politely.
	rclpy.shutdown()


# This is the entry point for running the node directly from the command line.
if __name__ == '__main__':
	main()
