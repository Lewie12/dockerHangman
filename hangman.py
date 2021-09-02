import random

words = ["something", "marvel movies", "valorant", "cool"]
word = random.choice(words)

lives = 6
guesses = [" "]

while True:
    blanks = 0
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            blanks += 1
            print("_", end=" ")
    print()

    if blanks == 0:
        print("You win!")
        break

    guess = input("Choose a letter: ")
    guesses.append(guess)

    if guess not in word:
        lives -= 1
        print(f"Incorrect! {lives} remaining")
    
    if lives == 0:
        print("GAME OVER")
        