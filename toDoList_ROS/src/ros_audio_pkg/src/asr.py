#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

from speech_recognition import AudioData
import speech_recognition as sr

# Initialize a Recognizer
r = sr.Recognizer()

# Init node
rospy.init_node('speech_recognition', anonymous=True)
#pub1 = rospy.Publisher('voice_data', Int16MultiArray, queue_size=10)
#pub2 = rospy.Publisher('voice_txt', String, queue_size=10)
pub = rospy.Publisher('text_to_bot', String, queue_size=10)
pub2 = rospy.Publisher('text_for_reidentification', String, queue_size=10)


current_user = ""
def callback1(msg):
    global id
    if msg.data!="NO":
        id=msg.data
    print("label "+msg.data)
# this is called from the background thread
def callback(audio):
    global current_user,id
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    print("id "+id)
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
        
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
        pub2.publish("RIPETI")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def listener():
    rospy.Subscriber("mic_data", Int16MultiArray, callback)
    rospy.Subscriber("ID",String,callback1)
    #rospy.Subscriber("mic_data_label", Int16MultiArray, callback_label)
    rospy.spin()

if __name__ == '__main__':
    listener()

