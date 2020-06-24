#add functions for now ignore the dullness
import tkinter as tk
import random
deathstate = 0
def display1():
    #tkinter code for starting animation
    while gameon==True:
        if deathstate==1:
            #tk for hangman state 1
            print()
            #proceed similarly for 7 states of death of hangman
        
    if gameon==False:
        print()
        #ending display
        #restart?
import time

#welcoming the user
name1 = input("Player 1, What is your name?")

print("hello " + name1)

name2= input("Player 2, what is your name?")
print("hello  ",name2)
time.sleep(1)
print ("Start guessing...")
#call display 1 bumblebee
gameon = True

def get_secret_word():

    random_wordbank = ["lemon","orange","grapefruit","apple","lychee","pear","banana","melon","watermelon","honey"] #word bank of potential secret words
    pick_word = random.randint(0, len(random_wordbank)-1) #choose a random integer in range of wordbank length to use as the secret word
    return random_wordbank[pick_word]

secret= get_secret_word()
turns = 7
fails=0
def getvowels(secret):
    vow=['a','e','i','o','u']
    for i in secret:
        if i in vow:
            print(i, end=" ")
        else:
            print("__", end=" ")
        print(" ", end= " ")

    print("\n")
def printword(secret, lastword, guess):
    print()# TO DO such that it adds the guessed character to lastword if guess matches with secret and output is our new lastword
getvowels(secret)
p1=0
p2=0
while (turns>0):
    guess= input("enter a character")
    if guess in secret:
        p1+=5
        print(";)")
        printword(secret, secret, guess)#to change
    else:
        p1-=1
        deathstate+=1
    turns-=1
print("you scored ", p1)
        
         
     
        
        
