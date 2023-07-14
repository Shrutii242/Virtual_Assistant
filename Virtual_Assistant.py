import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import pywhatkit
import os
import smtplib
from playsound import playsound
import pyjokes

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz   

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")    

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  
    
    speak("Please tell me how may I help you")  

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('cm.b.48jitesh.shringare@gmail.com', 'shringare1205')
    server.sendmail('cm.b.48jitesh.shringare@gmail.com', to, content)
    server.close()
    
def btn1():
    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()
            if "go to sleep" in query:
                speak("ok sir recall me anytime!!")
            elif "hello" in query:
                speak("Hello sir, how are you ?")
            elif "i am fine" in query:
                        speak("that's great, sir")
            elif "how are you" in query:
                        speak("Perfect, sir")
            elif "thank you" in query:
                        speak("you are welcome, sir")         
        
            elif "google" in query:
                searchGoogle(query)
            elif "youtube" in query:
                searchYoutube(query)
            elif "wikipedia" in query:
                searchWikipedia(query)

            elif 'play' in query:
                song = query.replace('play', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)                   
                # playsound('C:\\Users\\shrut\\OneDrive\\Desktop\\Python Course\\play.mp3')
            
            elif 'file manager' in query:
                 path = "C:\\Users\\shrut\\OneDrive\\Desktop"
                 os.startfile(path)

            elif 'the time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif 'what is' in query:
                 meaning = query.replace('what is', '')
                 info = wikipedia.summary(meaning, 1)
                 print(info)
                 speak(info)

            elif 'email to lalit' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "cm.b.22lalit.patil@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")   
            elif "set an alarm" in query:
                print("input time example:- 10 and 10 and 10")
                speak("Set the time")
                a = input("Please tell the time :- ")
                alarm(a)
                speak("Done,sir") 

            elif 'joke' in query:
                 speak(pyjokes.get_joke())
    
if __name__ == '__main__':
    root = Tk()
    
    img =Image.open("bgimg.jpg")
    bg = ImageTk.PhotoImage(img)

    root.maxsize(width="500", height="400")
    root.minsize(width="500", height="400")
    root.title("VIRTUAL ASSISTANT")
    root.iconbitmap("Image3.ico")

    lab = Label(root, image=bg)
    lab.place(x = 0,y = 0)

    frame4 = Frame(root)
    frame4.pack()
    frame4.place(anchor = 'ne', relx=1 , rely=0)

    date = datetime.now() 
    label1 = Label(frame4, text = f"{date :%A, %B %d, %Y}" , font = "Calibari, 10")
    label1.pack()

    time = datetime.now()
    label2 = Label(frame4, text = f"{time :%H : %M %p}" , font = "Calibari, 10" )
    label2.pack()

    frame = Frame(root, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    img = ImageTk.PhotoImage(Image.open("Image.jpg"))
    label = Label(frame, image = img)
    label.pack()
    
    frame2= Frame(root)
    frame2.pack(side=BOTTOM)
    btn1 = Button(frame2, text="Tap to Speak", command=btn1).pack(ipadx=2, ipady=2)

    frame3= Frame(root)
    frame3.pack(side=BOTTOM)
    btn2 = Button(frame3, text="Cancel", command=root.destroy).pack(ipadx=2, ipady=2)

    root.mainloop()
