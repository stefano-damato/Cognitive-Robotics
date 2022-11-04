from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
import ast
import os

def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict
def exportDict(filepath,dict):
    with open(filepath, 'w+') as f:
        f.write(str(dict))


FILENAME="toDoList.txt"

class ActionAddSubmit(Action):

    def name(self) -> Text:
        return "action_add_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        activity = tracker.get_slot("activity")
        deadline = tracker.get_slot("deadline")

        print("\nActivity:",activity)
        print("Deadline:",deadline)

        if(os.path.exists(FILENAME)):
            toDoList=importDict(FILENAME)
        else:
            toDoList={}
        #attr=list() #qui poi mettimo il campo deadline e reminder
        toDoList[activity]=deadline
        exportDict(FILENAME, toDoList)

        dispatcher.utter_message(text=f"Added activity {activity} at {deadline}")
        return [AllSlotsReset()]

class ActionDisplaySubmit(Action):

    def name(self) -> Text:
        return "action_display_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if(os.path.exists(FILENAME)):
            toDoList=importDict(FILENAME)
        else:
            toDoList={}

        i = 1

        for key,value in toDoList.items():
            dispatcher.utter_message(text=f"[{i}] Activity: {key}, deadline: {value}\n")
        return [AllSlotsReset()]