#add functions for now ignore the dullness
import tkinter as tk
import random
import time
deathstate = 0

def hang(deathstate):
    import turtle
    
    m = turtle.Turtle()
    j = turtle.Screen()
    j.bgcolor("yellow")
    m.color("blue")
    m.speed(10)
    
    if deathstate == 1:
        
        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        
        m.ht()
        
    elif deathstate == 2:
        
        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        [m.fd(100) , m.rt(90) , m.fd(40) , m.rt(90)]
        
        m.ht()
        
    elif deathstate == 3:
        
        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        [m.fd(100) , m.rt(90) , m.fd(40) , m.rt(90)]
        [m.circle(20)]
        
        m.ht()
        
    elif deathstate == 4:
        
        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        [m.fd(100) , m.rt(90) , m.fd(40) , m.rt(90)]
        [m.circle(20)]
        [m.lt(90) , m.pu() , m.sety(100) , m.pd() , m.fd(55)]
        
        m.ht()

    elif deathstate == 5:
        
        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        [m.fd(100) , m.rt(90) , m.fd(40) , m.rt(90)]
        [m.circle(20)]
        [m.lt(90) , m.pu() , m.sety(100) , m.pd() , m.fd(55)]
        [m.rt(180) , m.fd(40) , m.rt(90) , m.fd(25) , m.rt(180) , m.fd(50)]
        
        m.ht()


    elif deathstate == 6:

        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        [m.fd(100) , m.rt(90) , m.fd(40) , m.rt(90)]
        [m.circle(20)]
        [m.lt(90) , m.pu() , m.sety(100) , m.pd() , m.fd(55)]
        [m.rt(180) , m.fd(40) , m.rt(90) , m.fd(25) , m.rt(180) , m.fd(50)]
        [m.rt(180) , m.fd(25) , m.rt(90) , m.fd(40) , m.rt(50) , m.fd(25) , m.rt(180) , m.fd(25) , m.rt(80) , m.fd(25)]
        
        m.ht()

    elif deathstate == 7:

        [m.pu() , m.setx(0) , m.sety(0) , m.pd()]
        [m.fd(100) , m.rt(180) , m.fd(50) , m.rt(90) , m.fd(180) , m.rt(90)]
        [m.fd(100) , m.rt(90) , m.fd(40) , m.rt(90)]
        [m.circle(20)]
        [m.lt(90) , m.pu() , m.sety(100) , m.pd() , m.fd(55)]
        [m.rt(180) , m.fd(40) , m.rt(90) , m.fd(25) , m.rt(180) , m.fd(50)]
        [m.rt(180) , m.fd(25) , m.rt(90) , m.fd(40) , m.rt(50) , m.fd(25) , m.rt(180) , m.fd(25) , m.rt(80) , m.fd(25)]
        [m.pu() , m.setx(145) , m.sety(125) , m.pd() , m.circle(2) , m.pu() , m.setx(160) , m.sety(125) , m.pd() , m.circle(2),
         m.pu() , m.setx(140) , m.sety(103.5) , m.pd() , m.write("loser")]
        
        m.ht()


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

secret= get_secret_word()
turns = 7
fails=0    
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
        hang(deathstate)
    turns-=1
print("you scored ", p1)
        
         
     
        
        
