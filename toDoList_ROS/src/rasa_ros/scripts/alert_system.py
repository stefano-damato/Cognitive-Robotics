#!/usr/bin/env python3
from datetime import datetime as dt
import rospy
import time
import ast
import os

def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict

FILENAME="_toDoList.txt"

rospy.init_node('alert_node')
pub = rospy.Publisher('text_to_bot', String, queue_size=10)

while(1):
    name = rospy.wait_for_message("ID",String)
    file_path = name + FILENAME
    dt_string = dt.now().strftime("%m/%d/%Y, %H:%M")
    if(os.path.exists(file_path)):
        toDoList=importDict(file_path)
    else:
        toDoList={}

    for key, values in toDoList.items():
        if(dt_string == values[1] and values[2]):
            pub.publish("Attention " + name + ", you  have to do " + key + ", for category " + values[0])

    time.sleep(20)