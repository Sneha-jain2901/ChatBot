# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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
from voice_interface import voice_input, voice_output

class VoiceInput(Action):
    def name(self):
        return "voice_input"

    def run(self, dispatcher, tracker, domain):
        text = voice_input()
        if text:
            dispatcher.utter_message(text=text)
        return []
    
class VoiceOutput(Action):
    def name(self):
        return "voice_output"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message['text']
        voice_output(text)
        return []