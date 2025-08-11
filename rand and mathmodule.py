#activity 1
import random
playing = True
number = str(random.randint(10,20))
print("i will generate a numbr from 10 to 20, and you have to guess the number one digit at a time")

while playing:
    guess = input("give me your best guess! \n")
    if number == guess:
        print("you win the game")
        print("the number was", number)
        break
    
    else:
        print("your guess isn't quite right, try again. \n")

#activity 2
import random

while True:
    user_action = input("enter a choice(rock, paper, scissors)")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\n You chose{user_action}, computer chose{computer_action}.\n")
    
    if user_action==computer_action:
        print(f"both players selected {user_action}. it's a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes the scissors, you win")
        else:
            print("paper covers rock, you loose")        
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock, you win")
        else:
            print("scissors cuts the paper, you loose") 
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts the paper, you win")
        else:
            print("rock smashes the scissors, you loose")
    
    play_again = input("play again? (y / n):") 
    if play_again != "y":
        break
    
#activity 3
import math

print('the floor and cieiling value of 23.56 are:'+str(math.ceil(23.56))+',' + str(math.floor(23.56)))

x= 10
y= -15
print('the value of x after copying the sign of y is:'+ str(math.copysign(x,y)))

print('absolute value of - 96 and 56 are:' + str(math.fabs(-96)) + str(math.fabs(56)))

print('the gdc of 24 and 56:' + str(math.gcd(24, 56)))