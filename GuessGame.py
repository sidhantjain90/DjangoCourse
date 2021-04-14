# Generate the code
import random
def generate_code():
    digits = [str(num) for num in range(10)]

    random.shuffle(digits)
    return digits[:3]

# Get Guess
def get_guess():
    return list(input("What is your guess?"))

# Generate the clues
def generate_clues(code, user_guess):

    if user_guess == code:
        print("Code Cracked!")

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# Game Logic
print("Welcome to code Breaker!")

secret_code = generate_code()

clueReport = []

while clueReport != "Code Cracked!":
    guess = get_guess()

    clueReport = generate_clues(guess, secret_code)
    print("here is the result of your guess!")
    for clue in clueReport:
        print(clue)
