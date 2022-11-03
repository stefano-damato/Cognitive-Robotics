from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import ast

def importDict(filepath):
    with open(filepath, 'r') as f:
        str = f.read()
    convertedDict=ast.literal_eval(str)
    return convertedDict
def exportDict(filepath,dict):
    with open(filepath, 'w') as f:
        f.write(str(dict))


FILENAME="toDoList.txt"
class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        activity = tracker.get_slot("activity")
        deadline = tracker.get_slot("deadline")

        print("\nActivity:",activity)
        print("Deadline:",deadline)
        toDoList=importDict(FILENAME)
        attr=list() #qui poi mettimo il campo deadline e reminder
        toDoList[Activity]=attr.append(deadline)

        dispatcher.utter_message(text=f"Added activity {activity} at {deadline}")
        return "????"