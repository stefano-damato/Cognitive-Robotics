#!/usr/bin/env python3
import os
import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2DArray
import cv2
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
from threading import Lock

rospy.init_node('visualization_node')
image_lock = Lock()
image = None

# This callback recives the bounding box cordinates and draw it
def rcv_detection(msg):
    global image
    rospy.loginfo('detection here')
    image_lock.acquire()
    if image is None: im = None
    else: im = image.copy()
    image_lock.release()
    if im is None: return
    h,w,_ = im.shape
    for d in msg.detections:
        c = d.source_img.header.frame_id 
        #s = d.results[0].score
        b = [d.bbox.center.y,d.bbox.center.x,d.bbox.size_y, d.bbox.size_x]
        b[0]-=b[2]/2
        b[1]-=b[3]/2
        p1 = (int(b[1]), int(b[0]))
        p2 = (int((b[3]+b[1])), int((b[2]+b[0])))
        #print(p1, p2, c, classmap[c], s)
        col = (255,0,0) 
        cv2.rectangle(im, p1, p2, col, int(round(480/300)), 3 )
        p1 = (p1[0]-10, p1[1])
        cv2.putText(im, c, p1, cv2.FONT_HERSHEY_SIMPLEX, 0.8, col, 2)
    cv2.imshow('Image', im)
    cv2.waitKey(10)

# This callback recive the image from the webcam
def rcv_image(msg):
    global image
    rospy.loginfo('image here')
    image_lock.acquire()
    image = ros_numpy.numpify(msg)
    image_lock.release()

# Subscribe to the topic webcam where the webcam_node publish the images
si = rospy.Subscriber("webcam", Image, rcv_image)
# Subscribe to the topic detection where the reidentification node publish the bounding box cordinates
sd = rospy.Subscriber("detection", Detection2DArray, rcv_detection)


try:
    rospy.spin()

except KeyboardInterrupt:
    print("Shutting down")
    