from nltk.tokenize import word_tokenize
from spellcheck import is_spelled_correctly
from nltk.corpus import stopwords
import docx2txt
import os


def menu_1():
    i = 0
    sentence = str(input("Input your sentence: "))
    values = word_tokenize(sentence.lower())
    ready = [word for word in values if word not in english]
    for value in ready:
        if not is_spelled_correctly(value):
            print("NOT SPELLED CORRECTLY: " + value)
            i = i + 1
    if(i == 0):
        print("Checked Done! Nothing wrong.")
    input()


def menu_2():
    newWord = str(input("Input a new word: "))
    newWord = "\n" + newWord
    file = open("linuxwords.txt", 'a')
    file.write(newWord)
    file.close()


def printMenu():
    chooseMenu = 0
    os.system('cls')
    print("1. Check a sentence")
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


english = set(stopwords.words('english'))
