import random

words = ["shopping", "gaming", "spaceship", "curtains", "bicycle", "garden"]

while True:
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6

    print("\nWelcome to Hangman!")
    print("Word to guess:", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess. Attempts left: {attempts}")

        print("Word:", " ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Game over! The word was:", word)

    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes":
        print("Thanks for playing Hangman! Goodbye.")
        break
