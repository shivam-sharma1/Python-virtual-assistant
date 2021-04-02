import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import time
import wolframalpha # to calculate strings into formula 
from selenium import webdriver
import pyttsx3
warnings.filterwarnings('ignore')
# Record Audio
def recordAudio():
    r = sr.Recognizer()
    # open mic
    with sr.Microphone() as source:
        print('Say Something! Shivam')
        audio = r.listen(source)
    #use google speech recognisation
    data=' '
    try:
        data = r.recognize_google(audio)
        print('Shivam Said: '+data)
    except sr.UnknownValueError:
        print('Sorry Shivam! could not understand, Please Repeat again')
    except sr.RequestError as e:
        print('Request results from google speech recognization'+e)
    return data
# Get the assistant response
def assistantResponse(text):
    print(text)
    #convert txt to speech
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# wake word
def WakeWord(text):
    WAKE_WORDS = ['hey chintu','ok chintu','Hello chintu']
    text=text.lower() #list words are in lower case...easy to compare
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #if wake word isn't found
    return False
#current date
def getDate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']
    ordinalNumbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
    return 'Today is '+weekday+' '+month_names[monthNum - 1]+' the '+ordinalNumbers[dayNum - 1]+'. '
def greeting(text):
     GREETING_INPUTS=['hi','hey','hello','greetings','wassup']
     GREETING_RESPONSES=['hey!how are you','whats good','hey there','hello']
     for word in text.split():
         if word.lower() in GREETING_INPUTS:
             return random.choice(GREETING_RESPONSES) + '.'
     return ''
def getThing(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i+3<=len(wordList)-1 and wordList[i].lower() == 'what' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]
def getPerson(text):
    wordList = text.split()
    for i in range(0, len(wordList)):
        if i+3<=len(wordList)-1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+ wordList[i+3]


def search_web(text): 

	driver = webdriver.Chrome('C:/Users/Shivam/Downloads/chromedriver.exe') 
	driver.implicitly_wait(1) 
	driver.maximize_window() 

	if 'youtube' in text.lower(): 

		assistantResponse("Opening youtube") 
		indx = text.lower().split().index('youtube') 
		query = text.split()[indx + 1:] 
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
		return

	elif 'wikipedia' in text.lower(): 

		assistant_speaks("Opening Wikipedia") 
		indx = text.lower().split().index('wikipedia') 
		query = text.split()[indx + 1:] 
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
		return

	else: 

		if 'google' in text: 

			indx = text.lower().split().index('google') 
			query = text.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q=" + '+'.join(query)) 

		elif 'search' in text: 

			indx = text.lower().split().index('search') 
			query = text.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q=" + '+'.join(query)) 

		else: 

			driver.get("https://www.google.com/search?q=" + '+'.join(text.split())) 

		return


# function used to open application 
# present inside the system. 
def open_application(text): 

	if "chrome" in text: 
		assistantResponse("Google Chrome") 
		os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"') 
		return

	elif "brave browser" in text or "brave" in text: 
		assistantResponse("Opening Brave") 
		os.startfile('"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"') 
		return
    

	else: 

		assistantResponse("Application not available") 
		return





while True:
    #record audio
    text = recordAudio()
    response = ''
    #check wake word
    if(WakeWord(text)==True):
        response=response + greeting(text)
        assistantResponse(response)
        if('date' in text):
            get_date = getDate()
            response = response + ' '+get_date
            assistantResponse(response)
        #check for time
        elif('time' in text):
            now = datetime.datetime.now()
            meridien=''
            if now.hour >=12:
                meridien ='p.m'
                hour = now.hour - 12
            else:
                meridien = 'a.m.'
                hour = now.hour
            if now.minute<10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)
            response = response +' '+'It is '+str(hour)+ ':'+minute+ ' '+meridien+' .'
            assistantResponse(response)
        # check for who is
        elif('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response +' '+wiki
            assistantResponse(response)
        elif('what is' in text):
            person = getThing(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response +' '+wiki
            assistantResponse(response)
        elif "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistantResponse("Ok bye, Shivam") 
            break
        

        elif 'search' in text or 'play' in text: 
            # a basic web crawler using selenium 
            search_web(text) 


        elif "who are you" in text or "define yourself" in text: 
            speak = '''Hello, I am Chintu. The personal Assistant. 
            Memory 1 terabyte. speed 1.8 Gigahertz.'''
            assistantResponse(speak) 
          

        elif "who made you" in text or "who created you" in text: 
            speak = "I have been created by Shivam Sharma."
            assistantResponse(speak) 
            

        elif "calculate" in text.lower(): 
                
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id) 

            indx = text.lower().split().index('calculate') 
            query = text.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistantResponse("The answer is " + answer) 
            

        elif 'open' in text: 
                
            # another function to open 
            # different application availaible 
            open_application(text.lower()) 
            

        else: 

            assistantResponse("I can search the web for you, Do you want to continue?") 
            ans = recordAudio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                    search_web(input) 
            

        
        
            


