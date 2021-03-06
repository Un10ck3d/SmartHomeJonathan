#Config
lang = 'en'
dirr = 'speech/'

#Imports
try:
    from gtts import gTTS
    from hashlib import md5
    from os.path import exists
    from os import mkdir, environ
    from time import sleep
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame.mixer import init, music
    from pygame import mixer
    #from cores.apiai import FifteenAPI
    #tts_api = FifteenAPI(show_debug=True)
    init()
except Exception as es:
    print("""You have to install the modules: pygame and gtts. Use: 'pip3 install pygame' and 'pip3 install gtts' to install the modules""")
    print(es)
    quit()

#Make dir if not exists
if not exists(dirr):
    mkdir(dirr)

#Say function
def say(text):
    while music.get_busy() == True:
        sleep(0.1)
    print(text)
    if not text or ')' in text or '(' in text:
        return
    #Convert text to hash for file name
    filename = md5(text.encode()).hexdigest()
    #Make path
    path = f"{dirr}{filename}"
    newpath = path + '.wav'
    #Check if file allready exists
    if not exists(newpath):
        #If not generate the file
        speak = gTTS(text=text, lang=lang, slow=False)
        speak.save(path)
        #tts_api.save_to_file("GLaDOS", text, path)
    #Play the sound file
    mixer.Sound(newpath).play()
    #music.load(newpath)
    #music.play()

#Say function
def ask(text):
    while music.get_busy() == True:
        sleep(0.1)
    if not text or ')' in text or '(' in text:
        return
    #Convert text to hash for file name
    filename = md5(text.encode()).hexdigest()
    #Make path
    path = f"{dirr}{filename}.mp3"
    #Check if file allready exists
    if not exists(path):
        #If not generate the file
        speak = gTTS(text=text, lang=lang, slow=False)
        speak.save(path)
        #tts_api.save_to_file("GLaDOS", text, path)
    #Play the sound file
    music.load(path)
    music.play()
    test = input(text).lower()
    return test

#Generate sound file function
def gen(text):
    if not text or ')' in text or '(' in text:
        return
    #Convert text to hash for file name
    filename = md5(text.encode()).hexdigest()
    #Make path
    path = f"{dirr}{filename}.mp3"
    #Check if file allready exists
    if not exists(path):
        #If not generate the file
        speak = gTTS(text=text, lang=lang, slow=False)
        speak.save(path)