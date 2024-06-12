import art
import random
print(art.logo)
random_number = random.choice(range(1,101))
print(random_number)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
  number_of_attempts = 10
elif level == "hard":
  number_of_attempts = 5
guess_again = 0
print("Guess a number between 1 and 100:")

    
def game(guess_again):
    while guess_again < number_of_attempts:
 
      again = int(input("Make a guess: "))
      if  again > random_number:
          print("Too high")
          print("Guess again")
          print(f"The number of attempts you had {guess_again+1}")
      elif  again < random_number:
          print("Too low")
          print("Guess again")
          print(f"The number of attempts you had {guess_again+1}")
     
      guess_again += 1
      if guess_again == number_of_attempts:
        print("You run out of guesses, you lose.")
      elif  again == random_number:
        print("You win")
        break

