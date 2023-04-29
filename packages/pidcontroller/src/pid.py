#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

class pidController:
	def callback(self, data) :
		pub = rospy.Publisher('/control_input', Float32, queue_size=1)
		errorVal = data.data
		kp = 0.27
		ki = 0.11
		kd = 0.56
		self.t0 = rospy.get_time()
		dt = self.t0 - self.t1
		self.error_product = kp*errorVal
		self.error_intergration = ki*(self.error_intergration +(self.error_intergration*dt))
		self.error_derivative = kd*((errorVal - self.last_errorVal)/dt)
		op_value = (self.error_product + self.error_intergration + self.error_derivative)
		pub.publish(op_value)

		self.t1 = self.t0
		self.last_errorVal = errorVal


	def __init__(self):
		rospy.init_node('pid_node', anonymous=True)
		rospy.Subscriber('error', Float32, self.callback)
		self.error_intergration = 0
		self.error_derivative = 0
		self.error_product = 0

		self.t1 = 0
		self.t0 = 0
		self.last_errorVal = 0

if __name__ == '__main__':
	pid = pidController()
	rospy.spin()
