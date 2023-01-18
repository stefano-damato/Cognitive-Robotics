#!/usr/bin/python3
from datetime import datetime as dt
import rospy
import time
import ast
import os
import json
from std_msgs.msg import String
from rasa_ros.srv import Text2Speech

# Function used to open the toDoList file, read it and import its content as a dictionary in which the key is activity name
# and the value is a list containing the activity properties.
def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict

# Callback function activated when a new message is published on the topic "ID" by the reidentification node. It updates the
# global variable "name", used to identify the current user.
def callback1(msg):
    global name
    name = msg.data

# Definition of the global variable "name", used to identify the current user.
global name
# Default value of "name" if no message has yet been correctly received from the subscription to the "ID" topic.
name = "default"
FILENAME="_toDoList.txt"

rospy.init_node('alert_node')
# Subscription to the "ID" topic, on which the reidentification node publishes the current user recognized by the artificial
# vision module.
rospy.Subscriber("ID",String,callback1)

# Open the json config file
with open('config.json', 'r') as f:
  config = json.load(f)

# Checks in the config file if Pepper has to be used, and in that case initialize the service proxy for the "tts" service.
pepper = config["PEPPER"]
if pepper:
    rospy.wait_for_service('tts')
    text2speech_node=rospy.ServiceProxy('tts', Text2Speech) 

# Main loop executed until the shutdown signal is received from ROS.
while not rospy.is_shutdown():
    time.sleep(20)
    # Builds the file_path string concatenating the path to the toDoList files location and the name of the specific toDoList file,
    # which contains the name of the current user.    
    if name != "unknown":
        file_path = "cogrob_chatbot/" + name + FILENAME
        datetime_object_now = dt.now()
        
        # Import the toDoList file as a dictionary
        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            print("Wrong file path!")
            toDoList={}

        # Iterates on the dictionary checking on the "deadline" field in its list values. If the difference between the current
        # date and time and the one indicated in the dictionary for a specific activity is of 1, 30 or 60 minutes, it remind the
        # user about the activity using the "tts" service
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

    
