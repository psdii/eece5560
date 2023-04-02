#!/usr/bin/env python3
import rospy
from odometry_hw.msg import DistWheel, Pose2D
from math import pi, cos, sin

class odometry:
	def __init__(self):
		rospy.Subscriber("dist_wheel", DistWheel, self.ticks_cb)
		self.pub = rospy.Publisher("pose", Pose2D, queue_size=10)
		self.theta = 0
		self.x = 0
		self.y = 0
	def ticks_cb(self, msg):
		s_l = msg.dist_wheel_left
		s_r = msg.dist_wheel_right
		
		delta_s = (s_l + s_r)/2
		delta_theta = (s_r - s_l)/(0.1)
		delta_x = delta_s * cos(self.theta + delta_theta/2)
		delta_y = delta_s * sin(self.theta + delta_theta/2)
		self.x += delta_x
		self.y += delta_y
		self.theta += delta_theta

		if self.theta > pi:
		    self.theta -= 2*pi
		if self.theta < - pi:
		    self.theta += 2*pi
		
		pose = Pose2D()
		
		pose.x = self.x
		pose.y = self.y
		pose.theta = self.theta
		self.pub.publish(pose)
       
if __name__ == '__main__':
	rospy.init_node("odometry", anonymous=True)
	odo = odometry()
	rospy.spin()
