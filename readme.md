# To_DO_List with Pepper
This is a Univeristy project with the goal of develop a robotic assistant for helping people in managing their personal to do lists.

The management of the to do list is done through a RASA chatbot.
  
The robotic platform:
- communicates with its users through spoken natural language.
- recognize the user through facial recognition and if it does not recognize it, it creates a new one.

## Initial Setup

### Add pip bin to PATH
Modify the .bashrc file in HOME, adding the line:
```
PATH="$HOME/.local/bin:$HOME/bin:$PATH"
```

### Path to the chatbot server

Change the strings in `toDoList_ROS/src/rasa_ros/scripts/rasa_action.sh` and in `toDoList_ROS/src/rasa_ros/scripts/rasa_server.sh` relative to the absolute path of the rasa chatbot directory, named `cogrob_chatbot`.

### Creating virtual environments
1. Create a virtual environment for VGGFace application. In the root directory run:
```
python3 -m venv python-env
source python-env/bin/activate
cd Cognitive-Robotics
pip install -r VGG_requirements.txt
deactivate
cd ..
```

In case of ModuleNotFoundError: No module named 'keras.engine.topology'
Change from keras.engine.topology import get_source_inputs 
to from keras.utils.layer_utils import get_source_inputs
in file /python-env/lib/python3.8/site-packages/keras_vggface/models.py


### Microphone and Webcam node
1. Find the michrophone index with:
```python
import sounddevice as sd
sd.query_devices()
```
Set the index in the file `voice_detection.py`
2. Find the webcam index with:
```
sudo apt-get install v4l-utils
v4l2-ctl --list-devices
sudo apt install ffmpeg
ffplay /dev/video_indices
```
Substitute "video_indices" with the listed cameras from the previous command to check the webcam to use. 

### Creation of the Database of the knowing people

To start the conversation with already known identities, you need to create the **database of known people**. Go in the folder `createdatabase` and run the following command to add photos in the image folder:
```
python3 Take_photo.py --face_path img/your_name --pps 2 --camera_index chosen_camera
```
Substitute "your_name" with your name and "chosen_camera" with the index of the camera checked at the previous point.
To obtain the file containing the new database that will be used from the face recognition model run:
```
source ~/python-env/bin/activate
python3 Image_reidentification.py --data_path img --traineing 1 --file_name data
deactivate
```
Now you can move the `data.pickle` in the ros pakage where the `reidentification_node` is containing.

### Symbolinc links
Incude config file and other files in the ros workspace, from the directory of ros (usually $HOME/.ros) run the command:
```
ln -s ~/Cognitive-Robotics/toDoList_ROS/config.json ./
ln -s ../Cognitive-Robotics/cogrob_chatbot/ ./
```

### Dependencies:
1. To install all the required dependencies run the `install_dependencies.bash` file with the command:
```
sudo bash install_dependencies.bash
sudo bash audio_setup.sh
pip3 install git+https://github.com/eric-wieser/ros_numpy
```
2. QI dependencies:
```
sudo apt install -y python3-rosdep python3-pip python3-catkin-tools git
WS=$HOME/catkin_ws/src
mkdir -p $WS
cd $WS
wget https://github.com/aldebaran/libqi-python/releases/download/qi-python-v3.0.0/qi-3.0.0-cp38-cp38-linux_x86_64.whl
python3 -m pip install ./qi*
rm qi-3.0.0*
sudo rosdep init
rosdep update
```


## How to run the application
Go in the ROS workspace and for every point in this list open a new terminal tab and re-source with:
```
source devel/setup.bash
```
1. run a duckling server in the docker container with the command:
```
sudo docker run -p 8000:8000 rasa/duckling
```
2. Launch the ROS Master with the command:
```
roscore
```
3. Build the workspace:
```
catkin build
```
4. Launch the chatbot and the pepper nodes with:
```
roslaunch rasa_ros dialogue.launch
```
5. Launch the face recognition nodes with:
```
roslaunch detector recognition.launch
```
6. Launch the speech recognition nodes with:
```
roslaunch ros_audio_pkg speech_recognition.launch
```

## Application Demo

## Authors
- Cirillo Benedetto @bcirillo99
- D'Amato Stefano @stefano-damato
- De Gruttola Andrea @sudousernameavailable

