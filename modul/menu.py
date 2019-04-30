from modul.readFile import readFile
from modul.docChecker import checkThis
import os


def menu_1():
    sentence = readFile()
    checkThis(sentence)
    input()


def menu_2():
    newWord = str(input("Input a new word: "))
    newWord = "\n" + newWord
    file = open("modul\\linuxwords.txt", 'a')
    file.write(newWord)
    file.close()


def printMenu():
    chooseMenu = 0
    os.system('cls')
    print("1. Get a file")
    print("2. Input new dictionary data")
    print("3. Exit")
    chooseMenu = int(input(">> "))
    return chooseMenu


def callMenu(number):
    if (number == 1):
        menu_1()
    elif(number == 2):
        menu_2()
    elif(number == 3):
        print("thankyou")
