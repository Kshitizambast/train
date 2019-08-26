# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:10:56 2019

@author: Kshitiz
"""
from __future__ import print_function
import speech_recognition as sr
import pyttsx3
import os
import sys
import re
import webbrowser
import sphinx
import smtplib
import requests
import subprocess
from pyowm import OWM
import urllib
import urllib.request
import json
import vlc
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
from time import strftime



def buddyResponse(audio):
      print(audio)
      engine = pyttsx3.init()
      for line in audio.splitlines():
            engine.say(audio)
            engine.setProperty('rate',100)
            engine.setProperty('volume', 0.9)
            engine.runAndWait()

def myCommand():
      r = sr.Recognizer()
      with sr.Microphone() as source:
            print('Say Something....')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
      try:
            command = r.recognize_google(audio).lower()
            print('You Said: ' + command + '\n')
      except sr.UnknownValueError:
            print('.....')
            command = myCommand();
      return command
         
def assistant(command):
      if 'open reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
            url = 'https://www.reddit.com/'
            if reg_ex:
                  subreddit = reg_ex.group(1)
                  url = url + 'r/' + subreddit
                  webbrowser.open(url)
                  buddyResponse('Reddit is here bro!')
                  
      #time
      if 'time' in command:
            import datetime
            now = datetime.datetime.now()
            buddyResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))
      
      elif 'launch' in  command:
            reg_ex  = re.search('launch (.*)', command)
            if reg_ex:
                  appname = reg_ex.group(1)
                  appname1 = appname+'.exe'
                  os.startfile(appname1)
                  buddyResponse('I have opened it, sir')
                  
                  
      elif 'open folder' in command:
             reg_ex  = re.search('open folder (.*)', command)
             if reg_ex:
                   folder = reg_ex.group(1)
                   os.startfile(folder)
                   buddyResponse('Okay Sir, Here is the '+ folder)
                   
                   #go inside the file
                   buddyResponse('Which file you want to open sir')
                   file1 = myCommand()
                   file = file1+'.mp4'
                   buddyResponse('Openning '+ file1)
                   player = vlc.MediaPlayer(str(os.path.join(folder, file)))
                   player.play()
                   
                   #pause it
                   command_player = myCommand()
                   if 'pause' or 'continue' in command_player:
                         player.pause()
                   elif 'stop' in command_player:
                         player.stop()
                         
                   
                   
      elif 'open' in command:
            reg_ex = re.search('open (.+)', command)
            if reg_ex:
                  domain = reg_ex.group(1)
                  print(domain)
                  url = 'https://www.' + domain +'.com'
                  webbrowser.open(url)
                  buddyResponse('I have opened '+domain+' , sir')
            else:
                  pass
                  
            
                        
      elif 'hello' in command:    
            day_time = int(strftime('%H'))
            if day_time < 12:
                  buddyResponse('Hello Sir. Good morning')
            elif 12 <= day_time < 18:
                  buddyResponse('Hello Sir. Good afternoon')
            else:
                  buddyResponse('Hello Sir. Good evening')
                  
      #to terminate the program
      elif 'shutdown' or 'shut down' in command:
            buddyResponse('Bye bye Sir. Have a nice day')
            sys.exit()
            

            


            
buddyResponse('Hi, I am buddy and I am your learning partner. Tell Me What Can  I do for you?')
      
while True:
      assistant(myCommand())


















       
            

