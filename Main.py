"""
Python AI
By Captain Pi & EBz
Version 0.0.1
"""
#Imports
from time import strftime,sleep
from random import choice
import platform

platform = platform.platform()
platform = platform.split('-')

#Variables
ID = 0

#Functions
def Jokes(): #UPDATE JOKES
    global jokeList
    jokeList = []
    file = open('jokes.txt','r')
    for line in file:
        line = line.replace('\n','')
        jokeList.append(line)
    file.close()
    return True

def Loading(): #LOADING
    for x in range(100):
        print(x+1,'%')
    return True

def Title(): # TITLE INTRO
    #Loading()
    #Title = ['⌠☒☒☯☢◙◙▒▒▒▓▓▓▓▓████▓▓▓▓▓▒▒▒◙◙☢☯☒☒╖','╫                                ╫','║ ⌠◙┐ ⌠◙\ /◙┐ ⌠◙▒▓☒\ ⌠◙┐  ⌠◙█☒╖  ║','│ │▒║  \▓∨▓/  │▒┌╤\▒ │█║ │▓║☢║▓╖ │','☯ ║▓║   ║▓╫   ║▓╫☯╫▓ ║▓▒ ║█▒▓▒█║ ☯','│ │▒└__ │▓║   │▒└╧/▒ │█╫ │█╫ ║█╫ │','║ ⌡◙▒▓▒ ⌡█╝   ⌡◙▒▓☒/ ⌡◙╝ ⌡▒╝ └▒╝ ║','╫ ¯¯¯¯¯ ¯¯¯   ¯¯¯¯¯  ¯¯¯ ¯¯¯  ¯¯ ╫','⌡☒☒☯☢◙◙▒▒▒▓▓▓▓▓████▓▓▓▓▓▒▒▒◙◙☢☯☒☒╝']
    #for x in Title:
    #    for y in x:
    #        print(y,end="")
    #    print('')
    print("\n      By Captain Pi and EBz")
    print("           Version 0.0.1\n")
    print("running on: ",platform.platform())
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
    global jokeList
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
        if x == 'time':
            print("The current time is",strftime('%H:%M:%S'))
        elif x == 'date':
            print("Today's date is",strftime('%d/%m/%Y'))
        elif x == 'name':
            Name(1)
        elif x == 'joke':
            print(choice(jokeList))
        counter += 1

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
        quit()
    elif x == 'no' or x == 'n':
        return True

#main
try:
    Title()
except UnicodeDecodeError:
    print('BOB')
Jokes()
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
