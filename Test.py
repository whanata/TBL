#Python 3.4

import random

def main():
    play = None
    quoteNumber = 0

    print("*****Press enter to continue each step*****\n")

    name = input("Please type your name: ")
    print("Hi %s" % (name))
    inspirationalQuote()
    print("Do you want to play a game? (Y/N)")
    play = decidePlayGame()

    #to keep windows open
    print("\n*****Press enter to exit program*****")
    input()

def decidePlayGame():
    flag = False
    playGame = None

    while flag == False:
        decision = str.upper(input(">> "))
        if decision == "Y":
            print("Cool lets get into it then")
            flag = True
            playGame = True
        elif decision == "N":
            print("Well, you playing anyway")
            flag = True
            playGame = False

    return playGame

def inspirationalQuote():
    greeting = "\nHere is your daily inspirational quote: \n"
    quotes = ["Wira"
        , "Wira2"
        , "Wira3"
        , "Wira4"
        , "Wira5"
        , "Wira6"
        , "Wira7"
        , "Wira8"
        , "Wira9"
        , "Wira10"]
    inspirationalQuote = quotes[random.randint(0, 9)]

    input(greeting + inspirationalQuote)

main()
