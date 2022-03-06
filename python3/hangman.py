#HANGMAN - Day 3 - 05/03/2022
#WRITTEN BY - GitHub.com/ItzKakarotto

#ASCII - gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c & ascii.co.uk/art/hangman

TIPS = ("Type 'hint' to get a hint", "Type 'lives' to get your lives Remaining")

import random

#Welcome to Hangman
print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
|_____________________________________________|
\n""")


#Just some stolen stuff
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["mango", "otaku", "abstract", "lmao", "kakarot", "anime", "festival", "india", "program", "askew", "azure", "luxury", "bikini", "abyss", "buffalo", "pixel", "cobweb", "puppy", "stupid", "quiz", "equip", "random", "euouae", "exodus", "faking", 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'catwalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kiwifruit', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'yesterday', 'rhythm', 'rickshaw', 'social', 'scratch', 'shiv', 'snazzy', 'solid', 'sprint', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'android', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelve', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex']



#Initialization 
lives = 6 #Dont change -__-
hints = 2 #Dont cheat -__-

chosen_word = random.choice(words)
chosen_word_blank = list()

for x in chosen_word:
    chosen_word_blank.append("_")


def _hint():
    """generate a new hint"""
    global hints
    hint = random.choice(chosen_word)
    if hint not in chosen_word_blank:
        hints-=1
        return hint
    else:
        return _hint()

 
def guess_func():
    """gets the user input and provides hint"""
    global hints
    guess = str(input("\nGuess a letter: ").lower())
    if len(guess)>1:
        if guess.startswith("hi"):
            if hints==0:
                print("You don't have any Hints Remaining")
                return guess_func()
            else:
                print(f"Used a hint, {hints-1} hints remaining")
                return _hint()
        elif guess.startswith("li"):
            print(f"You have {lives} lives")
            return guess_func()
        else:
            print("You can only guess one letter at a time")
            return guess_func()
    elif guess in chosen_word_blank:
        print(f"'{guess}' is already guessed!")
        return guess
    else:
        return guess

        
def replace_guess(guess):
    """replaces the blank with guessed letter if guessed letter is in the word"""
    global lives
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                chosen_word_blank[i] = guess
    else:
        lives-=1
        print(f"'{guess}' is not in the Word!")
 
 
def main():
    """the switch"""
    global lives

    while "_" in chosen_word_blank and lives!=0:        
        print("\n"+HANGMANPICS[6-lives])
        print("Word:", ' '.join(chosen_word_blank))        
            
        guess = guess_func()
        replace_guess(guess)
    
    if lives==0:
        print(f"\n{HANGMANPICS[6-lives]}\n\nYou couldn't save Hangman!. The word was '{chosen_word}'")
        return
    if "_" not in chosen_word_blank:
        print(f"\n(づ￣ ³￣)づ\n\nYou guessed the word! '{chosen_word}'. Hangman is now safe")
        return


main()
