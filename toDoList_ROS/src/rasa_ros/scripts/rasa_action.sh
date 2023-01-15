#!/bin/bash

BOT_DIR="$HOME/Cognitive-Robotics/cogrob_chatbot"

cd $BOT_DIR

pyhton3 -m rasa run actions
