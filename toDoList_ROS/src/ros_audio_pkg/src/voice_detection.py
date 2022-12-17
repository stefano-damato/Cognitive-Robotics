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


def asr(audio,id):
    global current_user
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    print("id "+id)
    try:
        spoken_text= r.recognize_google(audio_data, language='it-IT')
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
        return True
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
        return False
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return False


def callback1(msg):
    global is_there_anyone
    is_there_anyone=msg.data
    print("Current user: ", current_user)

def callback(msg):
    label=msg.data
    print("voice "+ label)
    print("Posso? ",is_there_anyone)
    if is_there_anyone:
        while True:
            print("Recording...")
            with m as source:
                try:  
                    # listen for 1 second, then check again if the stop function has been called
                    print("here ", TIMEOUT, PRHASE_TIME_LIMIT)
                    audio = r.listen(source, timeout=TIMEOUT,phrase_time_limit=PRHASE_TIME_LIMIT)
                except Exception:
                    print("TimeOUT expired")
                    continue
                else:
                    print("CIAO MONDOOOO")
                    data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
                    data_to_send = Int16MultiArray()
                    data_to_send.data = data
                    if asr(data_to_send,label):
                        print("break")
                        break
                    """pub.publish(data_to_send)
                    pub2.publish(label)"""
        

    
pub = rospy.Publisher('text_to_bot', String, queue_size=10)
pub2 = rospy.Publisher('text_for_reidentification', String, queue_size=10)
rospy.init_node('voice_detection_node', anonymous=True)


is_there_anyone=True
current_user=" "

with open('config.json', 'r') as f:
  config = json.load(f)
TIMEOUT = config["TIMEOUT"]
PRHASE_TIME_LIMIT = config["PRHASE_TIME_LIMIT"]


# Initialize a Recognizer
r = sr.Recognizer()

# Audio source
global m
m = sr.Microphone(device_index=None,
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
rospy.Subscriber("is_there_anyone",Bool,callback1)

rospy.spin()
