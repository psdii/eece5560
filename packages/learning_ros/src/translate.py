#!/usr/bin/env python3
import rospy
import numpy
from math import sqrt, sin, cos, tan
import sys
from duckietown_msgs.msg import Vector2D
from turtlesim_helper.msg import UnitsLabelled

def callback(data):
    pos = Vector2D()
    posx = data.x
    posy = data.y
    
    pub1 = rospy.Publisher('robot_coord',Vector2D,queue_size=10)
    pub2 = rospy.Publisher('world_coord',Vector2D,queue_size=10)
    
    transformWorld = numpy.matrix([[sqrt(2)/2,sqrt(2)/2,5+sqrt(2)/2],[-sqrt(2)/2,sqrt(2)/2,3-sqrt(2)/2],[0,0,1]])
    transformRobot = numpy.matrix([[-1,0,-1],[0,-1,0],[0,0,1]])
    v = numpy.matrix([[posx],[posy],[1]])
    new_vw = transformWorld*v
    new_vr = transformRobot*v
    
    pos.x = new_vw[0,0]
    pos.y = new_vw[1,0]
    pub2.publish(pos)
    
    pos.x = new_vr[0,0]
    pos.y = new_vr[1,0]
    pub1.publish(pos)
    
    
def trans():
    rospy.init_node('trans',anonymous = True)
    while not rospy.is_shutdown():
        rospy.Subscriber('/sensor_coord',Vector2D,callback)
        

if __name__ == '__main__':
    try:
        trans()
    except rospy.ROSInterruptException:
        pass
