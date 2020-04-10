#!/usr/bin/env python
# Author: Peter Stulpner, pstulpner@student.unimelb.edu.au
# Script creates a node which send a random integer between 1 and 1000 to the first_num topic

import rospy
from std_msgs.msg import String
from random import seed
from random import randint

def rand_int_generator(i, j):
	'''Function returns a random integer from 1 to 1000 '''
	return  randint(i, j)

def main():

	# Initialise the publisher
	pub = rospy.Publisher("first_num", String, queue_size=19)

	# Initialise the node
	rospy.init_node("push_node1", anonymous=True)

	rate = rospy.Rate(1) #1Hz

	while not rospy.is_shutdown():
		# Generate number:
		num = rand_int_generator(1, 1000)

		# Log the number:
		rospy.loginfo(str(num))

		# Publish the integer to the topic:
		pub.publish(str(num))

		rate.sleep()

if __name__ == "__main__":
	try:
		main()

	except rospy.ROSInterruptException:
		pass
