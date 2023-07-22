import speech_recognition as sr
import pyttsx3
import os
from google.cloud import speech
class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init('sapi5')

    def speak(self, text):
        self.speaker.say(text)
        self.speaker.runAndWait()

    def listen(self):
        with sr.Microphone(device_index=1) as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            text_return = ''.join(text)
            print("You said:", text)
            return text_return.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand. repeat it please")
            return ""
        except sr.RequestError:
            print("There was an error while send request.")
            return ""

    def run(self):
        self.speak("Hello! I am Cyber's assistant. How can i help you")
        while True:
            command = self.listen()

            if "hello" in command:
                self.speak("Hello there!")
            elif "what is your name" in command:
                self.speak("I am your voice assistant.")
            elif "exit" in command or "goodbye" in command:
                self.speak("Goodbye!")
                break
            elif "how are you" in command:
                print("Fine Thanks. you")
            elif "command prompt" in command:
                os.system("cmd")
                
            else:
                self.speak("Sorry, I can't perform that command.")

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
