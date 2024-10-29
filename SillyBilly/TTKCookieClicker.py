from asyncore import loop
from cmath import e
from lib2to3.pgen2.token import NUMBER
from multiprocessing.connection import wait
from subprocess import call
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
import os
import time
import threading


root = Tk()

rawCookies = 1
cookies = 0
multiplier = 1
multiplierCost = 10
grandmaAmount= 0
grandmaCost = 100
grandmaCps = 0





def CookieButton():
    global rawCookies
    global cookies
    global multiplier

    if multiplier > 1:
        cookies += (rawCookies ^ (multiplier * 10))
        cookieamount_text = "You have "+str(cookies)+" Cookies"
        cookielabel.config(text=cookieamount_text) # Change the text of the label
        print(cookieamount_text)
    else:
        cookies += rawCookies * multiplier
        cookieamount_text = "You have "+str(cookies)+" Cookies"
        cookielabel.config(text=cookieamount_text) # Change the text of the label
        print(cookieamount_text)

    

def MultiplierButton():
    global multiplier
    global multiplierCost
    global rawCookies
    global cookies
    

    if cookies >= multiplierCost:
      cookies = cookies - multiplierCost
      multiplier += 1
      multiplierCost = multiplierCost * 2
      print("Bought multiplier, now at "+str(cookies)+" cookies!")
      cookieamount_text = "You have "+str(cookies)+" Cookies"
      cookielabel.config(text=cookieamount_text)
      multiplier_text = "Multiplier is "+str(multiplier)
      multiplierbutton_text = "This Multiplier Costs "+str(multiplierCost)
      multiplierlabel.config(text=multiplier_text)
      multiplierbutton.config(text=multiplierbutton_text)
      print(multiplier_text)

    if multiplier == 2:
        rawCookies = 2

   

def Grandma():
    global grandmaAmount
    global grandmaCost
    global cookies
    global grandmaCps

    if cookies >= grandmaCost:
        grandmaAmount += 1
        cookies = cookies - grandmaCost
        grandmaCost = grandmaCost * 1.2
        grandma_text = "You have "+str(grandmaAmount)+" grandmas!"
        grandmabutton_text = "Grandma Costs "+str(grandmaCost)
        grandmalabel.config(text=grandma_text)
        grandmabutton.config(text=grandmabutton_text)
        print(grandma_text)
        print(cookies)

    if grandmaAmount == 1:
        b = threading.Thread(name='background', target=GrandmaCookies)
        b.start()

    
        
def GrandmaCookies():
    global cookies
    global grandmaAmount

    while grandmaAmount > 0:
        cookies = (cookies + (grandmaAmount * multiplier))
        time.sleep(1)
        print("Grandma made "+str(cookies))
        cookieamount_text = "You have "+str(cookies)+" Cookies"
        cookielabel.config(text=cookieamount_text) # Change the text of the label


cookielabel = Label(root, text="You have 0 cookies", padx=25, pady=10)
cookielabel.pack()

cookiebutton = Button(root, text="This is a cookie", padx=25, pady=25, command=CookieButton, bg="brown", fg="white")
cookiebutton.pack()


multiplierlabel = Label(root,text="Multiplier is 1", padx=25, pady=10)
multiplierlabel.pack()

multiplierbutton = Button(root, text=" Buy multiplier: 10", padx=25, pady=25, command=MultiplierButton)
multiplierbutton.pack()


grandmalabel = Label(root, padx=10, pady=10, text="You have 0 grandmas")
grandmalabel.pack()

grandmabutton = Button(root, text="Buy a grandma: 100", padx=10, pady=10, command=Grandma)
grandmabutton.pack()


receiptFrame = Frame(root, width=500, height=100)
receiptFrame.pack()

root.mainloop()