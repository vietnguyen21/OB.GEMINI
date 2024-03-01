import pyttsx4

# Create an engine instance
engine = pyttsx4.init('sapi5')

# Say something
engine.say("Hello")
engine.runAndWait()