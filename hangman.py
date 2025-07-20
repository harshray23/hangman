#!/usr/bin/env python3
"""
Hangman — simplified console version
• Five predefined words
• Six allowed wrong guesses
"""

import random
import string

WORD_LIST = ["APPLE", "BANANA", "CHERRY", "GRAPE", "MANGO"]
MAX_WRONG = 6


def pick_word() -> str:
    return random.choice(WORD_LIST)


def display_state(secret, correct, wrong):
    revealed = " ".join([c if c in correct else "_" for c in secret])
    print(f"\nWord: {revealed}")
    print(f"Misses ({len(wrong)}/{MAX_WRONG}): {' '.join(sorted(wrong)) or '-'}")


def main():
    secret = pick_word()
    correct, wrong = set(), set()

    while len(wrong) < MAX_WRONG and set(secret) != correct:
        display_state(secret, correct, wrong)
        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("⚠️  Please enter a single A‑Z letter.")
            continue
        if guess in correct | wrong:
            print("⚠️  Already tried that.")
            continue

        (correct if guess in secret else wrong).add(guess)

    display_state(secret, correct, wrong)
    if set(secret) == correct:
        print("\n🎉  You win!")
    else:
        print(f"\n💀  Out of guesses. The word was: {secret}")


if __name__ == "__main__":
    main()
