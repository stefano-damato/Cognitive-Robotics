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
    global name
    name = msg.data
    
global name
name = "default"
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
    time.sleep(20)
    if name != "unknown":
        file_path = "cogrob_chatbot/" + name + FILENAME
        datetime_object_now = dt.now()
        
        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            print("Wrong file path!")
            toDoList={}

        for key, values in toDoList.items():
            datetime_object = dt.strptime(values[1],"%m/%d/%Y, %H:%M")
            diff=datetime_object - datetime_object_now
            days = diff.days
            seconds = diff.seconds
            minutes = int((seconds+60)/60)
            if days==0:
                if minutes==60:
                    print("Attention " + name + ", you  have to " + key + " in one hour, for category " + values[0])
                    if pepper:
                        text2speech_node("Attention " + name + ", you  have to " + key + " in one hour, for category " + values[0])
                if minutes==30:
                    print("Attention " + name + ", you  have to " + key + " in half an hour, for category " + values[0])
                    if pepper:
                        text2speech_node("Attention " + name + ", you  have to " + key + " in half an hour, for category " + values[0])
                if minutes==1:
                    print("Attention " + name + ", you  have to " + key + " now, for category " + values[0])
                    if pepper:
                        text2speech_node("Attention " + name + ", you  have to " + key + " now, for category " + values[0])

    
