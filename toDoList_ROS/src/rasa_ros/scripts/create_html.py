#!/usr/bin/env python3
import os
import time
import ast
import rospy
import json
from std_msgs.msg import String
from datetime import datetime as dt
import socket
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
            <ul class="SG">"""
            dt_string = dt.now().strftime("%m/%d/%Y, %H:%M")
            for key, value in toDoList.items():
                if value[1] < dt_string:
                    html_template = html_template +"""<li class="sgLi"><div class="box_expired"><h3>""" + key +  """</h3><ul class="df"><li>""" + value[0] + """</li><li>""" + value[1] + """</li></ul></div>"""
                else:
                    html_template = html_template +"""<li class="sgLi"><div class="box"><h3>""" + key +  """</h3><ul class="df"><li>""" + value[0] + """</li>"""
                    if value[1] != "12/31/2050, 23:59":
                        html_template = html_template + """<li>""" + value[1] + """</li></ul></div>"""
                    else:
                        html_template = html_template + """</ul></div>"""
            html_template = html_template + """</ul>
            <style>
            body{
            padding: 0 2%;
            color: #2e3e50;
            background: #F7EAD6;
            }
            .X{
            margin: auto;
            padding: 1% 2%;
            max-width: 1440px;
            border-radius: 5px;
            background: #ecf0f1;
            box-shadow: 0 2px 6px 0 rgba(0,0,0, .3);
            }
            h1,h2,h3{
            text-align: center;
            font-family: 'Chalkduster', fantasy;
            }
            h1{
            color: #000000;
            }
            h3{
            color: #000000;
            }
            li{
            color: #2c3e50;
            font-size: 18px;
            line-height: 30px;
            text-align: justify;
            letter-spacing: 1px;
            font-family: 'Chalkduster', fantasy;
            }
            /*SG = style grid*/
            .SG{
            margin: 0;
            padding: 0;
            text-align: center;
            }
            .SG .sgLi{
            min-width: 24%;
            margin: 2% .35%;
            display: inline-flex;
            box-shadow: 0 2px 4px rgba(0,0,0, .2);
            }
            .SG .sgLi:hover{
            box-shadow:0 5px 10px rgba(0,0,0,.15);}
            .SG .box{
            width: 100%;
            height: 100vh;
            padding: 1% 2%;
            background: #EFCF2D;
            min-height: 200px;
            max-height: 220px;
            box-sizing: border-box;
            }
            .box_expired{
            width: 100%;
            height: 100vh;
            padding: 1% 2%;
            background: #ef2d2d;
            min-height: 200px;
            max-height: 220px;
            box-sizing: border-box;
            }
            /*Styles */
            .df{list-style-type: disc;}
            .s1{list-style-type: square;}
            .s2{list-style-type: circle;}
            .s3{list-style-type: decimal;}
            .s4{list-style-type: decimal-leading-zero;}
            .s5{list-style-type: lower-alpha;}
            .s6{list-style-type: upper-alpha;}
            .s7{list-style-type: lower-roman;}
            .s8{list-style-type: upper-roman;}
            .s9{list-style-type: lower-greek;}
            .s10{list-style-type: georgian;}
            .s11{list-style-type: hebrew;}
            .s12{list-style-type: hiragana;}
            .s13{list-style-type: hiragana-iroha;}
            .s14{list-style-type: katakana;}
            .s15{list-style-type: katakana-iroha;}
            .s16{list-style-type: cjk-ideographic;}
            .s17{list-style-image: url(//goo.gl/L3tqpe);}
            .s18{list-style: none;}
            .s18 li:before{
            content: '';
            width: 20px;
            height: 20px;
            margin-right: 15px;
            display: inline-block;
            background: url(//goo.gl/lcPSVD);
            background-position: 50%;
            }
            .s19{list-style: none;}
            .s19 li:before{
            content: '\f0a9';
            margin-right: 15px;
            font-family: FontAwesome;
            }

            /* responsive grid*/
            @media (max-width: 970px){
            .SG .sgLi{width: 180px;}}
            @media (max-width: 425px){
            .SG .sgLi{width: 100%;}
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
ip = socket.gethostbyname(socket.gethostname())
url = "http://" + ip + "/toDoList.html"
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

