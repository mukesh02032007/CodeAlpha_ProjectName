import random

words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left.")

if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
