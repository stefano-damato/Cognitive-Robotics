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


FILENAME="_toDoList.txt"

class ActionAddSubmit(Action):

    def name(self) -> Text:
        return "action_add_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        activity = tracker.get_slot("activity")
        deadline = tracker.get_slot("deadline")
        reminder = tracker.get_slot("reminder")
        user_name = tracker.get_slot("user_name")

        print("\nActivity:",activity)
        print("Deadline:",deadline)

        file_path = user_name + FILENAME
        
        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            toDoList={}
        #attr=list() #qui poi mettimo il campo deadline e reminder
        toDoList[activity]=list()
        toDoList[activity].append(deadline)
        toDoList[activity].append(reminder)

        exportDict(file_path, toDoList)

        dispatcher.utter_message(text=f"Added activity {activity} at {deadline} for {user_name}")
        
        return [AllSlotsReset()]

class ActionDisplaySubmit(Action):

    def name(self) -> Text:
        return "action_display_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot("user_name")

        if(user_name is None):
            dispatcher.utter_message(text=f"Please enter your name")
            return [AllSlotsReset()]

        file_path = user_name + FILENAME

        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            toDoList={}

        dispatcher.utter_message(text=f"{user_name}'s ToDo List\n")

        i = 1

        for key,value in toDoList.items():
            dispatcher.utter_message(text=f"[{i}] Activity: {key}, deadline: {value[0]}, reminder: {value[1]}\n")
            i+=1
        return [AllSlotsReset()]

class ActionRemoveSubmit(Action):

    def name(self) -> Text:
        return "action_remove_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity = tracker.get_slot("activity")
        user_name = tracker.get_slot("user_name")

        file_path = user_name + FILENAME

        print("\nActivity:",activity)

        if(not os.path.exists(file_path)):
            dispatcher.utter_message(text=f"There are no activities")
            return [AllSlotsReset()]
        else:
            toDoList=importDict(file_path)
            if(activity not in toDoList):
                dispatcher.utter_message(text=f"There is no such activity")
                return [AllSlotsReset()]
            else:
                removed_activity=toDoList.pop(activity)
        exportDict(file_path, toDoList)

        dispatcher.utter_message(text=f"Removed activity {activity} with deadline {removed_activity}")
        return [AllSlotsReset()]