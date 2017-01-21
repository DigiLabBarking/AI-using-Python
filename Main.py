"""
Python AI
By Captain Pi & EBz
Version 0.0.1
"""
#Imports
from time import strftime
from time import sleep
import random
joke_list = [joke1, joke2, joke3, joke4,] #list of functions

#Variables
ID = 0

#Joke Functions
def joke1():
    print("I wondered why the frisbee was getting bigger, and then it hit me.")
def joke2():
    print("I used to like my neighbors, until they put a password on their Wi-Fi.")
def joke3():
    print("If practice makes perfect, and nobody's perfect, why practice?")
def joke4():
    print("I once farted in an elevator, it was wrong on so many levels.")
def joke5():
    print("What do you call a bear with no teeth? -- A gummy bear!")


#Functions
def Loading(): #LOADING
    for x in range(100):
        print(x+1,'%')
        sleep(0.01)
    return True

def Title(): # TITLE INTRO
    #Loading()
    file = open('Title.txt','r')
    for line in file:
        for char in line:
            print(char,end="")
    file.close()
    print("\n      By Captain Pi and EBz")
    print("           Version 0.0.1\n")
    return True

def Update():#UPDATE FILES
    global Names
    Names = []
    try:
        file = open('Names.txt','r')
    except FileNotFoundError:
        file = open('Names.txt','w')
        file.close()
        file = open('Names.txt','r')
    line = file.readline()
    line = line.split(',')
    for name in line:
        if name != '':
            Names.append(name)
    file.close()

def Question(): #AI QUESTIONS
    X = str(input("Ask me a question\n: "))
    file = open('Symbols.txt','r')
    for symbol in file:
        symbol = symbol.replace('\n','')
        X = X.replace(symbol,'')
    X = X.lower()
    Words = []
    for x in X:
        if x == " ":
            X = X.split()
            for y in X:
                Words.append(y)
            break
    if len(Words) == 0:
        Words.append(X)
    counter = 0
    for x in Words:
        print(x)
        if x == 'time':
            print("The current time is",strftime('%H:%M'))
        elif x == 'date':
            print("Today's date is",strftime('%d/%m/%Y'))
        elif x == 'name':
            Name(1)
            counter += 1
        elif x == 'joke':
            joke = random.choice(joke_list)
            joke()

def Name(option): #NAMES
    global Names,ID
    if option == 0: #start
        name = str(input("What is your name?\n: "))
        name = name.lower()
        User = False
        counter = 0
        for user in Names:
            if name == user:
                User = True
                ID = counter
                print('Welcome back '+name.title())
                break
            else:
                counter += 1
        if User == False:
            Names.append(name)
            file = open('Names.txt','w')
            for user in Names:
                file.write(user+',')
            file.close()
            ID = len(Names) - 1
            Update()
            print("Welcome\nMy name is Lydia")
    elif option == 1: #AI
        print('Your name is',Names[ID].title())

def Exit(): #EXIT
    x = str(input('Do you want to exit?\n: '))
    x = x.lower()
    if x == 'yes' or x == 'y' or x == 'yep' or x == 'yeah':
        file.close()
        quit()
    elif x == 'no' or x == 'n':
        return True

#main
Title()
while True:
    try:
        Update()
        Name(0)
        while True:
            Question()
    except KeyboardInterrupt:
        Exit()
#end
quit()
