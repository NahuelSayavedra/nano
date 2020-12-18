 # import all library 
import speech_recognition as sr # microfone
import pyttsx3 #speaker
import pywhatkit #google control
import wikipedia #wikipedia control
import datetime

listener = sr.Recognizer() # start a microfone
engine = pyttsx3.init() #start a speaker 
engine.setProperty('rate', 125)
wikipedia.set_lang("es") #configure a wikipedia in spanish

def delted(string,delete):
	return string.replace(delete,"") #remove the part of the string that is same with delete

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        inpVoice = input("que quieres hacer? ")
        #voice = listener.listen(inpVoice)
        #command = listener.recognize_google(voice)
        command = inpVoice.lower()
        ok = "nano" in command #verificate a command for nano
        print(ok)
        if ok == True:
            command = delted(command, "nano ") #delete nano for de command
            return command
        else:
            return False
    except:
        pass
    
def nano():
    command = listen_command()  #get the command
    commands = {1: "nada", 2: "wikipedia", 3: "reproducir",  4: "whatsapp"} #diccionary whit the commands
    print(commands)
    key = 1 #key of diccionary
    if command != False: #verificate command isn´t False
        for key in commands:
            print(key)
            if commands[key] in command: #verificate command exist
                print("comando resivido") #alert who the command is verificate
                return key, command
            else:
                key = key + 1 
        return 0, "None"

def run_nano():
    command_exist, command = nano() #resave the command
    print(command_exist)
    print(command)
    if command_exist != False: #verificate command exist
        if command_exist == 1:
            pass 
        elif command_exist == 2:
            cuestion = delted(command, "wikipedia") #get the cuestion for wikipedia
            data = wikipedia.summary("{0}".format(cuestion), sentences = 1) #the firs line of wikipedia
            talk(data)
        elif command_exist == 3:
            play = delted(command, "reproducir")
            talk("reproduciendo {0}".format(play))
            pywhatkit.playonyt(play)
        elif command_exist == 4:
            number = input("¿A quien? ").__str__
            message = input("¿Cual es el mensaje? ")
            hour = datetime.datetime.now().strftime('%I')
            minnute = datetime.datetime.now().strftime('%M')
            pywhatkit.sendwhatmsg(number, message, hour, minnute )
    else:
        pass


while True:
    run_nano()