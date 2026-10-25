import random


HANGMAN_STAGES = (
    (
        "  +---+",
        "  |   |",
        "      |",
        "      |",
        "      |",
        "=========",
    ),
    (
        "  +---+",
        "  |   |",
        "  O   |",
        "      |",
        "      |",
        "=========",
    ),
    (
        "  +---+",
        "  |   |",
        "  O   |",
        "  |   |",
        "      |",
        "=========",
    ),
    (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|   |",
        "      |",
        "=========",
    ),
    (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        "      |",
        "=========",
    ),
    (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " /    |",
        "=========",
    ),
    (
        "  +---+",
        "  |   |",
        "  O   |",
        " /|\\  |",
        " / \\  |",
        "=========",
    ),
)


WORDS_BY_CATEGORY = {
    "animals": {
        "alpaca": "A fluffy animal that looks permanently surprised.",
        "badger": "A small digger with a black-and-white face.",
        "dolphin": "A clever sea mammal that enjoys showing off.",
        "giraffe": "A very tall animal with a built-in lookout.",
        "hamster": "A tiny pet that stores snacks in its cheeks.",
        "lemur": "A wide-eyed primate with a striped tail.",
        "otter": "A playful swimmer that sometimes holds hands.",
        "turtle": "A slow reptile that carries its house.",
    },
    "food": {
        "avocado": "A green fruit that made toast very fashionable.",
        "biscuit": "A crunchy snack that vanishes during tea.",
        "brownie": "A chocolate square that never lasts long.",
        "cheese": "A dairy food with many holes and opinions.",
        "coconut": "A hard-shelled fruit with vacation energy.",
        "omelette": "Eggs folded around whatever is in the fridge.",
        "pancake": "A flat breakfast that enjoys a syrupy hat.",
        "spaghetti": "Long pasta that tangles like headphone wires.",
    },
    "school": {
        "backpack": "A bag that carries half your life to class.",
        "biology": "The study of living things and their weird habits.",
        "calculator": "A tiny machine that does the maths you forgot.",
        "dictionary": "A book that explains words using more words.",
        "homework": "Schoolwork that somehow follows you home.",
        "notebook": "A place for notes, doodles, and secret plans.",
        "science": "The study of how things work and why they fizz.",
        "teacher": "A professional question-answerer with a marker.",
    },
    "space": {
        "comet": "An icy space visitor with a bright tail.",
        "galaxy": "A huge collection of stars, gas, and cosmic dust.",
        "jupiter": "The biggest planet in our solar system.",
        "meteor": "A space rock that glows as it enters the atmosphere.",
        "nebula": "A colourful cloud of gas and dust in space.",
        "planet": "A large round object that orbits a star.",
        "rocket": "A vehicle that makes a very dramatic exit from Earth.",
        "telescope": "A tool for seeing faraway things in the sky.",
    },
    "technology": {
        "browser": "An app for looking around the internet.",
        "keyboard": "A board full of keys that cannot open your front door.",
        "laptop": "A portable computer that gets warm during homework.",
        "microphone": "A device that makes your voice louder.",
        "monitor": "A screen that watches your computer work.",
        "password": "A secret word that should not be your pet's name.",
        "printer": "A machine that waits until the deadline to complain.",
        "robot": "A machine that follows instructions and never needs lunch.",
    },
    "nature": {
        "blizzard": "A snowstorm that makes going outside a bad idea.",
        "forest": "A large area full of trees and wildlife.",
        "island": "Land surrounded by water on every side.",
        "jungle": "A dense tropical forest full of life.",
        "meadow": "A grassy field that sounds like a picnic spot.",
        "mountain": "A very tall landform with a summit.",
        "rainbow": "A colourful arc that appears after rain.",
        "volcano": "A mountain that may erupt with lava.",
    },
    "everyday things": {
        "alarm": "A device whose job is to interrupt your best dream.",
        "blanket": "A cosy cover that makes getting up harder.",
        "candle": "A small light with a flame and a waxy base.",
        "curtain": "Fabric that gives a window some privacy.",
        "flashlight": "A portable light for finding things in the dark.",
        "pillow": "A soft place for your head to make plans.",
        "scissors": "A tool with two blades and a very specific haircut risk.",
        "toaster": "A machine that turns bread into crunchy bread.",
    },
    "silly words": {
        "hiccup": "A tiny noise that arrives without an invitation.",
        "jellyfish": "A sea creature with no bones and a very wobbly name.",
        "noodle": "Pasta, or an affectionate word for a silly person.",
        "pickle": "A cucumber that took a long bath in vinegar.",
        "sneakers": "Shoes designed for running, walking, or sneaking snacks.",
        "squirrel": "A tree-climbing animal with excellent snack storage.",
        "tadpole": "A baby frog that has not grown its legs yet.",
        "yodel": "A singing style that echoes around the mountains.",
    },
}


