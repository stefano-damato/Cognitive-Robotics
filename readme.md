First step: 

Only the first time, run the install_dependencies.bash file through the command "sudo bash install_dependencies.bash" to install all the required dependencies.

Second step:

In one terminal tab run the command "sudo docker run -p 8000:8000 rasa/duckling" to run a duckling server in the docker container.

Third step:

Change the strings in toDoList_ROS/src/rasa_ros/scripts/rasa_action.sh and in toDoList_ROS/src/rasa_ros/scripts/rasa_server.sh relative to the absolute path of the rasa chatbot directory, named cogrob_chatbot.

Fourth step:

Enter in the toDoList directory and run the following commands: 
"catkin build"
"source devel/setup.bash"
"roslaunch rasa_ros dialogue.xml"

