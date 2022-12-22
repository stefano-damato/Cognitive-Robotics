#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import streamlit as st
import joblib
import pandas as pd
from PIL import Image
import ast
import os
import json
import threading
from datetime import datetime as dt
import time


def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict

def callback():

    placeholder = st.empty() 
    prev_toDoList = dict
    while not rospy.is_shutdown():
        name = rospy.wait_for_message("ID",String)
        name = name.data
        print("received name:" + name)
        global previous_name
        dt_string = dt.now().strftime("%m/%d/%Y, %H:%M")
        if name != "unknown":
            previous_name = name
            file_path = "cogrob_chatbot/" + name + FILENAME
            toDoList=importDict(file_path)

            if(os.path.exists(file_path)):
                toDoList=importDict(file_path)
            else:
                print("Wrong file path!")
                toDoList={}

            if prev_toDoList != toDoList:
                
                prev_toDoList = toDoList
                toDoList = dict(sorted(toDoList.items(), key=lambda item: item[1][1], reverse=True))
                
                placeholder.empty()
                with placeholder.container():
                    st.title(name + "'s to do list:")
                    #image = Image.open('data/diabetes_image.jpg')
                    #st.image(image, use_column_width=True)

                    i=0
                    for key, value in toDoList.items():
                        if value[1] < dt_string:
                            st.markdown('<li id=li_' + str(i) + ' style="margin-bottom:-8px;" type="disc" class="activity">' + key +  '</li> <span style="margin-bottom:-8px;" class="category">' + value[0] + '<br><span style="margin-bottom:-12px;" class="deadline_expired"> ' + value[1] + '<hr>' , unsafe_allow_html=True)
                        else:
                            st.markdown('<li id=li_' + str(i) + ' style="margin-bottom:-8px;" type="circle" class="activity">' + key +  '</li> <span style="margin-bottom:-8px;" class="category">' + value[0], unsafe_allow_html=True)
                            if value[1] != "12/31/2050, 23:59":
                                st.markdown('<br><span style="margin-bottom:-12px;" class="deadline"> ' + value[1] + '<hr>' , unsafe_allow_html=True)
                            else:
                                st.markdown('<hr>', unsafe_allow_html=True)
                        i = i + 1


                st.markdown('''
                <style>
                .activity {
                    font-size:25px !important;
                }
                .category {
                    font-size:20px;
                    color: grey;
                    padding-left:50px;
                }
                .deadline{
                    font-size:20px;
                    color: grey;
                    padding-left:50px;
                }
                .deadline_expired{
                    font-size:20px;
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
                ''', unsafe_allow_html=True)
                if pepper:
                    load_url_node("http://192.168.1.152:8501")
        time.sleep(4)
    

global FILENAME, previous_name
FILENAME="_toDoList.txt"
previous_name = ""

threading.Thread(target=lambda: rospy.init_node('website_node', disable_signals=True)).start()
#rospy.Subscriber("ID",String,callback)

with open('config.json', 'r') as f:
    config = json.load(f)

global pepper
pepper = config["PEPPER"]
if pepper:
    rospy.wait_for_service('load_url')
    load_url_node = rospy.ServiceProxy('load_url', LoadUrl) 

callback()