WELCOME_LINES = (
    "Welcome to Hangman: the only game where a stick figure is your life coach.",
    "Welcome! The secret word is hiding. It claims it is not hiding.",
    "Let's play Hangman. The game is friendly; the stick figure is dramatic.",
)

CORRECT_GUESS_LINES = (
    "Nice! That letter was definitely in there the whole time.",
    "Correct! The mystery word has revealed one tiny secret.",
    "Good guess! Your letter-detecting skills are suspiciously good.",
    "Yep! The word is starting to look less mysterious.",
    "Correct! The word has lost its element of surprise.",
)

WRONG_GUESS_LINES = (
    "Nope. The word says it has never heard of that letter.",
    "Wrong! The stick figure has requested a tiny helmet.",
    "Not this time. The alphabet is being difficult.",
    "Miss! Somewhere, a letter is pretending it was not involved.",
    "Missed! Your guess has wandered into the wrong dictionary.",
)

INVALID_GUESS_LINES = (
    "One letter at a time, please. The alphabet is large enough already.",
    "That is not one letter. The word asked for a simple introduction.",
    "Please enter a single letter, not a whole novel.",
)

REPEATED_GUESS_LINES = (
    "You already tried that letter. It has had its turn.",
    "That letter is old news. Pick a different one.",
    "Repeat guesses do not count; the stick figure checked the rules.",
)

WIN_LINES = (
    "You win! The word has been found and may now stop hiding.",
    "Brilliant! The stick figure can put its feet up.",
    "Victory! You and the alphabet are officially friends.",
    "You solved it! The mystery word has been unmasked.",
)

LOSS_LINES = (
    "Oh no! The stick figure is complete. The word wins this round.",
    "Game over! The word was hiding in plain sight. Rude.",
    "The last body part appeared. The word has escaped justice.",
    "So close! The stick figure is finished, but there is always a rematch.",
)

HINT_LINES = (
    "Your hint is: {hint}",
    "A helpful clue, delivered by the very patient dictionary: {hint}",
    "The word has reluctantly offered this clue: {hint}",
)


def choose_category():
    """Let the player pick a topic, or choose a surprise category."""
    category_names = list(WORDS_BY_CATEGORY)

    print("\nChoose a category:")
    for number, category in enumerate(category_names, start=1):
        print(f"  {number}. {category.title()}")
    print("  R. Random category")

    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in ("r", "random", ""):
            category = random.choice(category_names)
            print(f"The surprise category is: {category.title()}!")
            return category

        if choice.isdigit():
            category_number = int(choice)
            if 1 <= category_number <= len(category_names):
                return category_names[category_number - 1]

        print("Please enter one of the listed numbers, or R for random.")


def draw_hangman(wrong_guesses):
    """Display the gallows and the body parts for the current mistake count."""
    print()
    for line in HANGMAN_STAGES[wrong_guesses]:
        print(line)


def show_word(secret_word, guessed_letters):
    """Return the word with unknown letters replaced by underscores."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def show_round_status(secret_word, guessed_letters, wrong_guesses, hint_used):
    """Print the current puzzle and useful round information."""
    draw_hangman(wrong_guesses)
    print(f"\nWord: {show_word(secret_word, guessed_letters)}")
    print(f"Misses remaining: {6 - wrong_guesses}")

    if guessed_letters:
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    else:
        print("Guessed letters: none yet (a clean slate!)")

    if hint_used:
        print("Hint: already used. The hint budget has left the building.")
    else:
        print("Type HINT for a clue. It costs one miss.")
    print("Type QUIT to end this round.")


def ask_for_guess(guessed_letters):
    """Read and validate one letter, or return a special command."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if guess in ("quit", "exit"):
            return "quit"

        if guess == "hint":
            return "hint"

        if len(guess) != 1 or not guess.isalpha():
            print(random.choice(INVALID_GUESS_LINES))
            continue

        if guess in guessed_letters:
            print(random.choice(REPEATED_GUESS_LINES))
            continue

        return guess


def give_hint(secret_word, hint, wrong_guesses):
    """Reveal a useful clue and charge one miss for asking."""
    print("\n" + random.choice(HINT_LINES).format(hint=hint))
    print("The stick figure charges one miss for professional consulting.")
    wrong_guesses += 1

    if wrong_guesses == 6:
        print("The clue arrived, but so did the final body part!")
        print(f"The secret word was: {secret_word}")
        return wrong_guesses

    return wrong_guesses


