from time import time
from tkinter import *
from tkinter import ttk
import random,array,sys
import tkinter.messagebox as tmsg
import datetime
time = datetime.datetime.now()
time_now = time.strftime("%d/%b/%Y. time: %H:%M")
# TODO:passgenerator from old project
#saves the password in a file with when it was created and under what name
def savepassinfile ():
    
    f = open("pass.txt","a")
    f.write(f"Datetime:{time_now}, Username:{usernameentry.get()}, Password: {password}")
    print(f"Date:{time_now}, Username:{usernameentry.get()}, Password: {password}")
    f.close()
#takes a username to save the pass
def savepass ():
    global usernameentry
    root4=Tk()
    root4.title("Saving")
    Label(root4,text="What shall be the username?").pack()
    usernameentry=Entry(root4)
    usernameentry.pack()
    Button(root4,text="Confirm",command=savepassinfile).pack()
    root4.mainloop()
#loops refresh 
def theloopwhichneverends():
    
    while True:
        createpass()
#takes the length of the password and creates a distinct password
#also takes intput if you want to make a new password or save this password
def pass_create():
    global password
    root3 = Tk()
    root3.title("Password")
    try:
        user_input_length = eval(entrypass.get())
        print(user_input_length)
        
        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
        symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<',"[", "]", "{", "}",";", "'", "\'" ]
        random.shuffle(DIGITS)
        random.shuffle(LOCASE_CHARACTERS)
        random.shuffle(UPCASE_CHARACTERS)
        random.shuffle(symbols)
        combined_list = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + symbols
        rand_numb = random.choice(DIGITS)
        rand_locar = random.choice(LOCASE_CHARACTERS)
        rand_upcar = random.choice(UPCASE_CHARACTERS)
        rand_symbols = random.choice(symbols)
        rand_noshit = random.choice(rand_locar + rand_numb +rand_upcar + rand_symbols)
        random.shuffle(rand_noshit)
        rand_shit = rand_locar + rand_numb +rand_upcar + rand_symbols + rand_noshit
        for x in range(user_input_length):
            rand_shit = rand_shit + random.choice(combined_list)
        rand_shit = array.array("u",rand_shit)
        password = random.shuffle(rand_shit)
        password = ""
        for x in rand_shit:
            password = password + x
        Label(root3,text=f"Your new and distinct password is {password} ").pack()
        Button(root3,text="Create again",command=theloopwhichneverends).pack()
        Button(root3,text="Save",command=savepass).pack(side=LEFT)
        
    except:
        tmsg.showerror("Error","Not valid input")
        sys.exit()
    root3.mainloop()
def createpass ():
    #takes length of the password you want to create from the user
    global entrypass
    root2=Tk()
    root2.title("Create Password")
    Label(root2,text="Enter the length of password you want to create.").pack()
    entrypass = Entry(root2)
    entrypass.focus_set()
    entrypass.pack()
    Button(root2,text="Confirm",command=pass_create).pack()
    root2.after(pass_create)
    root2.mainloop() 
   #reads the file which has old generated passwords in it
def showoldpass():
    f = open("pass.txt","r")
    root5 = Tk()
    root5.title("Old Passwords")
    root5.geometry("1000x800")

    Label(root5,text=f"{f.read()}").pack()
    f.close()
    root5.mainloop()
root = Tk()
root.title("Store your password")
root.geometry("390x270")
root.config(bg="#272391")
sbarvar = StringVar()
sbarvar.set("All your information is private :wink:")
sbar = Label(root,textvariable=sbarvar,relief= SUNKEN,anchor= "w",bg="#f0b6b6")#status bar
sbar.pack(side=BOTTOM,fill= X)
lable1 = Label(root,text="Create a new pass!",fg="#e6175c",bg="#272391",font="Arial 20").pack()
createpassbutton=Button(root,text="CREATE",padx=10,pady=10,bg="black",fg="#CAF1DE",command=createpass).pack()
ttk.Separator(root,orient=HORIZONTAL).pack(fill=X)
lable2 = Label(root,text="Old passwords and usernames",fg="#e6175c",bg="#272391",font="Arial 20").pack()
oldpassshowerbutton=Button(root,text="SHOW OLD PASSWORDS",padx=10,pady=10,bg="black",fg="#CAF1DE",command=showoldpass).pack()
root.mainloop()
