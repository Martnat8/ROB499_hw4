#!/usr/bin/env python3


# Action client for nasa.py
#
# nasa_client.py
#
# Nathan Martin
#
# This is an action client to accompany the nasa.py action server


# Pull in the stuff we need from rclpy.
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient


# Pull in the action definition. 
from hw4_interfaces.action import LaunchRocket


# Creating the client node
class LaunchClient(Node):
	def __init__(self, with_cancel=False):

		# Initialize the superclass
		super().__init__('launch_client')

		# Set up the simple action client.
		self.client = ActionClient(self, LaunchRocket, 'launch_rocket')

	# This function is a wrapper that will allow us to more conveniently invoke the action.
	def send_goal(self, n):

		# Build an action goal, and fill in the data. 
		goal = LaunchRocket.Goal()
		goal.number = n

		# Wait until the server is ready to accept an action request.
		self.client.wait_for_server()

		# Make the action request.  We're going to send the goal message, and set the
		# feedback callback.  We're going to store the handle in an instance variable.
		self.result = self.client.send_goal_async(goal, feedback_callback=self.feedback_cb)

		# Attach a callback to the call, so that we can react when the action is accepted or
		# rejected. The callback is called when the action is accepted or rejected.
		self.result.add_done_callback(self.response)

	# Process feedback as it comes in.
	def feedback_cb(self, feedback_msg):

		# We're not going to do anything other than log the feedback.
		self.get_logger().info(f'Got feedback: {feedback_msg.feedback.progress}')

	def cancel_cb(self, future):

		response = future.result()

		if len(response.goals_canceling) > 0:
			self.get_logger().info('Goal canceled.')
		else:
			self.get_logger().info('Goal failed to cancel.')			

	# This callback fires when the action is accepted or rejected.
	def response(self, future):

		# Get the result of requesting the action.
		self.goal_handle = future.result()

		# If it's not accepted, then we're done.  Log a message and return from the
		# function.
		if not self.goal_handle.accepted:
			self.get_logger().info('Goal rejected')
			return

		# If the action was accepted, then get a handle to it, so that we can retrieve the
		# result.  Then, associate a callback with it, so that we get access to the results
		# when they're available.
		self.result_handle = self.goal_handle.get_result_async()
		self.result_handle.add_done_callback(self.process_result)

	# This callback fires when there are results to be had.  This happens when the action
	# is finished.
	def process_result(self, future):
		# Get the result.  This has a type corresponding to the result part of the
		# action message definition.
		result = future.result().result

		# Log the result to the info channel.
		self.get_logger().info(f'Countdown ended at: {(result.countdown)}')



def without_cancel(args=None):
	# Initialize rclpy.
	rclpy.init(args=args)

	# Set up a node to do the work.
	client = LaunchClient(with_cancel=False)

	# Make the action call.
	client.send_goal(10)

	# Give control over to ROS2.
	rclpy.spin(client)

	# Make sure everything has shut down correctly.
	rclpy.shutdown()
	

def with_cancel(args=None):
	# Initialize rclpy.
	rclpy.init(args=args)

	# Set up a node to do the work, demonstrating action canceling.
	client = LaunchClient(with_cancel=True)

	# Make the action call.
	client.send_goal(10)

	# Give control over to ROS2.
	rclpy.spin(client)

	# Make sure everything has shut down correctly.
	rclpy.shutdown()


# This is the entry point for running the node directly from the command line.
# Runs without cancels if called on the command line
if __name__ == '__main__':
	without_cancel()
