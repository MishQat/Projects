from tkinter import *
from typing import Sized

def click(event):
    text = event.widget.cget("text")#Gets the data of the widget in this case the button that has been pressed 
    
    if text == "=":
        if Screenvalue.get().isdigit():#checks if the number on the calculator is digits or not
            value = float(Screenvalue.get())#calculates the number
        else:
            value = eval(Screenvalue.get())#calculates the number 
        Screenvalue.set(value)#updates the answer
        Frame1.update()
    elif text == "C":
        Screenvalue.set("")# if C is pressed the whole frame is cleared 
        Frame1.update()  
    else:
        Screenvalue.set(Screenvalue.get() + text)# The button you pressed get printed on the Frame. and new numbers are added at the end 
        Frame1.update()#Forces an update to update the frame to the new data

root = Tk()
root.geometry("854x800")
root.configure(bg="#00B4AB")
root.title("Calculator ")
root.wm_iconbitmap("calculator - Copy.ico")
sbarvar = StringVar()
sbarvar.set("Calculator 1.0.0 by Ahmed Mishqat____________________________________________________________________________________________________________________hope you enjoy it.")
sbar = Label(root,textvariable=sbarvar,relief= SUNKEN,anchor= "w",bg="#db3939")#status bar
sbar.pack(side=BOTTOM,fill= X)
Screenvalue=StringVar()
Screenvalue.set("")
Entryofuser = Entry(root,textvariable=Screenvalue,font= "lucida 40 bold",fg=  "#e6175c",background= "#000000").pack(fill=X, padx=20,pady=30)
#TODO:We make the button which will print out theris coresponding number in the calculator
#for number 1,2,3

Frame1 = Frame(root,bg="#79c9bc")
Buttonnum = Button(Frame1,text="1",fg="#000000",font="Lucida 35 bold",padx=22,pady=28,bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)#we binded the button to the right click of the mouse, and created the command "click"
Buttonnum = Button(Frame1,text="2",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="3",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6,  pady=5)
Buttonnum.bind("<Button-1>",click)
Frame1.pack( pady= 10)

#for number 4,5,6
Frame1 = Frame(root,bg="#79c9bc",)
Buttonnum = Button(Frame1,text="4",fg="#000000",font="Lucida 35 bold",padx=22,pady=28,bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)#we binded the button to the right click of the mouse, and created the command "click"
Buttonnum = Button(Frame1,text="5",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="6",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6,  pady=5)
Buttonnum.bind("<Button-1>",click)
Frame1.pack(pady= 10)

#for number 9,8,7
Frame1 = Frame(root,bg="#79c9bc",)
Buttonnum = Button(Frame1,text="7",fg="#000000",font="Lucida 35 bold",padx=22,pady=28,bg= "#0269A4")
Buttonnum.pack(side=LEFT,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)#we binded the button to the right click of the mouse, and created the command "click"
Buttonnum = Button(Frame1,text="8",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="9",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6 ,pady=5)
Buttonnum.bind("<Button-1>",click)
Frame1.pack(pady=10)

#Operators
Frame1 = Frame(root,bg="#79c9bc")
Buttonnum = Button(Frame1,text="%",fg="#000000",font="Lucida 35 bold",padx=22,pady=28,bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)#we binded the button to the right click of the mouse, and created the command "click"
Buttonnum = Button(Frame1,text="*",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="+",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6,  pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="-",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6,  pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="=",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6,  pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="C",fg="#000000",font="Lucida 35 bold",padx=22,pady=28, bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6,  pady=5)
Buttonnum.bind("<Button-1>",click)
Buttonnum = Button(Frame1,text="/",fg="#000000",font="Lucida 35 bold",padx=22,pady=28,bg= "#0269A4")
Buttonnum.pack(side=LEFT ,padx= 6, pady=5)
Buttonnum.bind("<Button-1>",click)
Frame1.pack( side = BOTTOM,pady= 10)


root.mainloop()
