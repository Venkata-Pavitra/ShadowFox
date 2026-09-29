import random
words = {
    "python": "A popular programming language",
    "computer": "An electronic device used to process data",
    "programming": "The process of writing computer programs",
    "keyboard": "A device used to type on a computer",
    "internet": "A worldwide network of computers"
}
word = random.choice(list(words.keys()))
hint = words[word]
guessed_letters = set()
wrong_guesses = 0
max_wrong = 6
hangman = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

print("===== HANGMAN GAME =====")
print("Hint:", hint)

while wrong_guesses < max_wrong:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    print("Wrong guesses:", wrong_guesses, "/", max_wrong)
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("\nGame Over!")
    print("The correct word was:", word)