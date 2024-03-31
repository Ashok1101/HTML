#!C:/Users/Arvind/anaconda3/python
print ("Content-Type: text/html\n\n")
print()
import cgi,os
print("hello world")
form=cgi.FieldStorage()
n=56
no_of_guesses=1
print("you will get only 9 chances:")
while(no_of_guesses<=9):
    guess=int(input('Guess the number :'))
    if(guess == 56):
        print("You won!")
        print(no_of_guesses,"number of guesses you took to finish!")
        break
    elif(guess>=50 and guess<=60):
        print("you are too close to number")
    elif(guess<50):
        print("you guessed too small number.")
    else:
        print("you guessed too large number.")
    no_of_guesses+=1
if(no_of_guesses>9):
    print("Game Over")