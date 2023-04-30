#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageCropper:
    def __init__(self):
        rospy.Subscriber("/image", Image, self.filter)
        self.pub = rospy.Publisher("/image_yellow", Image, queue_size=10)
        self.pub2 = rospy.Publisher("/image_white", Image, queue_size=10)
        self.pub3 = rospy.Publisher("/image_cropped", Image, queue_size=10)
        
        # Instantiate the converter class once by using a class member
        self.bridge = CvBridge()
    def filter(self, msg):
        # convert to a ROS image using the bridge
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        # flip along the horizontal axis using an OpenCV function
        cv_cropped = cv_img[240:480, 0:640]
        hsv_cropped = cv2.cvtColor(cv_cropped, cv2.COLOR_BGR2HSV)
        ros_cropped = self.bridge.cv2_to_imgmsg(cv_cropped, "bgr8")
        x = 80
        hsv_filterwhite = cv2.inRange(hsv_cropped, (0,0,255-x), (255,x,255))
        ros_white = self.bridge.cv2_to_imgmsg(hsv_filterwhite, "mono8")
        hsv_filteryellow = cv2.inRange(hsv_cropped, (0,110,110), (40,255,255))
        ros_yellow = self.bridge.cv2_to_imgmsg(hsv_filteryellow, "mono8")
        
        # publish flipped image
        self.pub3.publish(ros_cropped)
        self.pub.publish(ros_yellow)
        self.pub2.publish(ros_white)
	#self.pub = rospy.Publisher("/image_cropped", Image, queue_size=10)

if __name__ == "__main__":
    # initialize our node and create a publisher as normal
    rospy.init_node("image_cropper", anonymous=True)
    img_crop = ImageCropper()
    rospy.spin()
