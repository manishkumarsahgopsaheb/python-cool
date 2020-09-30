# ----------random module------------

# import random
#       choice method of random module is used to pick the random item from the list

# my_list = ['pubg', 'free fire', 'counter strike', 'ludo']
# r = random.choice(my_list)
# print(r)
# print(dir(r))

#       random module is used to generate the random  number in a particular range

# num = random.randint(1, 6)
# print(num)

# Program to solve the tossing problem like who win the toss and wins
# def tossing_game():
#     import random
#     l = []
#     print("Enter names of Players --")
#     print("Press 0 if done")
#     while True:
#         names = input()
#         l.append(names)
#         if names == "0":
#             break
#     winner = random.choice(l)
#     print("Winner is : ", winner)
#
# tossing_game()

# -----------calender module-------------

# import calendar
#
# print('your calender\n\n')
#
# y = int(input('enter the year'))
# m = int(input('enter the month'))
#
# mycalender = calendar.month(y, m)
#
# print('\n', mycalender)

# year = int(input("enter the year"))
# i = int(calendar.isleap(year))
# if i==1:
#     print("is leap")
# else:
#     print("not leap year")


# ----------platform module---------------

# import platform
#
# my_sys = platform.system()
# print("system is: ", my_sys)
#
# print("processor is: ", platform.processor())
# print("architechture is: ", platform.architecture())
# print("compiler is: ", platform.python_compiler())
# print("python version is: ", platform.python_version())


# --------------datetime module---------------

# import datetime
#
# x = datetime.datetime.now()
# print(x)
#
# print(x.year)
#
#           use of strftime() method
#
# print(x.strftime("%A"))
#
#           creating a date object
#
# date_obj = datetime.datetime(2020, 9, 29)
# print(date_obj)


# ------------time module---------------------

# import time
#
# print("this is printed immediately.")
# time.sleep(2.4)
# print("this is printed after 2.4 seconds")


# -------------math module------------------
# import math

# num = int(input('enter the number'))
# sol = math.factorial(num)
# print("Factorial:", sol)

# h = math.fsum([2,30,4,30,34])
# print(h)


# ----------------------turtle module-----------------

# import turtle
#
# abhi = turtle.Turtle()
# abhi.speed(0)
# abhi.color("green", "yellow")  # this is for colour
# abhi.begin_fill()
#
# for i in range(100):
#     abhi.forward(200)
#     abhi.left(168.5)
#     abhi.forward(200)
#     abhi.left(175)
#
# abhi.penup()
# abhi.forward(200)
# abhi.pendown()
# for i in range(100):
#     abhi.forward(200)
#     abhi.left(168.5)
#     abhi.forward(200)
#     abhi.left(175)
#
# abhi.end_fill()
#
# abhi = turtle.Turtle()
# abhi.color("cyan", "green")
# abhi.begin_fill()
# abhi.forward(100)
# abhi.left(90)
# abhi.forward(100)
# abhi.left(90)
# abhi.forward(100)
# abhi.left(90)
# abhi.forward(100)
#
# abhi.penup()
# abhi.forward(100)
# abhi.pendown()
#
# abhi.forward(100)
# abhi.setheading(90)
# abhi.forward(100)
# abhi.left(90)
# abhi.forward(100)
# abhi.left(90)
# abhi.forward(100)
# abhi.left(90)
# abhi.forward(100)
# abhi.end_fill()
#
# turtle.done()

# --------------------numpy module-----------------

# import numpy as np
#
# a1 = np.arange(1, 10)
# print(a1)

# --------------pandas module------------------------

# import pandas as pd
#
# n1 = pd.Series({'KARAN': 42, 'PRITESH': 44, 'JATIN': 45, 'ROSHAN': 46})
# print(n1)
#
# dict = {
#     "State": ['Andhra Pradesh', 'Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu'],
#     "Capital": ['Hyderabad', 'Mumbai', 'Bengaluru', 'Trivandrum', 'Chennai'],
#     "Literacy %": [89, 77, 82, 97,85],
#     "Avg High Temp(c)": [33, 30, 29, 31, 32]
# }
#
# print(pd.DataFrame(dict))

# ---------------pyautogui module for taking screenshot-----------------------

# import pyautogui
#
# screenshot = pyautogui.screenshot()
# screenshot.save("screenpic.png")

# --------------playsound module for playing sound------------------

# import playsound
#
# playsound('C:\Users\hp\Desktop\mm.mp3')

# --------------------wikipedia module---------------------

# import wikipedia
#
# result = wikipedia.page("Steve Jobs")
# print(result.summary)

#       TO GET PERTICULAR SENTENCE IN THE SUMMARY

# print(wikipedia.summary("Jobs become", sentences=1))

# ----------for listening to sound-----------------------------

# import pyttsx3 as pyttsx3
#
# Engine = pyttsx3.init()
# Engine.say("I am speaking")
# Engine.RunAndWait()

# ----------------JSON module------------convert from json to python, and the result will be the
# dictionary------------------

# import json

# x = '{"name":"john", "age":30, "city":"New York"}'

# converting from Json to python dictionary
# y = json.loads(x)

#  here y is a dictionary type
# print(type(y))
#
# print(y["age"])

# -------------converting from python to JSON-------------------
# we can convert the python object into a JSON string by using the------- json.dumps() method-----------.
# lets create a python object dict

# dict_python = {
#     "name": 'John',
#     "age": '30',
#     "city": 'New York'
# }

# convert into Json

# js = json.dumps(dict_python)
# print(js)


# ---------------------Python RegEx module---------------------------------

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#
# RegEx can be used to check if a string contains the specified search pattern.

# import re

# txt = "the rain in spain"
#
# x = re.search("^the.*spain$", txt)
#
# print(x)
#
# if x:
#     print("yes! we have a match!")
# else:
#     print("no match")

# ---------------re.findall("substring", string) this will return the
# list which will contain all the substring. so if someone ask to find the count of
# any substring in a string then we can answer it by printing the length of list--------------

# srch_substr = re.findall("ai", txt)
# print(srch_substr)
# print(len(srch_substr))

# -----------search() function searches the string for a match, and returns a
# match object if there is match and return None if there is not any match

# srch = re.search("\s", txt)  # \s is used for space character
#
# print(srch)
#
# srch_item = re.search("rain", txt)
# print(srch_item)

# ---------------------split() function----------
# The split() function returns a list where the string has been split
# at each match:

# let me program for split at each white space character

# split_item = re.split("\s", txt)

# if i will print split_item it will print the list, so if someone ask to
# print the count of words in a string then we can split the whole string
# at each white space and print the count of total item in list or the
# length of the string

# print(split_item)

# for printing each word, splited at white space

# for i in split_item:
#     print(i)

# printing count of words splited at white space
# print(len(split_item))


# ---------------sub function------------------
# the sub() function replaces the matches with the text of your choice

# Replace every white-space character with the number 9:

# txt = "the rain in spain"
# replace_text = re.sub("\s", "9", txt)
# print(replace_text)

# we can control the number of replacements by specifying
# the count parameter:

# Replace the first 2 occurrences:
# replace_txt = re.sub("\s", "9", txt, 2)
# print(replace_txt)
