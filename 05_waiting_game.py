import time
import random

def start_game():
    target_time = random.randint(2,4)
    print("Welcome to the Waiting Game!")
    print(f"Your target time is {target_time} seconds")
    while True:
        tStart = input("--- Press Enter to Begin ---")
        if tStart == "":
            break
        else: 
            tStart = input("--- Press Enter to Begin ---")

    start_time = time.time()
    
    input(f"--- Press Enter again after {target_time} seconds ---")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    
    if abs(elapsed_time - target_time) <= 0.1:
        print("Great job! You were very close!")
    elif elapsed_time < target_time:
        print("Too fast! Try to wait a bit longer next time.")
    else:
        print("Too slow! Try to be quicker next time.")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        start_game()
    else:
        print("Thanks for playing! Goodbye.")

start_game()
