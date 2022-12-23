#!/usr/bin/env python3

import argparse
import streamlit as st
from datetime import datetime as dt
import time


def createWebPage(name):

    #placeholder = st.empty() 
    print("received name:" + name)
    dt_string = dt.now().strftime("%m/%d/%Y, %H:%M")
    toDoList = dict
    #placeholder.empty()
    #with placeholder.container():
    st.title(name + "'s to do list:")
        
    for key, value in toDoList.items():
        if value[1] < dt_string:
            st.markdown('<li style="margin-bottom:-8px;" type="disc" class="activity">' + key +  '</li> <span style="margin-bottom:-8px;" class="category">' + value[0] + '<br><span style="margin-bottom:-12px;" class="deadline_expired"> ' + value[1] + '<hr>' , unsafe_allow_html=True)
        else:
            st.markdown('<li style="margin-bottom:-8px;" type="circle" class="activity">' + key +  '</li> <span style="margin-bottom:-8px;" class="category">' + value[0], unsafe_allow_html=True)
            if value[1] != "12/31/2050, 23:59":
                st.markdown('<br><span style="margin-bottom:-12px;" class="deadline"> ' + value[1] + '<hr>' , unsafe_allow_html=True)
            else:
                st.markdown('<hr>', unsafe_allow_html=True)


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
        
    time.sleep(4)
    st.stop()
    
parser = argparse.ArgumentParser()
#parser.add_argument('--toDoList', type=dict, required=True)
#parser.add_argument('--name', type=str, required=True)
args = parser.parse_args()

createWebPage("Benedetto")
