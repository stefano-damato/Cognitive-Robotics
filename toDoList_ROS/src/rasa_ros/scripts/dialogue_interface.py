#!/usr/bin/env python3

import rospy
from rasa_ros.srv import Dialogue, DialogueResponse, Text2Speech
from std_msgs.msg import String
import json
import os
class TerminalInterface:
    '''Class implementing a terminal i/o interface. 

    Methods
    - get_text(self): return a string read from the terminal
    - set_text(self, text): prints the text on the terminal

    '''

    def get_text(self):
        return input("[IN]:  ") 

    def set_text(self,text):
        print("[OUT]:",text)

def callback(msg):
    message = msg.data
    if message == 'exit': 
        exit
    try:
        bot_answer = dialogue_service(message)
        if pepper:
            text2speech_node(bot_answer.answer)
        terminal.set_text(bot_answer.answer)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def main():
    global dialogue_service, terminal, text2speech_node
    dialogue_service=rospy.ServiceProxy('dialogue_server', Dialogue)
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    if pepper:
        # Check if the 'tts' service is available to perform the text-to-speech
        rospy.wait_for_service('tts')
        text2speech_node=rospy.ServiceProxy('tts', Text2Speech)
    print("Ready")
    # Subscribe to this topic to retrive the phrase that Pepper will utter
    rospy.Subscriber("text_to_bot", String, callback)
    terminal = TerminalInterface()

    while not rospy.is_shutdown():
        rospy.spin()

with open('config.json', 'r') as f:
  config = json.load(f)

pepper = config["PEPPER"]

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass
