"""
Python AI
By Captain Pi & EBz
Version 0.0.3
"""

#Imports
from time import *
from random import choice
from calendar import month
import platform

#Variables
ID = 0
Version = ('0.0.3')

#Functions
def Update():#UPDATE FILES
    global namesList,jokesList,feelingsList,factsList
    #Variables
    namesList = []
    jokesList = []
    feelingsList = []
    factsList = []
    #namesList
    try:
        file = open('namesList.txt','r')
    except FileNotFoundError:
        file = open('namesList.txt','w').close()
        file = open('namesList.txt','r')
    line = file.readline().split(',')
    for i in line:
        if i != '' and i.isalpha() == True:
            namesList.append(i)
    file.close()
    #Jokes
    try:
        file = open('jokesList.txt','r')
    except FileNotFoundError:
        file = open('jokesList.txt','w').close()
        file = open('jokesList.txt','r')
    for line in file:
        jokesList.append(line.replace('\n',''))
    file.close()
    #feelingsList
    try:
        file = open('feelingsList.txt','r')
    except FileNotFoundError:
        file = open('feelingsList.txt','w').close()
        file = open('feelingsList.txt','r')
    for line in file:
        feelingsList.append(line.replace('\n',''))
    file.close()
    #factsList
    try:
        file = open('factsList.txt','r')
    except FileNotFoundError:
        file = open('factsList.txt','w').close()
        file = open('factsList.txt','r')
    for line in file:
        factsList.append(line.replace('\n',''))
    file.close()
    return True

def Title(): # TITLE INTRO
    Title = ['⌠☒☒☯☢◙◙▒▒▒▓▓▓▓▓██████████▓▓▓▓▓▒▒▒◙◙☢☯☒☒╖','╫                                      ╫','║ ⌠◙┐   ⌠◙\ /◙┐ ⌠◙▒▓☒\   ⌠◙┐    ⌠◙█☒╖  ║','│ │▒║    \▓∨▓/  │▒┌╤\▒   │█║   │▓║☢║▓╖ │','☯ ║▓║     ║▓╫   ║▓╫☯╫▓   ║▓▒   ║█▒▓▒█║ ☯','│ │▒└__   │▓║   │▒└╧/▒   │█╫   │█╫ ║█╫ │','║ ⌡◙▒▓▒ ☢ ⌡█╝ ☢ ⌡◙▒▓☒/ ☢ ⌡◙╝ ☢ ⌡▒╝ └▒╝ ║','╫ ¯¯¯¯¯   ¯¯¯   ¯¯¯¯¯    ¯¯¯   ¯¯¯  ¯¯ ╫','⌡☒☒☯☢◙◙▒▒▒▓▓▓▓▓██████████▓▓▓▓▓▒▒▒◙◙☢☯☒☒╝']
    for i in Title:
        for ii in i:
            print(ii,end="")
        print('')
    print('\n      By Captain Pi and EBz\n           Version',Version,'\n        running on:',platform.platform().split('-')[0],'\n')
    return True

def Question(): #AI QUESTIONS
    global jokesList,feelingsList,factsList
    #Input
    i = str(input(': '))
    file = open('symbolsList.txt','r')
    for symbol in file:
        i = i.replace(symbol.replace('\n',''),'').lower()
    Input = []
    for ii in i:
        if ii == " ":
            i = i.split()
            for ii in i:
                Input.append(ii)
            break
    if len(Input) == 0:
        Input.append(i)
    i = 0
    #Questions
    for word in Input:
        if word == 'time':
            print('The current time is',strftime('%H:%M:%S'))
        elif word == 'date':
            print("Today's date is",strftime('%d/%m/%Y'))
        elif word == 'name':
            if Input[i-1] == 'my':
                Name(1)
            elif Input[i-1] == 'your':
                print('My name is Lydia')
        elif word == 'joke':
            print(choice(jokesList))
        elif word == 'feeling':
            if Input[i-1] == 'you':
                print('I am feeling',choice(feelingsList))
        elif word == 'fact':
            if Input[i-1] == 'a':
                print ('Here is a fact:\n'+str(choice(factsList)))
        elif word == 'you':
            try:
                if Input[i-1] == 'are' and Input[i-2] == 'who' or Input[i-2] == 'what':
                    print ('I am an artificial intelligence.\nI was created by Justinas Grigas and Ebenezer Odubanjo.')
            except IndexError:
                continue
        elif word == 'timer':
            if Input[i+2].isdigit() == True:
                if Timer(int(Input[i+2])):
                    print('The timer has ended sucessfully\nThe timer has been on for',Input[i+2],'minutes\nThe current time now is',strftime('%H:%M:%S'))
                else:
                    print('The timer has been interrupted')
        elif word == 'calendar':
            try:
                if Input[i+3].isdigit() == True:
                    if Input[i+2].isdigit() == True:
                        print(month(int(Input[i+3]),int(Input[i+2])))
                    elif Input[i+2].isalpha() == True:
                        months=['january','february','march','april','may','june','july','august','september','october','december','november',]
                        for x in range(len(months)):
                            if months[x] == Input[i+2]:
                                mon = x+1
                                break
                        print(month(int(Input[i+3]),int(mon)))
                else:
                    print('I do not understand your command')
            except IndexError:
                print('I do not understand your command')
        elif word == 'plus' or word == '+':
            if Input[i-1].isdigit() == True and Input[i+1].isdigit() == True:
                print(int(Input[i-1])+int(Input[i+1]))
        elif word == 'minus' or word == '-':
            if Input[i-1].isdigit() == True and Input[i+1].isdigit() == True:
                print(int(Input[i-1])-int(Input[i+1]))
        elif word == 'times' or word == '*':
            if Input[i-1].isdigit() == True and Input[i+1].isdigit() == True:
                print(int(Input[i-1])*int(Input[i+1]))
        elif word == 'divide' or word == '/':
            if Input[i-1].isdigit() == True and Input[i+1].isdigit() == True:
                print(int(Input[i-1])/int(Input[i+1]))
        elif word == 'hello' or word == 'hey' or word == 'hi':
            print("Hello!")
        elif word == 'bye' or word == 'adieu' or word == 'adios':
            print("Good Bye!")
        #END counter
        i += 1

def Name(option): #NAMES
    global namesList,ID
    if option == 0: #start
        name = str(input('What is your name?\n: ')).lower()
        User = False
        i = 0
        for user in namesList:
            if name == user:
                User = True
                ID = i
                print('Welcome back '+name.title())
                break
            else:
                i += 1
        if User == False:
            namesList.append(name)
            file = open('namesList.txt','w')
            for user in namesList:
                file.write(user+',')
            file.close()
            ID = len(namesList) - 1
            Update()
            print('Welcome\nMy name is Lydia')
    elif option == 1: #AI
        print('Your name is',namesList[ID].title())

def Timer(x):
    seconds = x * 60
    print('The current time is',strftime('%H:%M:%S'))
    try:
        for x in range(seconds):
            sleep(1)
        return True
    except KeyboardInterrupt:
        return False

def Exit(): #EXIT
    i = str(input('Do you want to exit?\n: ')).lower()
    if i == 'yes' or i == 'y' or i == 'yep' or i == 'yeah':
        quit()
        
#main
Title()
Update()
Name(0)
while True:
    try:
        Update()
        while True:
            Question()
    except KeyboardInterrupt:
        Exit()
#end
quit()
