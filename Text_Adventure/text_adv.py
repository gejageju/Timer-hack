import time
time.sleep(1)
print("Its getting really dark")
time.sleep(2)
print("You came here to this forest with your crew")
time.sleep(1)
print("They are nowhere to be found")
time.sleep(1)
print("It seems like you are stuck here...")
time.sleep(1)
print("All alone ......")
time.sleep(1)

name=input("Enter your name: ")
time.sleep(1)
print("So hello! "+name)
print("Your goal is to find your crewmates before it gets too late!")
time.sleep(1)
print("You  Ready !!??")
input()
print("Make wise choices or else you will die :)")
time.sleep(2)
print("Lets begin !")

time.sleep(3)
print("Its getting dark...\nYou hear the crickets chirp...\nThe leaves rustle due to the slow wind...")
time.sleep(2)
print("You hear the growl of a bear...")
time.sleep(2)
print("From Somewhere Far Away")
time.sleep(2)
print("Its getting really cold")
time.sleep(2)
print("What will you do")
time.sleep(2)
choice=int(input("1. Wait for you crewmates\n2.Try creating a fire\n3.Make noise and cry for help\n"))
if(choice==1):
      time.sleep(2)
      print(name+" keeps waiting in te cold")
      time.sleep(1)
      print(name+" sits there for hours")
      time.sleep(1)
      print(name+" loses stamina slowly and faints")
      time.sleep(1)
      print("Faints in the middle of nowhere in a dangerous forest")
      time.sleep(2)
      print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
if choice==2:
   time.sleep(2)
   print(name+" decides to start a fire\nHow will "+name+" start one")
   x=input("1.Make a pit, Gather twigs, slowly build fire with friction\n2.Gather leaves, rub twigs fiercely")
   if x==2:
       time.sleep(2)
       print(name+" tries creating fire ")
       time.sleep(2)
       print("Yay! "+name+" sees smoke\nThe fire grows")
       time.sleep(3)
       print("Oops !"+name+" starts a forest fire")
       time.sleep(3)
       print(name +" suffocates and dies")
       print("~~~~~~~~~~~~~~~~~~Game-over~~~~~~~~~~~~~~~~")
   if x==1:
       pass
if choice==3:
   pass
