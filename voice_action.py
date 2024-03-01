from typing import List, Dict, Any, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import Text
from voiceInterface import VoiceIntegration

class VoiceAction(Action):

    def name(self) -> Text:
        return "voice_action"

    async def run(self, dispatcher: CollectingDispatcher,
                   tracker: Tracker,
                   domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        voice_integration = VoiceIntegration()
        print("Voice action")
        # Get voice input
        user_input = voice_integration.get_voice_input()

        # Process user input and generate response
        response = "Your response goes here"

        # Output response using voice
        voice_integration.output_voice(response)

        return []