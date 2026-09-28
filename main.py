import random

Easy_turns = 10
Hard_turns = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
       return Easy_turns
    else:
        return Hard_turns

def check_answer(user_guess, actual_answer, turns):
        """Compares guess with actual answer and returns remaining turns."""
        if user_guess > actual_answer:
            print("You guessed too high.")
            return turns - 1
        elif user_guess < actual_answer:
            print("You guessed too low.")
            return turns - 1
        else:
            print(f"You got it! The answer was {actual_answer}.")
            return turns
def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  answer = random.randint(1, 100)
  turns = set_difficulty()
  guess = 0

  while guess != answer and turns > 0:
    print(f"\nYou have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)

    if turns == 0 and guess != answer:
      print(f"You've run out of guesses! The number was {answer}. You lose.")


game()
