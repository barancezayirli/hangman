import random
from string import ascii_lowercase


def game():
    words = ['python', 'java', 'kotlin', 'javascript', 'angular', 'react', 'django']
    word_index = random.randint(0, 3)
    word = words[word_index]
    guesses = set()

    result = ""
    no_guess = 0

    while no_guess < 8:
        print()
        result = ""
        for letter in word:
            if letter in guesses:
                result += letter
            else:
                result += "-"
        if result == word:
            break
        print(result)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should print a single letter")
        elif guess not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif guess in guesses:
            print("You already typed this letter")
        elif guess not in word:
            guesses.add(guess)
            no_guess += 1
            print("No such letter in the word")
        else:
            guesses.add(guess)

    if result == word:
        print(word)
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")


print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit: ')

while menu != "exit":
    if menu == "play":
        game()
    menu = input('Type "play" to play the game, "exit" to quit: ')
