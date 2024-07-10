import random

user_score = 0
computer_score = 0

options = ["rock" , "paper", "scissors"]

print("Welcome to Rock Paper Scissors!".center(100))

while True:
    user = input("enter your choice : (rock , paper , sissors or q for quit) ")
    if user == 'q':
        print("Thank you for playing".center(100))
        break
    
    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    
    if  user.lower() == computer_pick.lower():
        print("\nIt's a tie !")
        
    elif user == "rock" and computer_pick == "scissors":
        user_score +=1
        print('\nYou win this round')
    
    elif user == "scissors" and computer_pick == "paper":
        user_score+=1
        
    elif user == "paper" and computer_pick == "rock":
        user_score+=1
        
    else:
        print("you lost") 
        computer_score+=1
        
    print("you won" , user_score , "times")
    print("computer won" , computer_score , " times")      
        

    