import sys,tty,os,termios
def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left', 
                
            }
            return key_mapping.get(k, chr(k))
    finally:
       termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def KeyThings():
  
    while True:
        k = getkey()
        if k == 's':
            print("What")
        


KeyThings()

import threading
import time
#billy make the shop a function of its own wait i have to work rn
#add exit for the shopshopshopshop

cookies = 0
william = 0
grandma = 0
grandmaPrice = 10
proceed = 0
williamPrice = 100

print("Press 'Enter' to get a cookie, say 'shop' for the shop")

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


def commands():
  command = input("Enter command\n")
  if command == "backup":
    os.system("cp main.py mainBackup.py")
    print("Successfully updated backup")

  if command == "run":
    whatFile = input("what file do you want to run?\n")
    os.system("python " + whatFile)
  
  else:
    print("e")

def PrintThings():
  global cookies
  global william
  global grandma
  global Shopping
  global proceed
  global grandmaPrice
  printedCookies = 0

  while True:
    time.sleep(0.1)
    if cookies != printedCookies:
      if proceed in ["shop"]:
        print("e")
      else:
        cls()
        if cookies < 1000:
          print("You have " + str(round(cookies,1)) + " cookies")
        if cookies >= 1000:
          print("You have " + str(round(cookies/1000,1)) + "k cookies")
        if william <= 1:
          print("You have "+str(william)+" william")
        else:
          print("You have "+str(william)+" williams")
        
        if grandma <= 1:
          print("You have "+str(grandma)+" grandma")
        else:
          print("You have "+str(grandma)+" grandmas")
        
        printedCookies = cookies
    
def Grandma():
  
  global cookies
  global grandma
  
  while True:
    
    cookies = cookies + grandma * 0.1
    
    time.sleep(1)



def main():   
  
  global cookies
  global grandma
  global william
  global grandmaPrice
  global williamPrice

  printCookies = threading.Thread(target = PrintThings, daemon=True)
  printCookies.start()
  
  while True:

    proceed = input("")
    
    if proceed == "shop":
      Shopping = input("1:Buy a William ("+str(williamPrice)+")\n2:Buy a Grandma ("+str(grandmaPrice)+")\n")
  
      if Shopping == "1":
        howManyWilliamBuy = input("how many williams do you want to buy?\n")
        
        if cookies > williamPrice*float(howManyWilliamBuy):
#if shopIsThere == 1
          #dont cls()
          williamPrice = williamPrice * 1.2
          cookies = cookies - williamPrice
          0*float(howManyWilliamBuy)
          william = william + 1
          print("you now have " + str(william) + " william")
        
        else:

          print("Omg so silly, you don't have enough money to buy that stuff")
          
        
      if Shopping == "2": 

        if cookies > grandmaPrice:

          cookies = cookies - grandmaPrice
          grandma = grandma + 1
          grandmaPrice = grandmaPrice * 1.2
          print("you now have " + str(grandma) + " grandma")
          if grandma == 1:
            grandmaThreading = threading.Thread(target=Grandma, daemon=True)
            grandmaThreading.start()
          
        else:

          print("Omg so silly, you don't have enough money to buy that stuff")
          
      else:
        print("So silly you can't buy that stuff")
        
    if proceed == "commands":
      commands()
  
    if proceed == "addcookies":
      cookies = cookies + int(input(""))
      cls()
    if proceed == "w":
      os.system("python W.py")
      
    else: 
      
      cookies = cookies + 1 + william * 0.1
      time.sleep(0.01)
      
main()

#cus it never gets to the grandma ffunction it just stays at the loop before it and for this u need threading i htink
