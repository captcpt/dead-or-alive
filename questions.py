import random
from datetime import datetime
import time

def ask_question():
    question_bank = {
        "What is the capital of France? \n a. Paris | b. London | c. Tokyo | d. San Diego": "a",
        "How many sides does a triangle have? \n a. 2 | b. 6 | c. 3 | d. 1": "c",
        # Add more questions here
    }

    question, correct_answer = random.choice(list(question_bank.items()))
    print(question)

    user_answer = input("Enter the correct letter (a, b, c, d): ").lower()

    if user_answer == correct_answer:
        print("Correct! You've unlocked the door.")
        return True, random.randint(2, 8)  # Return True randomly 2-8 seconds for correct answer
    else:
        print("Wrong answer. 15-30 seconds deducted from your time.")
        return False, random.randint(15, 30)  # Return False and reduction in time for wrong answer
