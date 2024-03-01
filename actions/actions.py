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

# from .voice_integration import voice_input, voice_output
# from rasa_sdk import Action
# # In actions.py
# import voice_integration
# print(voice_integration)  # Print the module to check if it's loaded

# class VoiceInput(Action):
#     def name(self):
#         return "voice_input"

#     def run(self, dispatcher, tracker, domain):
#         text = voice_input()
#         if text:
#             dispatcher.utter_message(text=text)
#         return []
    
# class VoiceOutput(Action):
#     def name(self):
#         return "voice_output"

#     def run(self, dispatcher, tracker, domain):
#         text = tracker.latest_message['text']
#         voice_output(text)
#         return []

# In actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

from .voice_integration import VoiceIntegrationAction

class VoiceEnabledChatbotAction(VoiceIntegrationAction):
    def name(self):
        return "voice_enabled_chatbot"

    def run(self, dispatcher, tracker, domain):
        super().run(dispatcher, tracker, domain)
        return []

class VoiceInputWrapper(Action):
    def name(self):
        return "voice_input"

    def run(self, dispatcher, tracker, domain):
        voice_input = VoiceIntegrationAction().voice_input()
        if voice_input is not None:
            dispatcher.utter_message(text=voice_input)
        return []

class VoiceOutputWrapper(Action):
    def name(self):
        return "voice_output"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message.get('text', '')
        VoiceIntegrationAction().voice_output(text)
        return []