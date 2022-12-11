import numpy as np
import cv2
import tensorflow as tf
from argparse import ArgumentParser
import os

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
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/300)), 8)
    return frameOpencvDnn, bboxes

parser = ArgumentParser()
parser.add_argument('--padding', type=float, default=0.2)
parser.add_argument('--face_path', help='Folder where the images will be saved', type=str)
parser.add_argument('--pps', help='photos per second', type=int, default=1)
args = parser.parse_args()

# Initialize detector
faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, faceProto)


padding = args.padding
INPUT_SIZE = (224,224)
PATH = args.face_path

j=len(os.listdir(PATH))+1
# Read frame 
cap = cv2.VideoCapture(0)
fps= int(cap.get(cv2.CAP_PROP_FPS))
count=1
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
        if count%(fps/args.pps)==0:
            cv2.imwrite(PATH+"/img_"+str(j)+".jpg", resized_face)
            print("img_"+str(j)+".jpg saved")
            j+=1
    count+=1
    cv2.imshow("Emotion Demo", frameFace)
    cv2.waitKey(1)
cv2.destroyAllWindows()    
