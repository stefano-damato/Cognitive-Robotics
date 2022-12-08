#!/usr/bin/python3
from tensorflow.python.ops.gen_logging_ops import Print
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np
import pickle
import os
from rasa_ros.srv import Text2Speech

from identification.deep_speaker.audio import get_mfcc
from identification.deep_speaker.model import get_deep_speaker
from identification.utils import batch_cosine_similarity, dist2id


REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000

# Load model
model = get_deep_speaker(os.path.join(REF_PATH,'deep_speaker.h5'))

n_embs = 0
X = []
y = []

TH = 0.75


def listener():
    rospy.init_node('reidentification_node', anonymous=True)
    pub = rospy.Publisher('text_to_bot', String, queue_size=10)
    #text2speech_node=rospy.ServiceProxy('tts', Text2Speech)
    user = ""

    while not rospy.is_shutdown():
        data = rospy.wait_for_message("voice_data",Int16MultiArray)
        text = rospy.wait_for_message("voice_txt", String)

        audio_data = np.array(data.data)
        audio_text = text.data

        # to float32
        audio_data = audio_data.astype(np.float32, order='C') / 32768.0

        # Processing
        ukn = get_mfcc(audio_data, RATE)

        # Prediction
        ukn = model.predict(np.expand_dims(ukn, 0))

        if len(X) > 0:
            # Distance between the sample and the support set
            emb_voice = np.repeat(ukn, len(X), 0)

            cos_dist = batch_cosine_similarity(np.array(X), emb_voice)
            
            # Matching
            id_label = dist2id(cos_dist, y, TH, mode='avg')
        
        if len(X) == 0 or id_label is None:
            c = print("Voce non conosciuta. Vuoi inserire un nuovo campione? (S/N):")
            if user != "":
                #text2speech_node("Hi, who am I talking to?")
                name = rospy.wait_for_message("voice_txt", String)
                X.append(ukn[0])
                y.append(name.data)
                pub.publish("Hi, I am" + name.data)
                user = name.data
            else:
                #text2speech_node("Please, repeat")
                print("Please, repeat")
        else:
            print("Ha parlato:", id_label)
            if id_label != user:
                pub.publish("Hi, I am" + id_label)
                user = id_label
            else:
                pub.publish(audio_text)

        
if __name__ == '__main__':
    listener()