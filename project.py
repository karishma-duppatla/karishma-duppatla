import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input("enter Rock/paper/Scissors or q for quit ").lower()
    if user_input=="q":
        break
    
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_input=options[random_number]
    print("computer picked",computer_input+".")
    if(user_input=="paper" and computer_input=="rock"):
        print("You won!")
        user_wins+=1
    elif (user_input=="rock" and  computer_input=="Scissors"):
        print("You won!")
        user_wins+=1
    elif (user_input=="Scissors" and computer_input=="paper"):
        print("You won!")
        user_wins+=1 
    elif(user_input==computer_input):
        print("Its not Considered choose another one..")
    else:
        print("You lost! Better luck next time...")
        computer_wins+=1 
print("you won",user_wins,"times.")
print("computer won",computer_wins,"times.")
print("you exit! Thanks for playing")