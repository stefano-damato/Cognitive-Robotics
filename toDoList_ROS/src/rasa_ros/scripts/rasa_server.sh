#!/bin/bash

BOT_DIR="$HOME/Cognitive/Cognitive-Robotics-main/cogrob_chatbot"

cd $BOT_DIR

rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api
