import pyttsx3      # pyttsx3 is a Python-text-to-speak-x-3 module
import speech_recognition as sr
import webbrowser as wb
import wikipedia

import datetime
import calendar
import imdb

from Agg_percentage import *
from Random_pass import *
from phone_track import *
from music_play import *
# win_amd64.whl
engine = pyttsx3.init()     # Assign variable to module
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[0].id)
newVoiceRate = 175
engine.setProperty('rate', newVoiceRate)

# name of AI
ai_name = "ELECTRO"
# ai_name = "andrew"
# Function to convert the text to speech
print("\033[96m {}\033[00m".format("FINAL YEAR PROJECT"))
print("\033[96m {}\033[00m".format(f"{ai_name}, The Virtual Desktop Assistant"))
print("\033[99m {}\033[00m".format("Created By:"))

print(" \033[94m {}\033[00m " .format('ZEESHAN'), "\033[94m {}\033[00m" .format('AFTAB'))
print(" \033[94m {}\033[00m " .format('ANKUSH'), "\033[94m {}\033[00m" .format('ABHIJEET'))


def spk(audio):
    engine.say(audio)
    engine.runAndWait()
# spk("Hello master Z")


def take_cmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        voice_take = r.recognize_google(audio, language='en-in')
        print(voice_take)
    except Exception as e:
        spk("Sorry i can't recognize, please try again")
        return "None"
    return voice_take
# takecmd()

# >>>>>>>>>>>>>>>>>>>>>>>>>>↓↓↓↓↓↓↓↓↓↓Add features here↓↓↓↓↓↓↓↓↓↓<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>↓↓↓↓↓↓↓↓↓↓Add features here↓↓↓↓↓↓↓↓↓↓<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def wishme():
    spk("Welcome back")
    hour = datetime.datetime.now().hour
    if hour <= 12:
        spk("Good Morning master")
    elif hour <= 17:
        spk("Good afternoon master")
    elif hour > 17:
        spk("Good evening master")
    spk(f"This is {ai_name} at your service. How may i help u master....")


def time():
    time_now = datetime.datetime.now().strftime("%I:%M:%S")
    print(f"The current time is {time_now}")
    spk(f"The current time is {time_now}")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    print(f"Today's date is {date}/ {month}/ {year}")
    spk(f"Today's date is {date} / {month} / {year}")


def month():
    spk(f"this month calendar is shown below")
    yy = int(datetime.datetime.now().year)
    mm = int(datetime.datetime.now().month)
    print(calendar.month(yy, mm))


def intro():
    spk(f"Well Hello master. My name is {ai_name} an Artificial Intelligence also know as A I")
    spk("Broad branch of computer science that is focused on a machine's capability to produce rational behavior from external inputs.")
    spk("and my creators are Zeeshan, ankush, Aftab and Abhijeet")


def imdb_movie():
    # creating instance of IMDb
    ia = imdb.IMDb()

    search = ia.get_popular100_movies()
    spk("please enter How many number of movies do u want")
    n = int(input("Enter no.s of movies you want: "))
    spk(f"The top {n} I M D B movies are ")
    print("\033[93m {}\033[00m" .format(f"The top {n} IMDB movies are: "))
    for i in range(n):
        print(f"{i+1}) {search[i]['title']}")
        spk(f"{search[i]['title']}")


def hlp():
    spk("Here are some things that u can ask me about time or give me intro or search anything on wikipedia")

    
# >>>>>>>>>>>>>>>>>>>>>>>>>>↑↑↑↑↑↑↑↑↑↑Add features here↑↑↑↑↑↑↑↑↑↑<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>↑↑↑↑↑↑↑↑↑↑Add features here↑↑↑↑↑↑↑↑↑↑<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# this is the cmd taker to wake a function
# if __name__ == "__main__":
wishme()
while True:
    voice_take = take_cmd().lower()
    # print(voice_take)

    if "time" in voice_take:
        time()

    elif "date" in voice_take:
        date()

    elif "help" in voice_take:
        hlp()

    elif "percentage" in voice_take:
        cgpa()

    elif "intro" in voice_take:
        intro()

    elif "generator" in voice_take:
        runme()

    elif "details" in voice_take:
        track()

    elif "calendar" in voice_take:
        month()

    elif "movies" in voice_take:
        imdb_movie()

    elif "music" in voice_take:
        play()

    elif 'open' in voice_take:
        voice_take = voice_take.replace("open", "")
        voice_take += ".com"
        wb.open(voice_take)
    
    elif 'wikipedia' in voice_take:
        spk('Searching on Wikipedia...')
        voice_take = voice_take.replace("wikipedia", "")
        results = wikipedia.summary(voice_take, sentences=1)
        spk("According to Wikipedia")
        print(results)
        spk(results)

    elif "paper" in voice_take:
        wb.open("https://www.nagpurstudents.org/")
        spk("please select your field")
        engine.runAndWait()
        spk("branch and semester")
        engine.runAndWait()
        spk("after that click on view papers")
        engine.runAndWait()

    elif "turn off" in voice_take:
        spk("Bye bye")
        quit()

# ℤ𝕏