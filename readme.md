# To_DO_List with Pepper
This is a Univeristy project with the goal of develop a robotic assistant for helping people in managing their personal to do lists.

The management of the to do list is done through a RASA chatbot.
  
The robotic platform:
- communicates with its users through spoken natural language.
- recognize the user through facial recognition and if it does not recognize it, it creates a new one.

## Initial Setup

### Path to the chatbot server

Change the strings in `toDoList_ROS/src/rasa_ros/scripts/rasa_action.sh` and in `toDoList_ROS/src/rasa_ros/scripts/rasa_server.sh` relative to the absolute path of the rasa chatbot directory, named `cogrob_chatbot`.

### Creation of the Database of the knowing people

To start the conversation with already known identities, you need to create the **database of known people**. Go in the folder `createdatabase` and run the following command to add photos in the image folder:
```
python3 Take_photo.py --face_path img/name_of_the_person --pps 2
```
To obtain the file containing the new database that will be used from the face recognition model run:
```
python3 Image_reidentification.py --data_path img --training 1 --file_name data
```
Now you can move the `data.pickle` in the ros pakage where the `reidentification_node` is containing.

### Config File
1. Incude config file and other directories in the ros workspace, from the directory of ros (usually $HOME/.ros) run the command:
```
ln -s ~/Cognitive-Robotics/toDoList_ROS/config.json ./
ln -s ../Cognitive-Robotics/cogrob_chatbot/ ./
```

### Microphone and Webcam node
1. Find the michrophone index with:
```python
import sounddevice as sd
sd.query_devices()
```
Set the index in the file `voice_detection.py`
2. Find the webcam index with:

### Dependencies:

1. To install all the required dependencies run the `install_dependencies.bash` file with the command:
```
sudo bash install_dependencies.bash
```
2. Create a virtual environment where to install all the dependencies for the VGGFace model.
```
sudo bash install_dependencies.bash
```

## Creating virtual environments
1. Create the first virtual environment for streamlit application. In the root directory run:
```
python3 -m venv website-env
source website-env/bin/activate
cd Cognitive-Robotics
bash
pip install -r website_requirements.txt
deactivate
cd ..
```

2.

## How to run the application
Go in the ROS workspace and for every point in this list open a new terminal tab
1. run a duckling server in the docker container with the command:
```
sudo docker run -p 8000:8000 rasa/duckling
```
2. Launch the ROS Master with the command:
```
roscore
```
3. Launch the chatbot and the pepper nodes with:
```
roslaunch rasa_ros dialogue.launch
```
4. Launch the face recognition nodes with:
```
roslaunch detector recognition.launch
```
5. Launch the speech recognition nodes with:
```
roslaunch ros_audio_pkg speech_recognition.launch
```

## Application Demo

## Authors
- Cirillo Benedetto @bcirillo99
- D'Amato Stefano @stefano-damato
- De Gruttola Andrea @sudousernameavailable