def show_win_message(secret_word, wrong_guesses):
    """Celebrate a solved word and report how cleanly it was solved."""
    draw_hangman(wrong_guesses)
    print(f"\nThe word was: {secret_word}")
    print(random.choice(WIN_LINES))

    if wrong_guesses == 0:
        print("Zero misses! The stick figure never even got out of bed.")
    elif wrong_guesses <= 2:
        print("Nearly flawless. The gallows barely had time to wake up.")
    elif wrong_guesses <= 4:
        print("A close one! The stick figure recommends a less dramatic hobby.")
    else:
        print("That was a last-second rescue. Please let the stick figure breathe.")


def show_loss_message(secret_word):
    """Show the complete drawing and reveal the missed word."""
    draw_hangman(6)
    print(f"\nThe secret word was: {secret_word}")
    print(random.choice(LOSS_LINES))


def play_hangman():
    """Play one round and return whether it was won and how many misses occurred."""
    category = choose_category()
    secret_word, hint = random.choice(list(WORDS_BY_CATEGORY[category].items()))
    guessed_letters = set()
    wrong_guesses = 0
    hint_used = False

    print(f"\nCategory: {category.title()}")
    print(f"Word length: {len(secret_word)} letters")
    print(random.choice(WELCOME_LINES))

    while wrong_guesses < 6:
        show_round_status(
            secret_word,
            guessed_letters,
            wrong_guesses,
            hint_used,
        )

        if all(letter in guessed_letters for letter in secret_word):
            show_win_message(secret_word, wrong_guesses)
            return True, wrong_guesses

        guess = ask_for_guess(guessed_letters)

        if guess == "quit":
            print(f"\nYou left the round. The word was: {secret_word}")
            print("The   stick figure understands. Everyone needs a break.")
            return False, wrong_guesses

        if guess == "hint":
            if hint_used:
                print("You already used your hint. Even hints need boundaries.")
                continue

            hint_used = True
            wrong_guesses = give_hint(
                secret_word,
                hint,
                wrong_guesses,
            )
            if wrong_guesses == 6:
                return False, wrong_guesses
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(random.choice(CORRECT_GUESS_LINES))
        else:
            wrong_guesses += 1
            print(random.choice(WRONG_GUESS_LINES))   

    show_loss_message(secret_word)
    return False, wrong_guesses


def show_session_summary(games_played, games_won, best_streak, total_misses):
    """Print a friendly recap for the whole play session."""
    print("\n" + "=" * 42)
    print("SESSION RECAP")
    print("=" * 42)
    print(f"Rounds played: {games_played}")
    print(f"Rounds won: {games_won}")
    print(f"Rounds lost or left: {games_played - games_won}")
    print(f"Best winning streak: {best_streak}")
    print(f"Total misses: {total_misses}")

    if games_played == 0:
        print("No rounds played. The stick figure had a very relaxing day.")
    elif games_won == games_played:
        print("A perfect session! The words are asking for a rematch.")
    elif games_won == 0:
        print("The words had a lucky streak. Your comeback story starts next round.")
    elif games_won * 2 >= games_played:
        print("More wins than losses: the alphabet is mostly on your side.")
    else:
        print("The words were sneaky today. They have been warned.")
    print("=" * 42)


def ask_to_play_again():
    """Ask whether to start another round."""
    while True:
        answer = input("\nPlay another round? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer Y or N. The stick figure is waiting patiently.")


def main():
    """Run rounds until the player chooses to stop."""
    games_played = 0
    games_won = 0
    current_streak = 0
    best_streak = 0
    total_misses = 0

    print("=" * 42)
    print("       THE EXTREMELY WORDY HANGMAN")
    print("=" * 42)
    print("Guess the secret word before all six body parts appear.")
    print("You can ask for one hint per round, but it costs a miss.")
    print("You can also type QUIT if the word is being unbearable.")

    while True:
        won, misses = play_hangman()
        games_played += 1
        total_misses += misses

        if won:
            games_won += 1
            current_streak += 1
            best_streak = max(best_streak, current_streak)
        else:
            current_streak = 0

        print(f"\nCurrent winning streak: {current_streak}")
        if not ask_to_play_again():
            break

    show_session_summary(
        games_played,
        games_won,
        best_streak,
        total_misses,
    )
    print("Thanks for playing. May your next word have all its vowels.")


if __name__ == "__main__":
    main()
