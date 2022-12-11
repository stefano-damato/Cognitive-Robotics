#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

import time
import speech_recognition as sr

pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
pub2 = rospy.Publisher('mic_data_label', Int16MultiArray, queue_size=10)
rospy.init_node('voice_detection_node', anonymous=True)

# this is called from the background thread
def callback(recognizer, audio):
    data = rospy.wait_for_message("ID",String)
    label = data.data
    print(label)
    if label!="NO":
        print("Recording...")
        data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
        data_to_send = Int16MultiArray()
        data_to_send.data = data
        if label=="name_request":
            pub2.publish(data_to_send)
        else:
            pub.publish(data_to_send)

# Initialize a Recognizer
r = sr.Recognizer()

# Audio source
m = sr.Microphone(device_index=None,
                    sample_rate=16000,
                    chunk_size=1024)

# Calibration within the environment
# we only need to calibrate once, before we start listening
print("Calibrating...")
with m as source:
    r.adjust_for_ambient_noise(source,duration=3)  
print("Calibration finished")

# start listening in the background
# `stop_listening` is now a function that, when called, stops background listening

stop_listening = r.listen_in_background(m, callback)

rospy.spin()