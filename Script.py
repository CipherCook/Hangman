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

#welcoming the user
name1 = input("Player 1, What is your name?")

print("hello " + name1)

name2= input("Player 2, what is your name?")
print("hello  ",name2)
time.sleep(1)
print ("Start guessing...")

def get_secret_word():

    random_wordbank = ["lemon","orange","grapefruit","apple","lychee","pear","banana","melon","watermelon","honey"] #word bank of potential secret words
    pick_word = random.randint(0, len(random_wordbank)-1) #choose a random integer in range of wordbank length to use as the secret word
    return random_wordbank[pick_word]

secret= get_secret_word()

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
    
turns = 7
getvowels(secret)
p1=7
p2=7
#if a movie has a longer title the person guessing wud gain unnecessary adv on the points, so, instead, counting number of mistakes.
#hence, the person who guesses the movie with fewer mistakes gets more points!
while (turns>0):
    guess= input("enter a character")
    if guess in secret:
        print(";)")
        printword(secret, secret, guess)#to change
    else:
        p1-=1
        deathstate+=1
        hang(deathstate)
        turns-=1
if p1 == 0:
    print("You lost, NO POINTS FOR YOU :(")
elif p1 == 1:
    print("Making so many mistakes cost you, cost = 6 points to be exact \n" ,"final points = 1")
elif p1 == 2:
    print("Making so many mistakes cost you, cost = 5 points to be exact \n" ,"final points = 2")
elif p1 == 3:
    print("Making so many mistakes cost you, cost = 4 points to be exact \n", "final points = 3")
elif p1 == 4:
    print("only 3 wrong guesses.... impressive \n" ,"final points = 4")
elif p1 == 5:
    print("only 2 wrong guesses.... impressive \n", "final points = 5")
elif p1 == 6:
    print("only 1 wrong guess.... Bravo! \n", "final points = 6")
elif p1 == 7:
    print("Legend said it cudnt be done, yet here you are making no mistakes ......\n", "YOU ARE AWARDED (7+1) POINTS :)" )
#made lil changes :)        
         
     
        
        
