#!/usr/bin/python3
from datetime import datetime as dt
import rospy
import time
import ast
import os
import json
from std_msgs.msg import String
from rasa_ros.srv import Text2Speech

def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict

def callback1(msg):
    
    name = msg.data
    if name != "unknown":
        file_path = "cogrob_chatbot/" + name + FILENAME
        dt_string = dt.now().strftime("%m/%d/%Y, %H:%M")
        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            print("Wrong file path!")
            toDoList={}

        for key, values in toDoList.items():
            print(values[1])
            if(dt_string == values[1] and values[2]):
                print("Attention " + name + ", you  have to do " + key + ", for category " + values[0])
                if pepper:
                    text2speech_node("Attention " + name + ", you  have to do " + key + ", for category " + values[0])

    time.sleep(20)

FILENAME="_toDoList.txt"

rospy.init_node('alert_node')
rospy.Subscriber("ID",String,callback1)

with open('config.json', 'r') as f:
  config = json.load(f)

pepper = config["PEPPER"]
if pepper:
    rospy.wait_for_service('tts')
    text2speech_node=rospy.ServiceProxy('tts', Text2Speech) 

while not rospy.is_shutdown():
    rospy.spin()