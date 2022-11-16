import random

question_bank = ["Fastest animal", "Largest Mammal", "King of the Jungle"]
answers = {"Fastest animal": "Cheetah", "Largest Mammal": "Whale", "King of the Jungle": "Lion"}
options = {"Fastest animal": ["Cheetah", "tiger"], "Largest Mammal": ["Whale", "Shark"], "King of the Jungle": ["Lion", "Monkey"]}
score = 0


def quiz():
    print(f"Question {question_bank.index(q) + 1} :- {q}?")
    print(f"Options are: {options[q]}")
    user_input = input("\nEnter your answer\n")
    print(f"Your answer is {user_input}")
    if user_input == answers[q] and attempt <= 3:
        return True
    else:
        print("Wrong Answer")
        return False


for q in question_bank:
    attempt = 0
    guessing = False
    while guessing is False and attempt <= 3:
        code = quiz()
        attempt += 1
    if code is True:
        print("right Answer")
        score += 1

print(f"End of Quiz.. \n Your Score is {score}")