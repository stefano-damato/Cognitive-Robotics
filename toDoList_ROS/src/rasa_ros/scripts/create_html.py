#!/usr/bin/env python3
import os
import time
import ast
import rospy
import json
from std_msgs.msg import String
from datetime import datetime as dt
from rasa_ros.srv import LoadUrl

def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict

def callback(msg):
    global prev_toDoList
    name = msg.data
    if name != "unknown":
        file_path = "cogrob_chatbot/" + name + FILENAME
        #file_path = name + FILENAME

        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            print("Wrong file path!")
            toDoList={}

        if prev_toDoList != toDoList:
            prev_toDoList = toDoList
            toDoList = dict(sorted(toDoList.items(), key=lambda item: item[1][1], reverse=True))
            f = open('/opt/lampp/htdocs/toDoList.html', 'w')
            i=1
            # the html code which will go in the file GFG.html
            html_template = """<html>
            <head>
            <h1>""" + name + """'s to do list:</h1>
            </head>
            <body>
            <ul>"""
            dt_string = dt.now().strftime("%m/%d/%Y, %H:%M")
            for key, value in toDoList.items():
                if value[1] < dt_string:
                    html_template = html_template +"""<li style="margin-bottom:-5px;" type="disc" class="activity">""" + key +  """</li> <span style="margin-bottom:-8px;" class="category">""" + value[0] + """<br><span style="margin-bottom:-12px;" class="deadline_expired"> """ + value[1] + """<hr>"""
                else:
                    html_template = html_template + """<li style="margin-bottom:-5px;" type="circle" class="activity">""" + key +  """</li> <span style="margin-bottom:-8px;" class="category">""" + value[0]
                    if value[1] != "12/31/2050, 23:59":
                        html_template = html_template + """<br><span style="margin-bottom:-12px;" class="deadline"> """ + value[1] + """<hr>"""
                    else:
                        html_template = html_template + """<br><hr>"""
            html_template = html_template + """</ul>
            <style>
            .activity {
                font-size:30px !important;
                color: black
            }
            .category {
                font-size:25px;
                color: grey;
                padding-left:50px;
            }
            .deadline{
                font-size:25px;
                color: grey;
                padding-left:50px;
            }
            .deadline_expired{
                font-size:25px;
                color: red;
                padding-left:50px;
            }
            br {
                display: block;
                margin: 0.5px 0;
            }
            hr{
                margin-top: 1px;
                margin-bottom: 3px;
            }

            </style>
            </body>
            </html>
            """

            # writing the code into the file
            f.write(html_template)

            # close the file
            f.close()

            if pepper:
                load_url_node(url)

global FILENAME, pepper, prev_toDoList, url
prev_toDoList = dict
url = "http://localhost/toDoList.html"
FILENAME="_toDoList.txt"

with open('config.json', 'r') as f:
    config = json.load(f)

#threading.Thread(target=lambda: rospy.init_node('website_node', disable_signals=True)).start()
rospy.init_node('website_node')
rospy.Subscriber("ID",String,callback)

pepper = config["PEPPER"]

if pepper:
    rospy.wait_for_service('load_url')
    load_url_node = rospy.ServiceProxy('load_url', LoadUrl) 

while not rospy.is_shutdown():
    rospy.spin()
#pepper = False

