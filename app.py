import random

# Create an array with rock, paper and scissors
options = ['rock', 'paper', 'scissors']

# Create a function that randomly selects one of the the three options
def computer_choice():
    return random.choice(options)

# Create a function that asks the user for their choice
def user_choice():
    return input('Choose rock, paper or scissors: ')

# Create a function that compares the user's choice with the computer's choice
def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return 'You win!'
    elif user_choice == 'rock' and computer_choice == 'paper':
        return 'You lose!'
    elif user_choice == 'paper' and computer_choice == 'rock':
        return 'You win!'
    elif user_choice == 'paper' and computer_choice == 'scissors':
        return 'You lose!'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return 'You win!'
    elif user_choice == 'scissors' and computer_choice == 'rock':
        return 'You lose!'
    else:
        return 'Invalid choice!'
# Create a function that prints the results
def print_results(result):
    print(result)

# Create a function that asks the user if they want to play again
def play_again():
    return input('Do you want to play again? (yes/no): ')

# Create a function that prints the final results
def print_final_results(user_wins, computer_wins):
    print(f'You won {user_wins} times and the computer won {computer_wins} times.')

# Create a function that runs the game
def run_game():
    user_wins = 0
    computer_wins = 0
    while True:
        user = user_choice()
        computer = computer_choice()
        result = compare_choices(user, computer)
        print_results(result)
        if result == 'You win!':
            user_wins += 1
        elif result == 'You lose!':
            computer_wins += 1
        play = play_again()
        if play == 'no':
            break
    print_final_results(user_wins, computer_wins)

# Run the game
run_game()