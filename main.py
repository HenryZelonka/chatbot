#imports
from time import sleep as s
import sys
import parser

#----------------------------------------------------------

#functions

#scrolly text
def scroll(string):
  for letter in string:
    print(letter, end = "")
    sys.stdout.flush()
    s(0.05)

#----------------------------------------------------------

# main program

#introduction
scroll("Hello, I am a chatbot programmed by Henry Zelonka.\nWhat would you like to talk about?\n\n")

while True:
  userInput = input()
  parser.parse(userInput)
