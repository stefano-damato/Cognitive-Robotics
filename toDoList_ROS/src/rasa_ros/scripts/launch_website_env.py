#!/usr/bin/python3

import subprocess
import os
import signal
import time
import ast
import json
import rospy
from std_msgs.msg import String


def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict


def callback(msg):

    global prev_toDoList, sub_pro
    name = msg#.data
    if name != "unknown":
        file_path = "cogrob_chatbot/" + name + FILENAME
        file_path = name + FILENAME

        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            print("Wrong file path!")
            toDoList={}

        if prev_toDoList != toDoList:
            if sub_pro is not None:
                os.killpg(os.getpgid(sub_pro.pid), signal.SIGTERM)

            prev_toDoList = toDoList
            toDoList = dict(sorted(toDoList.items(), key=lambda item: item[1][1], reverse=True))
            sub_pro = subprocess.Popen([python_bin, "-m", "streamlit", "run", script_file], preexec_fn=os.setsid)
            if pepper:
                load_url_node("http://192.168.1.152:8501")

home = os.path.expanduser('~')
# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/website_virtualenv/
python_bin = home + "/website-env/bin/python"

# Path to the script that must run under the virtualenv
script_file = home + "/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/scripts/website.py"

global FILENAME, pepper, prev_toDoList, sub_pro
sub_pro = None
prev_toDoList = dict
FILENAME="_toDoList.txt"

"""with open('config.json', 'r') as f:
    config = json.load(f)

#threading.Thread(target=lambda: rospy.init_node('website_node', disable_signals=True)).start()
rospy.init_node('website_node')
rospy.Subscriber("ID",String,callback)

pepper = config["PEPPER"]

if pepper:
    rospy.wait_for_service('load_url')
    load_url_node = rospy.ServiceProxy('load_url', LoadUrl) """

pepper = False

callback("Benedetto")

