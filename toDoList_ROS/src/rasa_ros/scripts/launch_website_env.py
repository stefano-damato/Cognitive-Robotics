#!/usr/bin/python3

import subprocess
import os

home = os.path.expanduser('~')
# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/website_virtualenv/
python_bin = home + "/website-env/bin/python"

# Path to the script that must run under the virtualenv
script_file = home + "/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/scripts/website.py"

subprocess.Popen([python_bin, "-m", "streamlit", "run", script_file])
