import speech_recognition as sr
import pyttsx3

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source ,timeout=5, phrase_time_limits=5)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def voice_output(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    voice_output("Hello! I am your voice-enabled chatbot. How can I assist you today?")

    while True:
        user_input = voice_input()

        if user_input:
            print("User: " + user_input)
            voice_output("You said: " + user_input)
        else:
            voice_output("Sorry, I couldn't understand. Can you please repeat that?")