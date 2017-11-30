# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello this is me talking")
# engine.setProperty('rate',120)  #120 words per minute
# # engine.setProperty('volume',0.9) 
# engine.runAndWait()

import pyttsx3
engine= pyttsx3.init()
engine.setProperty('rate',120)  #120 words per minute
engine.setProperty('volume',0.9) 
voices=engine.getProperty('voices')
for voice in voices:
    print ("Using voice:", repr(voice))
    engine.setProperty('voice',voice.id)
    engine.say("Hello Hello Hello")
engine.runAndWait()