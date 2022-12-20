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


def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict

def callback(msg):

    name = msg
    print(os.listdir())
    if name != "unknown":
        file_path = name + FILENAME
        toDoList=importDict(file_path)
        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            print("Wrong file path!")
            toDoList={}

        st.title(name + "'s to do list")
        #image = Image.open('data/diabetes_image.jpg')
        #st.image(image, use_column_width=True)
        for key, value in toDoList.items():
            st.markdown("- " + key + ", " + value[0])
        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)
        if pepper:
            load_url_node("http://192.168.1.152:8501")

def main():
    global FILENAME
    FILENAME="_toDoList.txt"

    rospy.init_node('website_node')
    rospy.Subscriber("ID",String,callback)

    with open('config.json', 'r') as f:
        config = json.load(f)

    global pepper
    pepper = config["PEPPER"]
    if pepper:
        rospy.wait_for_service('load_url')
        load_url_node=rospy.ServiceProxy('load_url', LoadUrl) 

    callback("Benedetto")

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass