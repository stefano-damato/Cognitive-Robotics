#!/usr/bin/env python3
import rospy, ros_numpy
import cv2
from sensor_msgs.msg import Image
import json
import os
# Read frame 

def talker():
    pub = rospy.Publisher('webcam',Image,queue_size=100)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(1)
    print(os.listdir())
    print("Starting videocapture")
    with open('config.json', 'r') as f:
        config = json.load(f)
    index = config["WEBCAM_IDX"]
    #index = 6
    cap = cv2.VideoCapture(index)
    print("Started videocapture")
    while not rospy.is_shutdown():             
        # Take each frame
        
        _, frame = cap.read() # Read frame
        msg = ros_numpy.msgify(Image, frame, encoding = "bgr8")
        #rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()



if __name__=='__main__':
    try:
        
        talker()
    except rospy.ROSInterruptException:
        pass