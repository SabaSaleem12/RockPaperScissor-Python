import random      #Importing the random module to generate random choices for the computer
game_list = ["rock", "paper", "scissor"]  #List of possible choices

user_choice = input("Enter your choice (rock, paper, scissor): ").lower()  #Taking user input and converting it to lowercase
computer_choice = random.choice(game_list)  #Randomly selecting a choice for the computer from the game_list
print("user choice: ", user_choice)  #Displaying user's choice
print("computer choice: ", computer_choice)  #Displaying computer's choice

if user_choice == computer_choice:  #Checking if both choices are the same
    print("It's a tie!")  #If they are the same, it's a tie

elif user_choice == "rock":  #If user chooses rock
    if computer_choice == "scissor":  #If computer chooses scissor
        print("You win!")  #User wins
    else:  #If computer chooses paper
        print("Computer wins!")  #computer wins

elif user_choice == "paper":  #If user chooses paper
    if computer_choice == "rock":  #If computer chooses rock
        print("You win!")  #User wins
    else:  #If computer chooses scissor
        print("Computer wins!")  #computer wins

elif user_choice == "scissor":  #If user chooses scissor
    if computer_choice == "paper":  #If computer chooses paper
        print("You win!")  #User wins
    else:  #If computer chooses rock
        print("Computer wins!")  #computer wins