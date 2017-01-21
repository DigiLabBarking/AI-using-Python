"""
Python AI
By Captain Pi & EBz
Version 0.0.1
"""
#imports
from time import strftime

#variables
ID = 0

#functions
def Update():
    global Names
    Names = []
    file = open('Names.txt','r')
    line = file.readline()
    line = line.split(',')
    for name in line:
        if name != '':
            Names.append(name)
    print(Names)
    file.close()
def Question():
    X = str(input("Ask me a question\n: "))
    file = open('Symbols.txt','r')
    for symbol in file:
        X.replace(symbol,'')
    X.lower().split(" ")
    for x in X:
        if x == 'time':
            Time()
        elif x == 'date':
            Date()
        elif x == 'name':
            Name(1)
def Name(option):
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
                print('Welcome back '+name)
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
    elif option == 1: #AI
        name = Names[ID]
        name.title()
        print('Your name is',name)
def Time():
    print(strftime('%H:%M:%S'))
def Date():
    print(strftime('%d/%m/%Y'))
def Exit():
    x = str(input('Do you want to exit?\n: '))
    x = x.lower()
    if x == 'yes' or x == 'y' or x == 'yep' or x == 'yeah':
        quit()
    elif x == 'no' or x == 'n':
        return True

#main
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
