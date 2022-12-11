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
global label
label = ""
# this is called from the background thread
def callback(audio):
    print("callback")
    global label
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    id = rospy.wait_for_message("ID",String)
    try:
        spoken_text= r.recognize_google(audio_data, language='it-IT')
        print("Google Speech Recognition pensa che "+label+" abbia detto: " + spoken_text)
        #pub1.publish(audio) # Publish audio only if it contains words
        if id.data != label:
            label = id.data
            pub.publish("Hi, I am "+ label)
        else: 
            pub.publish(spoken_text)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

        
def callback_label(audio):
    print("callback_label")
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    id = rospy.wait_for_message("ID",String)
    try:
        spoken_text= r.recognize_google(audio_data, language='it-IT')
        print("Google Speech Recognition pensa che "+label+" abbia detto: " + spoken_text)
        #pub1.publish(audio) # Publish audio only if it contains words
        pub2.publish(spoken_text)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def listener():
    print("Devo entrare in callback")
    rospy.Subscriber("mic_data", Int16MultiArray, callback)
    print("Sono entrato in callback")
    rospy.Subscriber("mic_data_label", Int16MultiArray, callback_label)
    print("Sono entrato in callback_label")
    rospy.spin()

if __name__ == '__main__':
    listener()
