import random

words = ["python", "apple", "tiger", "planet", "guitar"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

hidden_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses and "_" in hidden_word:
    print("\nWord:", " ".join(hidden_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in hidden_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)