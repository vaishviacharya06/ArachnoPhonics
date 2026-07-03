# ─────────────────────────────────────────────────────────────
# ArachnoPhonics — main game loop
#
# Hangman-style word guessing game. Each wrong guess adds a
# body part to the spider (see spiderDraw.py — 7 stages total,
# 0 = empty web, 6 = full spider / game over).
#
#   L15  Pseudocode + setup   — load words, pick a secret, set up
#                               display word with underscores
#   L16  Letter-guessing      — prompt for guess, reveal letters,
#                               count wrong guesses, draw spider
#   L17  Win / Lose / Replay  — end states + play-again loop
# ─────────────────────────────────────────────────────────────

import random
import functions as md
import spiderDraw as sd
from functions import load_words, build_display, check_word, clear_screen, time, introduction, pick_difficulty
from spiderDraw import spider_0, spider_1, spider_2, spider_3, spider_4, spider_5, spider_6

SPIDER_STAGES = [spider_0, spider_1, spider_2, spider_3, spider_4, spider_5, spider_6]
MAX_WRONG = pick_difficulty()

def play_round():
  correct, incorrect = [], []
  
  introduction(input("Your name: "))
  words = load_words("words.txt")
  secret = random.choice(words).upper()
  guessed_letters = []
  wrong = 0
  game = True
    
  print("\nWelcome to ArachnoPhonics!\n")
  while game:
    print(SPIDER_STAGES[wrong]())
    print("Word:", build_display(secret, correct))
    tries = md.check_word(correct, incorrect, secret, wrong)
    wrong = tries
    progress = build_display(secret, correct)
    if "_" not in progress:
      print(f"You won! The word was {secret}.")
      game = False
    elif wrong >= MAX_WRONG:
      print(f"You lost. The word was {secret}.")
      game = False

    # TODO (L16): main guess loop — ask for letter, update state,
    # redraw the spider, end when word complete or wrong == MAX_WRONG.


def main():
    # TODO (L17): play_round() inside a play-again loop.
  again = "y"
  while again.lower().startswith("y"):
    play_round()
    clear_screen()
    time.sleep(1)
    again = input("Play again? (y/n): ")
  print("Thanks for playing!")


if __name__ == "__main__":
    main()