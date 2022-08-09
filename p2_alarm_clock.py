# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:43:30 2022

@author: Harkiran.Singh
"""

from datetime import datetime                                                      #python has inbuilt datatime module
from playsound import playsound                                                    #playsound module to play the alarm ringtone
alarm_time = input('Enter the time of alarm to be set:HH:MM:SS:Period(AM/PM)\n')   #user inputs the alarm time to be set
alarm_hour = alarm_time[0:2]                                                       #slice the alarm_time string 
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11]
while True:                                                                        #once the progrem is run until alarm time, program should continuosly execute
    now = datetime.now()                                                           #now() method from datetime gives the current time
    current_hour = now.strftime("%I")                                              #strftime method to convert datetim to string and parse hour
    current_minute = now.strftime("%M")        
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period == current_period):                                            #compare alarm time to current time
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_seconds == current_seconds):                              #if matched
                    print('Wake Up!')                                                  
                    playsound(r'C:\Users\harkiran.singh\Downloads\windows_longhorn_shut.mp3') #ring alarm
                    break                                                          #break from the loop
    