import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import pyjokes
import datetime as dt
joke=pyjokes.get_joke()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def num(command):
        operation=command.split(" ")
        numbers=len(operation)
        numbers-=3
        num1=int(operation[numbers])
        numbers+=2
        num2=int(operation[numbers])
        return num1 ,num2
def dateTime(command):
    if "time" in command:
        time=dt.datetime.now().time().strftime("%H %m %p")
        speak(time) 
    elif "date" in command:
        date=dt.datetime.now().date().strftime("%d %B %Y")
        speak(date)

def processCommand(command):
    if "open google" in command:
        webbrowser.open("https://google.com")

    elif "open youtube" in  command:
        webbrowser.open("https://youtube.com")
    
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com") 
    
    elif "open insta" in command :
        webbrowser.open("https://instagram.com")    
    
    elif command.startswith("play"):
        song=command.split(" ")[1]
        songList=musiclibrary.music
        if song in songList.keys():
            webbrowser.open(songList.get(song))
        else :
            print("song not in the provided list....")
    elif command.startswith("tell"):
        speak(joke)
        speak("ha ha ha")
    elif "calculate" or "what is " in command :
        number1,number2=num(command)
        if "plus" in command:
            # newCommand=command.replace("plus","+")  
            # speak(f"the sum is {num1 + num2}")
            sum=number1+number2
            speak(f"The sum of {number1} and {number2} is {sum}")
            
        elif "minus" in command:
            difference=number1 - number2
            speak(f"The difference of {number1} and {number2} is {difference}")
            
        elif "multiply" in command:
            multiply=number1*number2
            speak(f"The multiply of {number1} and {number2} is {multiply}")
            
        elif "divided" in command:
            if number2==0:
                speak("second number cannot be negative...it will give infinity")
                
            else:
                divide=int(number1/number2)
                speak(f"The division of {number1} by {number2} is {divide}")
                
        elif "modulus" in command:
            module=number1%number2
            speak(f"The modulus of {number1} by {number2} is {module}")
            
        elif "power" in command:
            power=number1**number2
            speak(f"{number1} raised to the power {number2} is {power}")  
        elif "exit" in command:
            print("GoodBye...")     
    if "time" in command :

        time=dt.datetime.now().time().strftime("%H  %M  %p")
        speak(f"it is {time}")
    elif "date" in command:
        date=dt.datetime.now().date().strftime("%d %B %Y")
        speak(f"it is {date}")
    elif "day" in command:
        now=dt.datetime.now()
        day=now.strftime("%A")
        speak(f"today is {day}")
    elif "month" in command:
       month= dt.datetime.now().strftime("%B")
       speak(f"This is {month}")
    elif "year" in command:
        year=dt.datetime.now().strftime("%Y")
        speak(f"This is {year}")
    else :
        print("did not understand....")

print("wellcome....")
speak("Initializing Jarvis")
while True :
    r=sr.Recognizer()
    print("recognizing....")
    try :
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening....")
            audio=r.listen(source,timeout=2,phrase_time_limit=3)
            word=r.recognize_google(audio).lower()    
        if word == "jarvis" :
                speak("Ya")
                print("Jarvis Active...")
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio=r.listen(source,timeout=2,phrase_time_limit=3)
                    command=r.recognize_google(audio).lower()
                    if command.startswith("exit"):
                        break
                    else :
                        processCommand(command)

    except Exception as e :
        print(e)


