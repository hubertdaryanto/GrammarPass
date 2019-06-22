import subprocess as sub
from time import sleep
from tkinter import filedialog
import tkinter as tk
from tkinter import *
from modul.menu import menu_1, menu_2

p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()


def checkfile():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("docx files","*.docx"),("all files","*.*")))
    menu_1(window.filename)

def inputdictionary():
    def closeinputdictionary():
        typed_word = e1.get()
        menu_2(typed_word)
        inputwindow.destroy()
    inputwindow = Tk(className='Input Dictionary')
    input = StringVar()
    e1 = Entry(inputwindow, textvariable = input)
    e1.grid(row = 0, column = 0)
    b7 = Button(inputwindow, text = "OK", width = 12, command = closeinputdictionary)
    b7.grid(row = 0, column = 1)
    inputwindow.mainloop()

def close():
    window.destroy()
#create window object
window = Tk(className='GrammarPass')

#define four labels
'''
li = Label(window, text= "Title")
li.grid(row = 0,column = 0)

li = Label(window, text = "Author")
li.grid(row = 0, column = 2)

li = Label(window, text = "Year")
li.grid(row = 1, column = 0)

li = Label(window, text = "ISBN")
li.grid(row = 1, column = 2)
'''

# #define Entries
'''
title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)
'''

#define ListBox
list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 0, column = 0, rowspan = 6, columnspan = 2)
list1.insert(END, output)

#attach scrollbar to tohe list
sb1 = Scrollbar(window)
sb1.grid(row = 0, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#Define buttons
b1 = Button(window, text = "Check a sentence from docx", width = 30, command = checkfile)
b1.grid(row = 0, column = 3)

b2 = Button(window, text = "Input new dictionary data", width = 30, command = inputdictionary)
b2.grid(row = 1, column = 3)

b3 = Button(window, text = "Check Grammar", width = 30)
b3.grid(row = 2, column = 3)

"""
b4 = Button(window, text = "Update Selected", width = 12)
b4.grid(row = 3, column = 3)

b5 = Button(window, text = "Delete Selected", width = 12)
b5.grid(row = 4, column = 3)
"""
b6 = Button(window, text = "Close", width = 30, command = close)
b6.grid(row = 5, column = 3)


window.mainloop()