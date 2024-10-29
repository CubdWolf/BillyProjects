import os
import time
import subprocess
import webbrowser

# Im not good enough at python u need to teach me
#Learn English you retarded
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


def PasswordMachine():
  #I made what you asked  and the passwords are scsectrodod
  password = input("Enter your password\n")
  if password == os.environ['BillyPassword']:
    print("Hi Billy")
    input("Enter anything to continue")
    ChooseThePoop()
  if password == os.environ['SmartBillyPassword']:
    print("Hi smart Billy")
    input("Enter anything to continue")
    ChooseThePoop()
  else:
    print("NOOOOOOOOOOOOOOOOOOOOOOO go away I hate youuuuuuuuuuuuuuuuuuuuuuuuu (or if you typed\nwrong then ur just retartred)")
    time.sleep(5)
    ChooseThePoop()
    
def TheMagicLab():
  print("\nThis is the secret magic lab shhhhh\n")

  
  print("Giving stats:")
  os.system("date")
  os.system('uname -o')
  os.system("pwd -L")
  os.system("pwd -P")
  os.system("ls")
 # os.system("ls -l") #to have a long list of all the files (The first dash shows this is a file, not a directory (you would see a 'd' instead if it were a directory). After that you have 3 groups of rwx permissions (read, write, execute). The first 3 pertain to the owner of the file, the second 3 to his group, and the third to any user.)
  os.system("touch billy.txt")

  
  clearBilly = input("\n\nShould We clear billy? ")
  if clearBilly in ["Yes", "yes", "y"]:
    os.system("echo > billy.txt")
    
  addToFile = input("Add something to billy? ")
  if addToFile in ["Yes", "yes", "y"]:
    printedMessage = input("What the hell is to this file?")
    os.system("echo " + printedMessage + ">> billy.txt")

  
  proceed = input("Continue? ")
  if proceed in ["Yes", "yes", "y"]:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Continued\n")
  else:
    ChooseThePoop()

  print("Started shell commands, they should work now \n-- Nvm im retarted ill just use objects and they should work permanently")
  # look at this is so weird
  #so  hard i dont understand ho 
  #it workss soooo ahrd
  #this is p
  #sename and password for those access
  #ok...#i make a password that only i know :D i could fiind itsilly billy
  
def ChooseThePoop():
  cls()
  print("Credit to me only")
  chooseThePoop = input("Choose where you want to go.\n\n1)Maths\n2)CookieEnter\n3)Mid Cookie Clicker\n ")
  if chooseThePoop == "1":
    cls()
    import Maths
  elif chooseThePoop == "2":
    cls()
    import CookieEnter
  elif chooseThePoop == "3":
    cls()
    import TTKCookieClicker

  elif chooseThePoop in ["Secret Magic", "Magic lab", "magic lab", "ml"]:
      TheMagicLab()

  elif chooseThePoop.lower() == "backup":
    os.system('cp main.py mainBackup.py')
    os.system("cp main.py mainBackup2.txt")
    print("Successfully updated backup")

  elif chooseThePoop == "password":
    PasswordMachine()
    
  elif chooseThePoop.lower() == "restart":
    ChooseThePoop()

  elif chooseThePoop in ["run", "Run"]:
    whatFile = input("What file do you want to run?\n")
    os.system("python " + whatFile +".py")

  elif chooseThePoop == "index":

    from flask import Flask, render_template
    app = Flask(__name__,template_folder='templates', static_folder='static')

    @app.route('/')
    def index():
      webHook = os.environ["WebHook"]
      return render_template("index.html", webHook=webHook)
    
    
    app.run(host='0.0.0.0', port=8080)

    ChooseThePoop()
  else:
    print("How can you be so fucking dumb you asshole. Like bro, " + chooseThePoop + " doesn't exist!You're a fucking piece of human shit, go back to studying numbers pussy.")
    time.sleep(7)
    cls()
    ChooseThePoop()


ChooseThePoop()

#vc?$ okidoki
# yuthong made billy


#TODO: Finish all the 3 math Functions
#TODO: Add more math Functions
#TODO: Do stocheio in the chemestry part
#TODO: Do a visual UI like a graphics calculator or smthn
#TODO: make more readable

