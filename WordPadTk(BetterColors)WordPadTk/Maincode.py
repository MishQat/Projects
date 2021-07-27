from tkinter import * 
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
#defining functions of submenues
def rate ():
      value_user = tmsg.askyesno("Rate Us!!!","You used our Gui, was it good?")
      if value_user :#for true of false statements
            tmsg.showinfo("Thank you","Thanks for being with us we love you")
      else:
            tmsg.showinfo("Thank you","Oh no please let us know what you didnt like")
def newfile():
    global file
    root.title("untitled - WordPad")
    file = None
    textarea.delete(1.0,END)

def openfile ():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents",".txt")])#we told how to open files according to what format they are in
    #TODO: Searces the files from PC
    if file == ".txt":# if file black then no need to do anything
        tmsg.showwarning("Warning", "The file you are trying to open is blank!")
        file =None
    else:
        root.title(os.path.basename(file)+" - WordPad")
        textarea.delete(1.0,END)#deletes old file to open new one
        f = open(file,"r")
        textarea.insert(1.0,f.read())# copies all the data from first to last and pastes on new textarea
def savefile ():
    global file
    #for saving a NEW FILE
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents",".txt")])#asks to save as what name
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - WordPad")#saving a new file and changing the tittle with it
    # For saving a old file or updating it
    else:
        f = open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
def cutfile ():
    textarea.event_generate(("<<Cut>>"))#constants
def copyfile ():
    textarea.event_generate(("<<Copy>>"))#constants
def pastefile():
    textarea.event_generate(("<<Paste>>"))#constants
def aboutwordpadfunc():
    tmsg.showinfo("About WordPad","WordPad was made my the great Ahmed Mishqat on 27th of July of 2021. If you do like it I would appreaciate if you did rate us!")
def helpfunc():
    tmsg.showinfo("Help","If you are having issues with using WordPad. Contact mishqat0612@gmail.com to talk with us!")
#Functions end here
#Main part
if __name__ == "__main__":
    global root
    global textarea
    root = Tk()
    root.geometry("690x420")
    root.title("untitled - WordPad")
    root.wm_iconbitmap("wordicon.ico")
    #text adder
    textarea = Text(root,bg="#5dc2bd",fg="#451e3e",font="Helvetica ")
    file = None
    textarea.pack(expand=True,fill=BOTH)
    Scroll = Scrollbar(textarea)#setting scroll bar
    Scroll.pack(side=RIGHT,fill=Y)#on right side of the text area for y axis
    Scroll.config(command=textarea.yview)#constants
    textarea.config(yscrollcommand=Scroll.set)#constants

    mymenu=Menu(root)#creates a menu like one the top right corner of vscode
    #File menu starts
    submenu = Menu(mymenu,tearoff= 0)#creates a submenu like a dropdown box TODO : tearoff = dosent create a option for dropout box
    submenu.add_command(label="New", command= newfile)#commands

    submenu.add_command(label="Open",command=openfile)
    submenu.add_command(label="Quit",command=quit)
    submenu.add_command(label="Save", command= savefile)
    mymenu.add_cascade(label="File", menu= submenu)#adds the submenu inside the menu bar important very much(Labelled under "file") 
    #file menu ends
    #edit menu starts
    submenu2 = Menu(mymenu,tearoff=0)
    submenu2.add_command(label="Cut",command=cutfile)
    submenu2.add_command(label="Copy",command=copyfile)
    submenu2.add_command(label="Paste",command=pastefile)
    mymenu.add_cascade(label="Edit",menu=submenu2)
    #edit menu ends
    #help menu starts
    submenu3 = Menu(mymenu,tearoff=0)
    submenu3.add_command(label="Help",command= helpfunc)
    submenu3.add_command(label="Rate us",command=rate)
    submenu3.add_separator()
    submenu3.add_command(label="About WordPad", command=aboutwordpadfunc)
    mymenu.add_cascade(label="Help",menu=submenu3)
    root.config(menu=mymenu)#configures the menu important step
    #help menu ends

    root.mainloop()
