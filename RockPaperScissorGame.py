import os
import time
import random

dictionary_options = {1:"PAPER", 2:"ROCK", 3:"SCISSOR"}

user_score = 0
pc_score = 0

def header():
    print("""
          
          =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
             WELCOME TO ROCK, PAPER, SCISSOR's GAME
          =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

          """)

def score_points(x, y):
    print(f"""
          Score:
          
                You: {x}
                Computer: {y}

          """)


while True:
    while True:
        header()
        score_points(user_score, pc_score)
        choice = input("""Type:
                                
                    1 - PAPER
                    2 - ROCK
                    3 - SCISSOR
                    
                        OU
                                
                    0 - for EXIT

                    Your Answer: """)
        if choice.isdigit() and (int(choice) in [0, 1, 2, 3]):
            user_choice = int(choice)
            break
        else:
            os.system('clear')
            header()
            print("\nERROR!\nYou'll have to type a valid number choice!\n")
            time.sleep(2)
            os.system('clear')
    
    if user_choice==0:
        os.system('clear')
        print("\nThanks for playing. See you soon!\n")
        break
    else:
        os.system('clear')
        pc_choice = random.randint(1,3)
        if (user_choice==1 and pc_choice==2) or (user_choice==2 and pc_choice==3) or (user_choice==3 and pc_choice==1):
            header()
            print(f"\nYou chose {dictionary_options.get(user_choice)} and the computer {dictionary_options.get(pc_choice)}\nCongrats you won!\n")
            user_score += 1
            score_points(user_score, pc_score)
        elif (user_choice==1 and pc_choice==3) or (user_choice==2 and pc_choice==1) or (user_choice==3 and pc_choice==2):
            header()
            print(f"\nYou chose {dictionary_options.get(user_choice)} and the computer {dictionary_options.get(pc_choice)}\nPC won!\n")
            pc_score += 1
            score_points(user_score, pc_score)
        elif (user_choice==pc_choice):
            header()
            print(f"\nYou chose {dictionary_options.get(user_choice)} and the computer {dictionary_options.get(pc_choice)}\nYou've draw!\n")
            score_points(user_score, pc_score)
        time.sleep(2)
        os.system('clear')