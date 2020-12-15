from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.events import UserUtteranceReverted, Restarted, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class TicketForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "ticket_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        # print ("=============\n",tracker.latest_message)
        return ["date_time","start","end"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
    
        return {
            "date_time": self.from_entity(entity="date_time"),
            
            "start": [self.from_entity(entity="start",intent=["request_ticket","inform"]),
                       self.from_text(intent=["inform_single"]),],
                      # self.from_entity(entity="start",intent=["inform_single"]),
                      # self.from_entity(entity="end",intent=["inform_single"])],
            
            "end": [self.from_entity(entity="end",intent=["request_ticket","inform"]),
                     self.from_text(intent=["inform_single"]),],
                      # self.from_entity(entity="end",intent=["inform_single"]),
                      # self.from_entity(entity="start",intent=["inform_single"])],
        }
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        date_time = tracker.get_slot('date_time')
        start = tracker.get_slot('start')
        end = tracker.get_slot('end')
        print ("=========tracker==========\n",tracker.events)
        dispatcher.utter_message("你想查询{}从{}出发，前往{}的火车信息".format(date_time,start,end))
        return []

class SetStart(Action):
    def name(self):
        return "set_start"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("start", "乌鲁木齐")]

class SetEnd(Action):
    def name(self):
        return "set_end"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("end", "长春")]