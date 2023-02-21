#!/usr/bin/env python3
import rospy
from turtlesim_helper.msg import UnitsLabelled

def callback(data):
	pub = rospy.Publisher('conversion', UnitsLabelled, queue_size=10)
	rate = rospy.Rate(10)
	unittype = rospy.get_param('/unitvar')
	distance = data.value
	traveldis = UnitsLabelled()
	if unittype == 'smoots':
		traveldis.value = distance / 1.702
		traveldis.units = 'smoots'
		pub.publish(traveldis)
	elif unittype == 'feet':
		traveldis.value = distance * 3.281
		traveldis.units = 'feet'
		pub.publish(traveldis)
	else:
		traveldis.value = distance
		traveldis.units = 'meters'
		pub.publish(traveldis)
	
	rate.sleep()
	
def conversion():
	rospy.init_node('conversion',anonymous = True)
	rospy.Subscriber('distance', UnitsLabelled, callback)
	rospy.spin()
	
if __name__ == '__main__':
	conversion()
