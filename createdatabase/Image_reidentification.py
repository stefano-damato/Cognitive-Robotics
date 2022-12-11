import numpy as np
import cv2
import tensorflow as tf

from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import pickle
import os
from glob import glob
from scipy.spatial.distance import cosine
from argparse import ArgumentParser


def getFaceBox(net, frame, conf_threshold=0.8):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    
    #swapRB =True
    # flag which indicates that swap first and last channels in 3-channel image is necessary.
    #crop = False
    # flag which indicates whether image will be cropped after resize or not
    # If crop is false, direct resize without cropping and preserving aspect ratio is performed
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold and detections[0, 0, i, 5]<1 and detections[0, 0, i, 6]<1:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            print((x1,y1),(x2,y2),int(round(frameHeight/300)))
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/300)), 8)
    return frameOpencvDnn, bboxes

# This method takes as input the face recognition model and the filename of the image and returns
# the feature vector
def extract_features(face_reco_model, filename):
    faceim = cv2.imread(filename)
    faceim = cv2.resize(faceim, (224,224))
    faceim = preprocess_input([faceim.astype(np.float32)], version=2)
    feature_vector = (face_reco_model.predict(faceim,verbose='false')).flatten()
    return feature_vector

def data_to_file(data_dict,name):
    with open(name, 'wb') as handle:
        pickle.dump(data_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

def data_from_file(name):
    with open(name, 'rb') as handle:
        X = pickle.load(handle)
    return X


parser = ArgumentParser()
parser.add_argument('--padding', type=float, default=0.2)
parser.add_argument('--rejection_threshold', type=float, default=0.4)
parser.add_argument('--data_path', help='Folder where the images are saved', type=str)
parser.add_argument('--n_images_for_person', help='Number of images used for a known person', type=int, default=None)
parser.add_argument('--training', type=int, default=0)
parser.add_argument('--file_name',  type=str, help="The name of the database file", default=None)
args = parser.parse_args()


# Initialize detector
faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, faceProto)

# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model='resnet50', include_top=False, pooling='avg')




# Dataset path - Folder in which the faces are saved
data_path=args.data_path



padding = args.padding
INPUT_SIZE = (224,224)
rejection_threshold=args.rejection_threshold

file_name=args.file_name
if args.training==1:
    # Creation of the database of known people
    database = []
    for dirs in os.listdir(data_path):
        person_path = os.path.join(data_path, dirs)
        print(person_path)
        count = 0
        person = []
        if args.n_images_for_person is None:
            number_of_training_images_per_person = len(os.listdir(person_path))
        else:
            number_of_training_images_per_person = args.n_images_for_person
        for filename in glob(os.path.join(person_path,'*.jpg')):
            if count < number_of_training_images_per_person:
                feature_vector = extract_features(face_reco_model, filename)
                person.append({"id": dirs, "feature_vector": feature_vector, "filename": filename})
                count += 1
                print("Loading %s - %d"%(dirs, count))
        database.append(person)
        
    data_to_file(database, file_name+".pickle")
else:
    database = data_from_file(file_name+".pickle")
print(len(database))
# Read frame 
cap = cv2.VideoCapture(0)
while(1):             
    # Take each frame
    _, frame = cap.read() # Read frame
    frameFace, bboxes = getFaceBox(faceNet, frame)     # Get face
    for i,bbox in enumerate(bboxes):
        # Adjust crop
        w = bbox[2]-bbox[0]
        h = bbox[3]-bbox[1]
        padding_px = int(padding*max(h,w))
        face = frame[max(0,bbox[1]-padding_px):min(bbox[3]+padding_px,frame.shape[0]-1),max(0,bbox[0]-padding_px):min(bbox[2]+padding_px, frame.shape[1]-1)]
        face = face[ face.shape[0]//2 - face.shape[1]//2 : face.shape[0]//2 + face.shape[1]//2, :, :]
        # Preprocess image
        resized_face = cv2.resize(face,INPUT_SIZE)
        ##
        faceim = preprocess_input([resized_face.astype(np.float32)], version=2)
        feature_vector = (face_reco_model.predict(faceim,verbose='false')).flatten()
        min_distance = ["unknown", 1000000000000]
        for person in database:
            for face in person:
                distance = cosine(feature_vector, face['feature_vector'])
                if distance < min_distance[1] and distance < rejection_threshold:
                    min_distance[0] = face['id']
                    min_distance[1] = distance
                    #print("if")
                """else:
                    #print("else")"""
        

        cv2.imshow("f%d"%i, resized_face)
        cv2.moveWindow("f%d"%i, INPUT_SIZE[0]*i, 40)
        cv2.putText(frameFace, min_distance[0], (bbox[0], bbox[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Emotion Demo", frameFace)
    cv2.waitKey(1)
cv2.destroyAllWindows()    