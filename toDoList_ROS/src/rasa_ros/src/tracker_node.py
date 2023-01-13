#!/usr/bin/python3
from utils import Session
from rasa_ros.srv import Text2Speech
from optparse import OptionParser
import rospy

'''
This class implements a ROS node able to follow the face of the interlocutor 
'''
class TrackerNode:
    
    '''
    The costructor creates a session to Pepper and inizializes the services
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.session = Session(ip, port)
        self.tracker = self.session.get_service("ALTracker")

     
    '''
    Rececives a Text2Speech message and call the ALTextToSpeech service.
    The robot will play the text of the message
    '''
    def start_track(self):
      print("ALTracker successfully started, now show your face to robot!")
      self.tracker.registerTarget("Face", 0.1)
      # Then, start tracker.
      self.tracker.track("Face")

    def stop_track(self):
      print( "ALTracker stopped.")
      self.tracker.stopTracker()
      self.tracker.unregisterAllTargets()
        
    
    '''
    Starts the node and create the tts service
    '''
    def start(self):
        rospy.init_node("tracker_node")
        self.start_track()
        rospy.spin()

if __name__ == "__main__":
    import time
    time.sleep(3)
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        ttsnode = TrackerNode(options.ip, int(options.port))
        ttsnode.start()
    except rospy.ROSInterruptException:
        pass
