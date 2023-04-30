#!/usr/bin/env python3

import rospy
import actionlib
import example_action_server.msg
import time
from example_service.srv import Fibonacci, FibonacciResponse

def action_proxy(self):
    # Create an action client proxy
    actclient = actionlib.SimpleActionClient('fibonacci', example_action_server.msg.FibonacciAction)

    # Wait for the action server to be available
    actclient.wait_for_server()

    # Create an action goal
    goal = example_action_server.msg.FibonacciGoal(order=self)

    # Send the action goal
    actclient.send_goal(goal)

    # Wait for the action to complete
    actclient.wait_for_result()
    
    return actclient.get_result()
 
def service_proxy(x):
    fibonacci_service = rospy.ServiceProxy('calc_fibonacci', Fibonacci)
    # Wait for the service to become available
    fibonacci_service.wait_for_service()
    # Create a request object and set its values
    request = fibonacci_service(x)
    return request.sequence
        
if __name__ == '__main__':
    try:
        rospy.init_node('rosservice')
        it = time.time()
        
        serve = service_proxy(3)
        rospy.loginfo(serve)
        serve = service_proxy(15)
        rospy.loginfo(serve)
        
        act = action_proxy(3)
        rospy.loginfo(act)
        act = action_proxy(15)
        rospy.loginfo(act)
        
        ft = time.time()
        t = ft - it
        rospy.loginfo(t)
        
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
