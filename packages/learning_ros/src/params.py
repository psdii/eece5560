#!/usr/bin/env python3
import rospy
from turtlesim_helper.msg import UnitsLabelled

def callback(data):
	rate = rospy.Rate(0.2)
	traveldis = UnitsLabelled()
	rate.sleep()
	rospy.set_param('unitvar', 'meters')
	rate.sleep()
	rospy.set_param('unitvar', 'feet')
	rate.sleep()
	rospy.set_param('unitvar', 'smoots')
		
def params():	
	rospy.init_node('params',anonymous = True)
	rospy.Subscriber('distance', UnitsLabelled, callback)
	rospy.spin()
	
if __name__ == '__main__':
	params()
