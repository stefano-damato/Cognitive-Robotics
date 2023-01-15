#!/bin/bash

BOT_DIR="$HOME/Cognitive-Robotics/cogrob_chatbot"

cd $BOT_DIR

pyhton3 -m rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api
