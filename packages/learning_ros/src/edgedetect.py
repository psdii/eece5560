#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class edgedetect:
    global ros_edges
    def __init__(self):
        rospy.Subscriber("/image_cropped", Image, self.edges_cb)
        rospy.Subscriber("/image_yellow", Image, self.yellowedges_cb)
        rospy.Subscriber("/image_white", Image, self.whiteedges_cb)
        
        self.pub1 = rospy.Publisher("/image_edges", Image, queue_size=10)
        self.pub2 = rospy.Publisher("/image_lines_yellow", Image, queue_size=10)
        self.pub3 = rospy.Publisher("/image_lines_white", Image, queue_size=10)
        
        # Instantiate the converter class once by using a class member
        self.bridge = CvBridge()
        
    def edges_cb(self, msg):
        # convert to a ROS image using the bridge
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv_edges = cv2.Canny(cv_img, 100, 200)
        ros_edges = self.bridge.cv2_to_imgmsg(cv_edges, "mono8")
        
        self.pub1.publish(ros_edges)
    def yellowedges_cb(self, msg):
        # convert to a ROS image using the bridge
        cv_img = self.bridge.imgmsg_to_cv2(msg, "mono8")
        cv_edges = cv2.Canny(cv_img, 100, 200)
        ros_edges = self.bridge.cv2_to_imgmsg(cv_edges, "mono8")

        self.pub2.publish(ros_edges)
    def whiteedges_cb(self, msg):
        # convert to a ROS image using the bridge
        cv_img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        cv_edges = cv2.Canny(cv_img, 100, 200)

        ros_edges = self.bridge.cv2_to_imgmsg(cv_edges, "mono8")

        self.pub3.publish(ros_edges)
    '''
    def houghtransform():    
        cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn]]])
    '''

if __name__=="__main__":
    # initialize our node and create a publisher as normal
    rospy.init_node("edgedetect", anonymous=True)
    img_crop = edgedetect()
    rospy.spin()
