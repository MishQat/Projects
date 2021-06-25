from tkinter import BooleanVar, StringVar, font
from tkinter.ttk import *
import tkinter
import datetime
time = datetime.datetime.now()
time_now = time.strftime("%d/%b/%Y. time: %H:%M")
day_today = time.strftime("%A")
date_today = time.strftime("%d")

window = tkinter.Tk()#makes the window or the thing that will be displayed 
window.configure(bg="Yellow")

window.title("Notes")#title, like "Fortnite" basically a name of the window
while True:
    lable = tkinter.Label(window,text="welcome to notes what shall we write today",font=("Arial Italic",10),bg='white', fg='green')#important.basically what will be printed on the window, fonts and all types of things can be given


    lable.grid(column=0,row=0)#where the writing will be placed basically x,y
    user_value=StringVar()
    txt=tkinter.Entry(window,textvariable=user_value,width=100)#input from user like input("blah")
    txt.configure(bg="white",font="Arial",fg="black")
    txt.grid(column=1,row=0)#where the entry box will be 

    def clicked():#function that will do somethng when a button is pressed
        f = open("records.txt","a")# opens a new file for saving the inputs
        f.write(f"Entry of {time_now}\n{txt.get()}\n")# write the entry time and input
        f.close#closes the file and saves it
        f=open ("records.txt","r")#opens the file again but this time only reads it
        lable_read=tkinter.Label(window,text=f.read(),font=("Arial Italic",10),bg='white', fg='green')#creates a new label and prints the file in the GUI
        lable_read.grid(row=1)
       
    bt= tkinter.Button(window, text="Confirm entry",bg="yellow", fg="cyan",command=clicked)#Button which we wrote the function for earlier, the colour and stuff can be changed. dose something when clicked(command=clicked)
    bt.grid(column=0,row=2)
    window.mainloop()#loops through it all makes the program work most important
