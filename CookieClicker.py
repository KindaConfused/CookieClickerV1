from os import system as sys
from time import sleep as slp
from random import randint

cookie = 0
click = 1
autobuy = False
autoR = False
debug = False
chance = False
max = 11

while cookie < 1_000_000:
    if debug == True:
        print("DEBUG MODE ONLY ON RIGHT NOW")
        print("'autobuy' State:", autobuy)
        print("'autoR' State:", autoR)
        print("'Chance' State:", chance)
        debugger = input("I will Execute everything you say. You can say VarNames for varable names\nBe careful: ")
        if debugger != "VarNames":
            exec(debugger)
        else:
            print(f"""
cookie = {cookie}
click = {click}
debug = {debug}
max = {max}
""")
    if autobuy == True and cookie >= 100:
        cookie -= 100
        click += 1
        sys("clear")
    if autoR == True and cookie >= 3000:
        cookie = 0
        click += 30
    if cookie <= -1:
        sys("clear")
        print("wtf u have negative Cookies????")
        exit()
    print("Type 'store' for Store\nCookies:", cookie, "\nClicks =", click)
    if chance:
        print("Chance for Double: ", max)
    user = str(input()).lower()
    if user == "":
        if chance:
            if max != 1:
                doubles = randint(1,max)
                if doubles == 1:
                    cookie += click
            else:
                cookie += click
        cookie += click
        sys("clear")
    elif user == "store":
        print("Say 'B' to Buy clicks for 100 cookies.\nOr, say 'R' to reset but with a big boost for 3,000.\nOr buy a chance for a click to be worth double for 500 by typing\n'autoC' LOW NUMBER IS GOOD.\nOr say 'AutoB' to toggle auto buy Clicks.\noreo or ord Say 'AutoR' to toggle auto buy Reset")
        Suser = str(input(': ')).lower()
        if Suser == "b" and cookie >= 100:
            cookie -= 100
            click += 1
            sys("clear")
        elif Suser == "r" and cookie >= 3000:
            cookie = 0
            click += 30
            sys("clear")
        elif Suser == "autob" and autobuy == False:
            autobuy = True
            sys("clear")
        elif Suser == "autob" and autobuy == True:
            autobuy = False
            sys("clear")
        elif Suser == "autor" and autoR == False:
            autoR = True
            sys("clear")
        elif Suser == "autor" and autoR == True:
            autoR = False
            sys("clear")
        elif Suser == "autoc" and cookie >= 500:
            cookie -= 500
            chance = True
            max -= 1
        else:
            sys("clear")
    elif user == "debug":
        debug = True
    else:
        print("Just press Enter")
        slp(0.4)
        sys("clear")
sys("clear")
print(". . .")
slp(4)
print("So...\n\nYou got 1,000,000 or more...")
slp(5)
print("Do you have a life?  . . .\n\nAre you... Ok?")
slp(4)
print("do u have a Cookie addiction???")