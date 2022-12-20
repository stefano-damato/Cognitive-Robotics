#!/usr/bin/python3
import rospy
import os
from std_msgs.msg import Int16MultiArray, String, Bool
import numpy as np
import time
import speech_recognition as sr
from speech_recognition import AudioData
class WaitTimeoutError(Exception): pass
import json

# This function perform the speech recognition on ``audio_data`` (an ``AudioData`` instance), 
# using the Google Speech Recognition API.
def asr(audio,id):
    global current_user
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    try:
        spoken_text= r.recognize_google(audio_data, language='en-GB')
        print("Google Speech Recognition pensa che "+id+" abbia detto: " + spoken_text)
        if id!="unknown":
            if id != current_user:
                current_user = id
                print("Hi, I am "+ current_user)
                pub.publish("Hi, I am "+ current_user)
            else: 
                print("text_to_bot"+spoken_text)
                pub.publish(spoken_text)
        else:
            print("text_for_reidentification "+ spoken_text)
            pub2.publish(spoken_text)
        pub_microphone.publish(True)
        return True
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
        return False
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return False

## This callback recives the label associeted to the user from the reidentification_node
def callback(msg):
    label=msg.data
    print("Label from callback: "+ label)
    print("Current user: "+ current_user)
    while True:
        print("Recording...")
        with m as source:
            try:  
                # listen for TIMEOUT second, then check again if the stop function has been called
                audio = r.listen(source, timeout=TIMEOUT,phrase_time_limit=PRHASE_TIME_LIMIT)
            except Exception:
                print("TimeOUT expired")
                continue
            else:
                data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
                data_to_send = Int16MultiArray()
                data_to_send.data = data
                if asr(data_to_send,label):
                    print("Successful speech recognition")
                    break

rospy.init_node('voice_detection_node', anonymous=True) 

pub_microphone = rospy.Publisher('microphone_ready', Bool, queue_size=10)   
pub = rospy.Publisher('text_to_bot', String, queue_size=10)
pub2 = rospy.Publisher('text_for_reidentification', String, queue_size=10)

current_user=" "

with open('config.json', 'r') as f:
  config = json.load(f)
TIMEOUT = config["TIMEOUT"]
PRHASE_TIME_LIMIT = config["PRHASE_TIME_LIMIT"]
index = config["MICROPHONE_IDX"]
pepper = config["PEPPER"]

# Initialize a Recognizer
r = sr.Recognizer()

# Audio source
global m
m = sr.Microphone(device_index=index,
                    sample_rate=16000,
                    chunk_size=1024)

# Calibration within the environment
# we only need to calibrate once, before we start listening
print(os.listdir())
print("Calibrating...")
with m as source:
    r.adjust_for_ambient_noise(source,duration=3)  
print("Calibration finished")

rospy.Subscriber("ID",String,callback)

rospy.spin()
