import tkinter as tk
import time
import turtle
import getpass

j = turtle.Screen()


# ALL FUNCTIONS:

# HANGMAN animation
def hang(deathstate):
    m = turtle.Turtle()
    j.bgcolor("#ffcc00")
    m.color("blue")
    m.speed(10)

    if deathstate == 1:

        [m.pu(), m.setx(0), m.sety(0), m.pd()]
        [m.fd(100), m.rt(180), m.fd(50), m.rt(90), m.fd(180), m.rt(90)]

        m.ht()

    elif deathstate == 2:
        [m.pu(), m.setx(0), m.sety(0), m.pd()]
        [m.fd(100), m.rt(180), m.fd(50), m.rt(90), m.fd(180), m.rt(90)]
        [m.fd(100), m.rt(90), m.fd(40), m.rt(90)]

        m.ht()

    elif deathstate == 3:
        [m.pu(), m.setx(0), m.sety(0), m.pd()]
        [m.fd(100), m.rt(180), m.fd(50), m.rt(90), m.fd(180), m.rt(90)]
        [m.fd(100), m.rt(90), m.fd(40), m.rt(90)]
        [m.circle(20)]

        m.ht()

    elif deathstate == 4:
        [m.pu() , m.setx(0) , m.sety(0), m.pd()]
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
        m.speed(20)
    
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

# Main Function
def main(secret,player):
    getvowels(secret)
    vow=('a','e','i','o','u')
    while(secret in vow):
        print("Please enter a movie name with atleast one consonant")
        secret = input()
        getvowels(secret)

    deathstate,turns,guesses = 0,7,""

    while (turns>0):
        guess= input("Enter a character ")
        
        
        
        if guess in vow:
            print("all vowels are already disclosed, try something else!!")
        elif guess in guesses:
            print("You have already tried this letter, Please try again")
        elif len(guess)!= 1:
            print("ONLY 1 LETTER can be guessed at once!!")
        elif guess not in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'):
            print("You can only guess using EITHER consonants OR numbers!")
        else:
            print('\n')
            time.sleep(1)
            guesses += str(guess)
            if guess in secret:
                print("You Guessed it!")
                final=""
                sec=""
                add=('a','e','i','o','u')
                for i in secret:
                    if i in add:
                        sec += i + " "
                        final += i
                    elif i == " ":
                        sec += "/"
                        final+= " "
                    elif i in guesses:
                        sec += i + " "
                        final += i
                    else:
                        sec += "_ "
                    print(" ", end= " ")
                if final == secret:
                    print(sec)
                    print("YOU GUESSED THE MOVIE!")
                    break
                else:
                    print(sec)
                    print("Keep the Momentum Going!")
            else:
                player-=1
                deathstate+=1
                turns-=1
                print("No  of lives remaining = ", 7-deathstate)
                if deathstate < 4:
                    print("oww, better luck next time")
                elif deathstate < 6:
                    print("USE REMAINING CHANCES WISELY")
                elif deathstate < 7:
                    print("only YOU can save HIM.....")
                hang(deathstate)
    if player == 0:
        print("\n\nYou lost, NO POINTS FOR YOU :( \n The name of the movie was :", secret)
    elif player == 1:
        print("\n\nMaking so many mistakes cost you, cost = 6 points to be exact \n" ,"Final Point = 1")
    elif player == 2:
        print("\n\nMaking so many mistakes cost you, cost = 5 points to be exact \n" ,"Final Points = 2")
    elif player == 3:
        print("\n\nMaking so many mistakes cost you, cost = 4 points to be exact \n", "Final Points = 3")
    elif player == 4:
        print("\n\nonly 3 wrong guesses.... impressive \n" ,"Final Points = 4")
    elif player == 5:
        print("\n\nonly 2 wrong guesses.... impressive \n", "Final Points = 5")
    elif player == 6:
        print("\n\nONLY 1 MISTAKE?!?! Bravo! \n", "Final Points = 6")
    elif player == 7:
        print("\n\nLegend said it cudnt be done, yet here you are making HISTORY ......\n", "YOU ARE AWARDED 7 POINTS , HECK FINAL POINTS = 8,:)" )

        
# convert movie into code   
def getvowels(secret):
    sec=""
    vow=('a','e','i','o','u')
    for i in secret:
        if i in vow:
            sec += i + " "
        elif i == " ":
            sec += "/"
        else:
            sec += "_ "
        print(" ", end= " ")
    print(sec)
    
# ALL FUCNTIONS USED HAVE BEEN DEFINED
    
# DRIVER CODE
# p1's turn
flag=1
while(flag==1):            
    name1 = input("Player 1, What is your name? ")
    print("Hello ", name1)

    name2= input("Player 2, What is your name? ")
    print("Hello  ",name2)

    print(name1,", You have been awarded the chance to go first!")
    a = 0

    while a == 0:
        
        b = ""
        secret1 = getpass.getpass("Enter a movie: \n*the movie name will remain hidden due to obvious reasons!!* \n ")
        
        for i in secret1:
            
            if i not in ("abcdefghijklmnopqrstuvwxyz 0123456789"):
                print("ENTER ONLY ALPHABETS OR NUMBERS, CHARACTERS ARE NOT ALLOWED! /n")
                break
            else:
                b += i
                
        if len(secret1) == len(b):
            a =  1
        else:
            a = 0
            
    print ("Your time to guess the movie Begins!!", name2)

    p1=7
    main(secret1,p1)

    # p1's turn has ended!

    # p2 is starting now
    print("\n\nNow its your turn,", name2, " show ", name1, " Whose the boss!!!")

    a = 0

    while a == 0:
        
        b = ""
        secret2 = getpass.getpass("Enter a movie: \n*the movie name will remain hidden due to obvious reasons!!* \n ")
        
        for i in secret2:
            
            if i not in ("abcdefghijklmnopqrstuvwxyz 0123456789"):
                print("ENTER ONLY ALPHABETS OR NUMBERS, CHARACTERS ARE NOT ALLOWED! /n")
                break
            else:
                b += i
                
        if len(secret2) == len(b):
            a =  1
        else:
            a = 0
    print ("Your time to guess the movie Begins!!", name1)

    j.clear()

    p2 = 7
    main(secret2,p2)

    # p2's turn has ended!
    print("Let's see who won...")
    time.sleep(1)
    print("DRUMROLL................")
    time.sleep(5)
    if(p1>p2):
        print(name1," has won!")
    elif(p2<p1):
        print(name2," has won!")
    else:
        print("you deserve another round because it looks like A TIE!")
    print("WANT ANOTHER ROUND? type'y' to continue and 'n'to quit")
    inp=0
    while(inp==0):
        loo=input()
        print(loo)
        if loo=='y'or loo=='Y':
            flag=1
            inp=1
        elif loo=='n' or loo=='N':
            flag=0
            inp=1
        else:
            print("Learn to type you dumbo")
            inp=0
    print(flag)
    if flag==0:
        print("see ya later")

# vowelonly as amovie name
# case sensitivity
# audio and bgcolor for deaths
# grammar typos

# round1 completed!

# IMPORTANT DATA TO BE TRANSFERRED TO MYSQL
# [TIME ELEMENT, HINT ELEMENT, ALL OF TKINTER] = LEFT
# THIS CODE AFTER COMPLETION IS THEN TO BE LOOPED
# DEFINITELY NOT MAKING SO MANY NOTES SO WE CAN REACH 500 LINES OF CODE FASTER. DEFINITELY, MAYBE.

