import numpy as np
import cv2
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import pickle
import os
from glob import glob
from scipy.spatial.distance import cosine
from argparse import ArgumentParser
from sklearn.metrics import accuracy_score, confusion_matrix


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
parser.add_argument('--test_path', help='Folder where the test images are saved', type=str)
parser.add_argument('--n_images_for_person', help='Number of images used for a known person', type=int, default=None)
parser.add_argument('--training', type=int, default=0)
parser.add_argument('--file_name',  type=str, help="The name of the database file", default=None)
parser.add_argument('--model',  type=str, help="The name of the vgg model", default='resnet50')
args = parser.parse_args()

model_name=args.model
# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model=model_name, include_top=False, pooling='avg')

save_path="Result_"+model_name+".txt"


# Dataset path - Folder in which the faces are saved
data_path=args.data_path
test_path=args.test_path

padding = args.padding
INPUT_SIZE = (224,224)
rejection_threshold=args.rejection_threshold

file_name=args.file_name

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
print(len(database))


# Test on the TestSet
groundtruth = []
predictions = []

for dirs in os.listdir(test_path):
    person_path = os.path.join(test_path, dirs)
    print(person_path)
    count = 0
    for filename in glob(os.path.join(person_path,'*.jpg')):
        # Preprocess image
        resized_face = cv2.resize(filename,INPUT_SIZE)
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
        groundtruth.append(dirs)
        predictions.append(min_distance[0])

accuracy = accuracy_score(groundtruth, predictions)
print("Accuracy score: %.3f" % (accuracy))
print("Normalized confusion matrix\n %s" % (confusion_matrix(groundtruth, predictions, normalize='true')))

res = "The accuracy of the %s model is %.3f"% (model_name,accuracy)
with open(save_path,"w") as f:
    f.write(res)
         