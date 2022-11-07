#!/bin/bash

BOT_DIR="$HOME/Desktop/Cognitive-Robotics/cogrob_chatbot"

cd $BOT_DIR

rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api
