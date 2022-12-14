from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset
from datetime import datetime as dt
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
        deadline = tracker.get_slot("time")
        time_object = dt.strptime(deadline, "%Y-%m-%dT%H:%M:%S.%f%z")
        deadline=time_object.strftime("%m/%d/%Y, %H:%M")
        print(deadline)
        reminder = tracker.get_slot("reminder")
        if (reminder!=True and reminder!=False):
            reminder=True
        category = tracker.get_slot("category")
        PERSON = tracker.get_slot("PERSON")
        if(isinstance(PERSON,list)):
            PERSON=PERSON[0]

        PERSON=PERSON.capitalize()
        file_path = PERSON + FILENAME
        
        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            toDoList={}
        #attr=list() #qui poi mettimo il campo deadline e reminder
        toDoList[activity]=list()
        toDoList[activity].append(category)
        toDoList[activity].append(deadline)
        toDoList[activity].append(reminder)

        exportDict(file_path, toDoList)

        if(deadline=="12/31/2050, 23:59"):
            dispatcher.utter_message(text=f"Added activity {activity}, {category} for {PERSON}")
        else:
            dispatcher.utter_message(text=f"Added activity {activity}, {category} at {deadline} for {PERSON} with reminder:{reminder}")
        
        return [AllSlotsReset(), SlotSet("PERSON", PERSON)]

class ActionDisplaySubmit(Action):

    def name(self) -> Text:
        return "action_display_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        PERSON = tracker.get_slot("PERSON")
        if(isinstance(PERSON,list)):
            PERSON=PERSON[0]

        if(PERSON is None):
            dispatcher.utter_message(text=f"Please enter your name")
            return [AllSlotsReset()]

        file_path = PERSON + FILENAME

        if(os.path.exists(file_path)):
            toDoList=importDict(file_path)
        else:
            toDoList={}

        dispatcher.utter_message(text=f"{PERSON}'s ToDo List:\n")

        i = 1

        for key,value in toDoList.items():
            if value[1]=="12/31/2050, 23:59":
                dispatcher.utter_message(text=f"[{i}] Activity: {key}, category: {value[0]}\n")
            else:
                dispatcher.utter_message(text=f"[{i}] Activity: {key}, category: {value[0]}, deadline: {value[1]}, reminder: {value[2]}\n")
            i+=1

        return [AllSlotsReset(), SlotSet("PERSON", PERSON)]

class ActionRemoveSubmit(Action):

    def name(self) -> Text:
        return "action_remove_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity = tracker.get_slot("activity")
        PERSON = tracker.get_slot("PERSON")
        if(isinstance(PERSON,list)):
            PERSON=PERSON[0]

        file_path = PERSON + FILENAME

        print("\nActivity:",activity)

        if(not os.path.exists(file_path)):
            dispatcher.utter_message(text=f"There are no activities")
            return [AllSlotsReset(), SlotSet("PERSON", PERSON)]
        else:
            toDoList=importDict(file_path)
            if(activity not in toDoList):
                dispatcher.utter_message(text=f"There is no such activity")
                return [AllSlotsReset(), SlotSet("PERSON", PERSON)]
            else:
                removed_activity=toDoList.pop(activity)
        exportDict(file_path, toDoList)

        if(deadline=="12/31/2050, 23:59"):
            dispatcher.utter_message(text=f"Removed activity {activity}, {category} for {PERSON}")
        else:
            dispatcher.utter_message(text=f"Removed activity {activity}, {category} at {deadline} for {PERSON}")
        
        return [AllSlotsReset(), SlotSet("PERSON", PERSON)]

class ActionModifySubmit(Action):

    def name(self) -> Text:
        return "action_modify_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity = tracker.get_slot("activity")
        PERSON = tracker.get_slot("PERSON")
        if(isinstance(PERSON,list)):
            PERSON=PERSON[0]
        deadline = tracker.get_slot("time")
        time_object = dt.strptime(deadline, "%Y-%m-%dT%H:%M:%S.%f%z")
        deadline=time_object.strftime("%m/%d/%Y, %H:%M:%S")
        reminder = tracker.get_slot("reminder")
        category = tracker.get_slot("category")

        file_path = PERSON + FILENAME

        print("\nActivity:",activity)

        if(not os.path.exists(file_path)):
            dispatcher.utter_message(text=f"There are no activities")
            return [AllSlotsReset(), SlotSet("PERSON", PERSON)]
        else:
            toDoList=importDict(file_path)
            if(activity not in toDoList):
                dispatcher.utter_message(text=f"There is no such activity")
                return [AllSlotsReset(), SlotSet("PERSON", PERSON)]
            else:
                toDoList[activity][0]=category
                toDoList[activity][1]=deadline
                toDoList[activity][2]=reminder
        exportDict(file_path, toDoList)

        if(deadline=="12/31/2050, 23:59"):
            dispatcher.utter_message(text=f"Modified activity {activity}, {category} for {PERSON}")
        else:
            dispatcher.utter_message(text=f"Modified activity {activity}, {category} at {deadline} for {PERSON}")
        
        return [AllSlotsReset(), SlotSet("PERSON", PERSON)]

class ActionPresentation(Action):

    def name(self) -> Text:
        return "action_presentation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        PERSON = tracker.get_slot("PERSON")
        if(isinstance(PERSON,list)):
            PERSON=PERSON[0]
        PERSON=PERSON.capitalize()
        dispatcher.utter_message(text=f"Hello {PERSON}! How can I help you today?")
        
        return []