from rasa_sdk import Action
from rasa_sdk.events import SlotSet

import speech_recognition as sr
import requests
import pyttsx3
import time

class VoiceIntegrationAction(Action):
    def name(self):
        return "action_voice_integration"

    def run(self, dispatcher, tracker, domain):
        self.voice_output("Hello! I am your voice-enabled chatbot. How can I assist you today?")

        while True:
            user_input = self.voice_input()

            if user_input:
                print("User: " + user_input)
                dispatcher.utter_message("You said: " + user_input)
                if self.should_end_conversation(user_input):
                    break  # Exit the loop if the user wants to end the conversation
                else:
                    message = self.text_input_to_message(user_input)
                    response = self.send_message(message)
                    self.voice_output(response)
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
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                return None

    def text_input_to_message(self, text):
        message = {"recipient": "bot", "text": text}
        return message

    def send_message(self, message):
        url = "http://localhost:5055/webhooks/rest/webhook"
        response = requests.post(url, json=message)
        response_text = response.json()[0]["text"]
        return response_text

    def voice_output(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def should_end_conversation(self, user_input):
        if "goodbye" in user_input.lower():
            return True
        else:
            return False
        
# def run_voice_integration_action():
#     # Initialize the voice integration action
#     voice_integration = VoiceIntegrationAction()

#     dispatcher = None
#     tracker = None
#     domain = None

#     # Run the voice integration action
#     voice_integration.run(dispatcher, tracker, domain)

# if __name__ == "__main__":
#     run_voice_integration_action()
    def is_valid_audio_input(self, audio):
        if audio is None:
            return False
        if len(audio) < 10:
            return False
        return True