import os
import time

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def Functions():
  
  while True:
    ClearScreen = 0
    print("e")
    fonctionFormula = input(
      "What is the formula of the function? \n1) f(x) = ax+b \n2) f(x) = a(x-h)^2+k \n3) f(x) = a[b(x-h)]+k \n4) f(x) = a√bx \n5)Fonction valeur absolue \n \n"
    )
    #function 1 (Droite)
    if fonctionFormula == "1":
      pointOrVarialbe = input("Do we have 2 points and want to find the formula or do we have every variable except one? \n1) Every variable except one. \n2) 2 points \n  ")
      #looking for variable 
      if pointOrVarialbe == "1":
        lookingFor = input("\nWhat variable are we looking for? \n")
  
        if lookingFor in ["y", "Y", "f(X)"]:
          a = float(input("What is the value of a? \n"))
          x = float(input("What is the value of x? \n"))
          b = float(input("What is the value of b? \n"))
          findingY = str(a * x + b)
          print("The value of y is " + findingY)
  
        elif lookingFor in ["a", "A"]:
          y = float(input("What is the value of y? \n"))
          x = float(input("What is the value of x? \n"))
          b = float(input("What is the value of b? \n"))
          findingA = str((y - b) / x)
          print("The value of a is " + findingA)

        elif lookingFor in ["x", "X"]:
          y = float(input("What is the value of y? \n"))
          a = float(input("What is the value of a? \n"))
          b = float(input("What is the value of b? \n"))
          findingX = str((y - b)/ a)
          print("The value of x is " + findingX)  
  
        elif lookingFor in ["b", "B"]:
          a = float(input("What is the value of a? \n"))
          x = float(input("What is the value of x? \n"))
          y = float(input("What is the value of y? \n"))
          findingB = str(y - (x * a))
          print("The value of b is " + findingB)

      #looking for function with 2 points  
      elif pointOrVarialbe == "2": 
        x1 = float(input("What is the value of the 1st X"))
        y1 = float(input("What is the value of the 1st Y"))
        x2 = float(input("What is the value of the 2nd X"))
        y2 = float(input("What is the value of the 2nd Y"))
        findingA = str((y2 - y1)/(x2 - x1))
        a = float(findingA)
        findingB = str(y1-(a * x1))

        print("The formula is f(x) = " + findingA + "x + " + findingB)
    #function 2 (Parabole)
    if fonctionFormula == "2":
      pointOrVarialbe = input("Do we have the peak and a point and want to find the formula or do we have every variable except one? \n1) Every variable except one. \n2) peak with a point \n  ")
      if pointOrVarialbe == "1":
        lookingFor = input("\nWhat variable are we looking for? \n")
        if lookingFor in ["y", "Y", "f(x)"]:
          a = float(input("What is the value of a? \n"))
          x = float(input("What is the value of x? \n"))
          h = float(input("What is the value of h? \n"))
          k = float(input("What is the value of k? \n"))
          findingY = str(a * (x - h) * (x - h) + k)
          print("The value of y is " + findingY)
  
        elif lookingFor in ["a", "A"]:
          y = float(input("What is the value of y? \n"))
          x = float(input("What is the value of x? \n"))
          h = float(input("What is the value of h? \n"))
          k = float(input("What is the value of k? \n"))
          findingA = str((y - k) / ((x - h) * (x - h)))
          print("The value of a is " + findingA)
  
        elif lookingFor in ["x", "X"]:
          y = float(input("What is the value of y? \n"))
          a = float(input("What is the value of a? \n"))
          h = float(input("What is the value of h? \n"))
          k = float(input("What is the value of k? \n"))
          findingX1 = str((((y - k) / a)**0.5) + h)
          findingX2 = str((-((y - k) / a)**0.5) + h)
          print("The value of x is " + findingX1 + " and " + findingX2)
  
        elif lookingFor in ["h", "H"]:
          y = float(input("What is the value of y? \n"))
          a = float(input("What is the value of a? \n"))
          x = float(input("What is the value of x? \n"))
          k = float(input("What is the value of k? \n"))
          findingH = str(((((y - k) / a)**0.5) - x)/-1)
          
          print("The value of a is " + findingH)
  
        elif lookingFor in ["k", "K"]:
          y = float(input("What is the value of y? \n"))
          a = float(input("What is the value of a? \n"))
          x = float(input("What is the value of x? \n"))
          h = float(input("What is the value of h? \n"))
          findingK = str(y-(a*(x - h)*(x - h)))
  
          print("The value of k is " + findingK)
    #looking for function with peak and a point
      elif pointOrVarialbe == "2":
        x = float(input("What is the value of the 1st X"))
        y = float(input("What is the value of the 1st Y"))
        h = float(input("What is the x value of the peak"))
        kc = float(input("What is the y value of the peak"))
        ks = str(kc)
        a = str((y - kc)/(x - h)/(x - h))
        print("f(x) = " + a + "(x - " + h + ")" + ks)

    #function 3 (Partie entière)
    if fonctionFormula == "3":
      lookingFor = input("\nWhat variable are we looking for? \n")

      if lookingFor in ["y", "Y"]:
        a = float(input("What is the value of a? \n"))
        b = float(input("What is the value of b? \n"))
        x = float(input("What is the value of x? \n"))
        h = float(input("What is the value of h? \n"))
        k = float(input("What is the value of k? \n")) # what is the billy doing
        findingAbsoluteValue = str(b * (x - h))
        AbsoluteValue = int(float(findingAbsoluteValue))
        Absolute = float(AbsoluteValue)
        findingY = str((a * Absolute) +k)
        
        print("The value of y is " + findingY)

      elif lookingFor in ["a", "A"]:
        y = float(input("What is the value of y? \n"))
        b = float(input("What is the value of b? \n"))
        x = float(input("What is the value of x? \n"))
        h = float(input("What is the value of h? \n"))
        k = float(input("What is the value of k? \n"))
        findingA = str()#Formula here
        print("The value of a is " + findingA)

      elif lookingFor in ["b", "B"]:
        y = float(input("What is the value of y? \n"))
        x = float(input("What is the value of x? \n"))
        h = float(input("What is the value of h? \n"))
        k = float(input("What is the value of k? \n"))
        findingA = str()#Formula here
        print("The value of a is " + findingA)  

      elif lookingFor in ["x", "X"]:
        y = float(input("What is the value of y? \n"))
        a = float(input("What is the value of a? \n"))
        b = float(input("What is the value of b? \n"))
        h = float(input("What is the value of h? \n"))
        k = float(input("What is the value of k? \n"))
        findingX1 = str()#Formula here
        findingX2 = str()#Formula here
        print("The value of a is " + findingX1 + " and " + findingX2)

      elif lookingFor in ["h", "H"]:
        y = float(input("What is the value of y? \n"))
        a = float(input("What is the value of a? \n"))
        b = float(input("What is the value of b? \n"))
        x = float(input("What is the value of x? \n"))
        k = float(input("What is the value of k? \n"))
        findingH = str()#Formula here
        print("The value of a is " + findingH)

      elif lookingFor in ["k", "K"]:
        y = float(input("What is the value of y? \n"))
        a = float(input("What is the value of a? \n"))
        b = float(input("What is the value of b? \n"))
        x = float(input("What is the value of x? \n"))
        h = float(input("What is the value of h? \n"))
        findingK = str()#Formula here
        print("The value of k is " + findingK)

    else:
        print("omg billy is so silly that is not an option, go back to the start :D")
        time.sleep(1)
        cls()
        
        
    ClearScreen = input("\n \n \n Press enter to go back to the start.")
    if ClearScreen:
      cls()

  cls()



def Chemestry():
  print("WIP")


def ChooseThePoop():
  cls()
  print("Credit to me only")
  chooseThePoop = input("Functions or Chemistry\n\n1)Functions\n2)Chemistry\n ")
  if chooseThePoop == "1":
    cls()
    Functions()
  elif chooseThePoop == "2":
    cls()
    Chemestry()

ChooseThePoop()