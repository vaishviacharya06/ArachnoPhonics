# ─────────────────────────────────────────────────────────────
# ArachnoPhonics — helper functions
#
# Build these out across L15–L17. The skeletons below are just
# enough to let main.py import them without crashing.
# ─────────────────────────────────────────────────────────────
import time

def load_words(path):
    """Return a list of words read from `path` (one per line)."""
    # TODO (L15): open the file, strip blank lines, return list.
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def build_display(secret, guessed_letters):
    """Return the word with unguessed letters replaced by '_'."""
    # TODO (L15): show guessed letters, hide the rest behind '_'.
    return " ".join(c if c in guessed_letters else "_" for c in secret)


# TODO (L16): add a function that validates a single-letter guess.
def check_word(correct, incorrect, word, tries):
  guess = input("Guess a letter: ").upper()
  if guess in correct or guess in incorrect:
    print("You already guessed that.")
  elif guess in word:
    correct.append(guess)
  elif guess.isalpha() and len(guess) == 1:
    incorrect.append(guess)
    tries += 1
  else:
    print("Please enter a single letter.")
  return tries

def clear_screen():
  print("\n" * 50)
  
# TODO (L17): add a function that asks the player if they want to play again.
def introduction(name):
  print(f"""
  ===================================
  Welcome to ArachnoPhonics, {name}!
  Guess letters before the spider
  finishes weaving its web.
  ===================================
  """)

def pick_difficulty():
    choice = input("Difficulty (easy/medium/hard): ").lower()
    table = {"easy": 8, "medium": 6, "hard": 4}
    max_wrong = table.get(choice, 6)
    print(f"You chose {choice or 'medium'} — {max_wrong} wrong allowed.")
    return max_wrong