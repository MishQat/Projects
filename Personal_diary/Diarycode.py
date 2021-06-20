import datetime
from os import write
import sys
time = datetime.datetime.now()
time_now = time.strftime("%d/%b/%Y. time: %H:%M")
day_today = time.strftime("%A")
date_today = time.strftime("%d")
month_today = time.strftime("%B")
year_today = time.strftime("%Y")#gets all data for time and date
try:
    user_input_diary = input(f"Today is {day_today}, {date_today}th of {month_today} {year_today} \nWhat do you want to write today?... ")#asks user

    f = open("Diary101.txt","a")
    f.write(f"\nEntry of {time_now}\n{user_input_diary}")#takes entry
    f.close
    user_input = input("New entry added succesfully, do you want to see your whole diary.y/n?... ")
    f = open("Diary101.txt","r")
except:
    print("Data entry unsuccesful, try again.")
    user_input = input("Do you wish to see your whole diary.y/n?... ")
    f = open("Diary101.txt","r")
if user_input == "y":
    print(f.read())#reads out the whole file if user wants to
else:
    sys.exit
