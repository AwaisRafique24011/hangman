import random

def hangman():
    #Word file in which program use random word
    word_list = ['python', 'java', 'swift', 'javascript', 'hangman', 'programming']
    word = random.choice(word_list).lower()
    guessed_word = ['_'] * len(word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print("The word has", len(word), "letters.")
    print(" ".join(guessed_word))
#loops that check the letter
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nGuess a letter: ").lower()
#condition
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
#condition
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")

        print(" ".join(guessed_word))
#if guess correct
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nGame over! You've run out of attempts. The word was:", word)

# Run the game
hangman()
