#This file is named voice_integration.py
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import speech_recognition as sr
import pyttsx3

class VoiceIntegrationAction(Action):
    def name(self):
        return "action_voice_integration"
    
    def run(self, dispatcher, tracker, domain):
        print("Action: VoiceIntegrationAction")
        self.voice_output("Hello! I am your voice-enabled chatbot. How can I assist you today?")

        while True:
            user_input = self.voice_input()

            if user_input:
                print("User: " + user_input)
                dispatcher.utter_message("You said: " + user_input)
                if self.should_end_conversation(user_input):
                    break  # Exit the loop if the user wants to end the conversation
            else:
                dispatcher.utter_message("Sorry, I couldn't understand. Can you please repeat that?")

    def voice_input(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=3)
                text = recognizer.recognize_google(audio)
                print("You said: " + text)
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                return None
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                return None

    def voice_output(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def should_end_conversation(self, user_input):
        # Add logic to determine if the user wants to end the conversation
        return "goodbye" in user_input.lower()
