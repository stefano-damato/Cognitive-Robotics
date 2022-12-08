#!/usr/bin/env python3

import rospy
from rasa_ros.srv import Dialogue, DialogueResponse, Text2Speech
from std_msgs.msg import String
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
        terminal.set_text(bot_answer.answer)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


def main():
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    global dialogue_service, terminal
    dialogue_service=rospy.ServiceProxy('dialogue_server', Dialogue)
    rospy.Subscriber("voice_txt", String, callback)
    terminal = TerminalInterface()

    while not rospy.is_shutdown():
        message = terminal.get_text()
        if message == 'exit': 
            break
        try:
            bot_answer = dialogue_service(message)
            terminal.set_text(bot_answer.answer)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass