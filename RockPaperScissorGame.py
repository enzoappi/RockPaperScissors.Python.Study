import os
import time
import random

dictionary_options = {1:"PAPER", 2:"ROCK", 3:"SCISSOR"}

user_choice = int(input("""Digite:
              
              1 - PAPER
              2 - ROCK
              3 - SCISSOR

              Your Answer: """))

pc_choice = random.randint(1,3)

time.sleep(0.5)

print(f"\nYou chose {dictionary_options.get(user_choice)} and the computer {dictionary_options.get(pc_choice)}")