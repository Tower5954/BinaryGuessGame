from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and one million!")
computer_number = random.randint(1,100000)

level = input("Choose a difficulty.\n Type 'easy' or 'hard':\n")

def hard_level():
  global computer_number
  lives = 10
  print("You have 10 attempts to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == computer_number:
    return f"Well Played, you guessed {computer_number} correctly" 
  while lives > 0 and guess != computer_number:
    if guess < computer_number:
      print("Higher")
      lives -= 1
      print(f"You have {lives} attempts left")
      guess = int(input("Guess again: "))
    elif guess > computer_number:
      print("Lower")
      lives -= 1
      print(f"You have {lives} left")
      guess = int(input("Guess again: "))
    
  if guess == computer_number:
      print(f"Well Played, you guessed {computer_number} correctly") 
  
def easy_level():
  global computer_number
  lives = 20
  print("You have 20 attempts to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == computer_number:
    return f"Well Played, you guessed {computer_number} correctly" 
  while lives > 0 and guess != computer_number:
    if guess < computer_number:
      print("Higher")
      lives -= 1
      print(f"You have {lives} attempts left")
      guess = int(input("Guess again: "))
    elif guess > computer_number:
      print("Lower")
      lives -= 1
      print(f"You have {lives} left")
      guess = int(input("Guess again: "))
    
  if guess == computer_number:
      print(f"Well Played, you guessed {computer_number} correctly")     
    
    

if level == "easy":
  easy_level()
else:
  hard_level()





