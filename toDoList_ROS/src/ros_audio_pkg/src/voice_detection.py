#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

import time
import speech_recognition as sr
class WaitTimeoutError(Exception): pass




def callback(msg):
    label=msg.data
    print("voice "+ label)
    if label!="NO":
        print("Recording...")
        with m as source:
            try:  
                # listen for 1 second, then check again if the stop function has been called
                print("here")
                audio = r.listen(source, timeout=1, phrase_time_limit=5)
            except WaitTimeoutError:
                pass
            else:
                print("CIAO MONDOOOO")
                data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
                data_to_send = Int16MultiArray()
                data_to_send.data = data
                pub.publish(data_to_send)
                pub2.publish(label)
        

    
pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
pub2 = rospy.Publisher('ID_label', String, queue_size=10)
rospy.init_node('voice_detection_node', anonymous=True)




# Initialize a Recognizer
r = sr.Recognizer()

# Audio source
global m
m = sr.Microphone(device_index=3,
                    sample_rate=16000,
                    chunk_size=1024)

# Calibration within the environment
# we only need to calibrate once, before we start listening
print("Calibrating...")
with m as source:
    r.adjust_for_ambient_noise(source,duration=3)  
print("Calibration finished")

rospy.Subscriber("ID",String,callback)

rospy.spin()
