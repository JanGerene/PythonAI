import pyttsx3
def change_voice(engine:pyttsx3, id):
    for voice in engine.getProperty('voices'):
        if id == voice.id: 
            engine.setProperty("voice", voice.id)
            return True
    raise RuntimeError("Language '{}' not found".format(id))

engine = pyttsx3.init()
volume = engine.getProperty('volume')
print(volume)
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate',175)
change_voice(engine, "english")
engine.say("hello world!")
engine.say('my current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()    