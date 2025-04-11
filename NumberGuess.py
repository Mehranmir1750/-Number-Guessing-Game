from random import randint
#from art import logo

easy_level = 10
hard_level = 5

def choose_level():
    level = input("Choose a difficulty.Type 'easy' or 'hard':").islower()

    if level =='easy':
        return easy_level
    elif level == 'hard':
        return hard_level
    else:
        print("invalid option")

def check_answer(user_guess, actual_answer, turns):

    if user_guess>actual_answer:
        print("Too High")
        return turns-1
    elif user_guess<actual_answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it! The answer was {actual_answer}")


def game():
#    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(f"the answer is {answer}")

    turns = choose_level()

    guess = 0
    while guess!= answer:
        print(f"you have {turns} attempts to guess! ")
        guess = int(input("Make a guess:"))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
        return
    elif guess != answer:
        print("Guess again.")

