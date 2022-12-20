#!/usr/bin/python3

import rospy
from optparse import OptionParser
from naoqi import ALProxy
from std_msgs.msg import Bool
import time

class IsSpeakingNode:
    
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.memory = ALProxy("ALMemory", options.ip, int(options.port))

    def is_speaking(self):
        is_done_speaking = self.memory.getData("ALTextToSpeech/TextDone")
        if not is_done_speaking == None:
            is_done_speaking = int(is_done_speaking)
            if is_done_speaking == 0:
                return True
        return False

    def onTextDone(self):
       

if __name__ == "__main__":
    import time
    time.sleep(3)
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    rospy.init_node('is_speaking_node')
    pub = rospy.Publisher('is_speaking', Bool, queue_size=10)


    try:
        isnode = IsSpeakingNode(options.ip, int(options.port))
        while not rospy.is_shutdown():
            pub.publish(isnode.is_speaking())
            time.sleep(1)

        #isnode.memory.subscribeToEvent("ALTextToSpeech/TextDone", "IsSpeakingNode", "onTextDone")
    except rospy.ROSInterruptException:
        pass