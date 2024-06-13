import random
from termcolor import colored
from colorama import init

# Initialize colorama
init()

# Function to load words from a file
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = [word.strip().upper() for word in file.readlines()]
    return words

# Function to get feedback on the user's guess
def get_feedback(secret_word, guess):
    feedback = []
    used_indices = set()
    
    # First, mark the correct letters (correct position)
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback.append((guess[i], 'correct'))
            used_indices.add(i)
        else:
            feedback.append((guess[i], 'wrong'))
    
    # Then, mark the correct letters (wrong position)
    for i in range(len(guess)):
        if feedback[i][1] == 'wrong' and guess[i] in secret_word:
            for j in range(len(secret_word)):
                if guess[i] == secret_word[j] and j not in used_indices:
                    feedback[i] = (guess[i], 'misplaced')
                    used_indices.add(j)
                    break

    return feedback

# Function to print the feedback with colored boxes
def print_feedback(feedback):
    for char, status in feedback:
        if status == 'correct':
            print(colored(f' {char} ', 'white', 'on_green'), end=' ')
        elif status == 'misplaced':
            print(colored(f' {char} ', 'white', 'on_yellow'), end=' ')
        else:
            print(colored(f' {char} ', 'white', 'on_grey'), end=' ')
    print()

# Main game function
def play_wordle():
    word_list = load_words('words.txt')
    secret_word = random.choice(word_list)
    attempts = 10
    print("Welcome to Wordle! Guess the 5-letter word.")

    while attempts > 0:
        guess = input("Enter your guess: ").strip().upper()
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        feedback = get_feedback(secret_word, guess)
        print_feedback(feedback)

        if guess == secret_word:
            print(colored("Congratulations! You've guessed the word!", 'white', 'on_green'))
            break

        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")

    if attempts == 0:
        print(colored(f"Sorry, you've run out of attempts. The word was: {secret_word}", 'white', 'on_red'))

# Run the game
if __name__ == "__main__":
    play_wordle()