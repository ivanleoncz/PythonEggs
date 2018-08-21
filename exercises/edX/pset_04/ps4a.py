# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    scored_letters = 0
    for l in word:
        if l in SCRABBLE_LETTER_VALUES.keys():
            score += SCRABBLE_LETTER_VALUES[l]
            scored_letters += 1                    
    score *= len(word)
    if len(word) != 0 and scored_letters == n:
        score += 50
    return score


#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_update = hand.copy()
    for l in word:
        if l in hand_update.keys():
            hand_update[l] -= 1
    return hand_update


#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    letters_found = 0                                                           
    hand_list = []                                                              
    word_list = sorted(word)                                                    
    if word in wordList:                                                        
        for l in hand.keys():                                                   
            for i in range(hand[l]):                                            
                hand_list += l                                                  
        hand_list.sort()                                                        
        for l in word_list[:]:                                                  
            if l in hand_list:                                                  
                hand_list.remove(l)                                             
                letters_found += 1                                              
        if letters_found == len(word):                                          
            return True                                                         
        else:                                                                   
            return False                                                        
    else:                                                                       
        return False 


#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_size = 0
    for l in hand.keys():
        if hand[l] != 0:
            for size in range(hand[l]):
                hand_size += 1
    return hand_size


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    word = '' # controls the behaviour of the final msg, if user exits
    total_score = 0
    hand_dict = hand.copy()
    while len(hand_dict.keys()) > 0:
        # processing current hand (there could be more than one),
        # providing the avaialable letters from hand_dict
        hand_list = []
        for l in hand_dict.keys():
            for i in range(hand_dict[l]):
                hand_list.append(l)
        # displaying hand
        print("Current Hand:", " ".join(hand_list))
        word = input('Enter word, or a "." to indicate that you are finished: ')
        # '.' stops the function
        if word == '.':
            break
        else:
            # word must be contained in wordList
            if word not in wordList:
                print("Invalid word, please try again.\n")
            else:

                letter_counter = 0 # how many letters are inside hand_dict
                hand_letters = list(hand_dict.keys()) # extract keys (letters)
                # for every letter in word variable...
                for l in word:
                    # ... compare it with one of the current keys
                    for c in hand_letters:
                        # if current letter is equal to current key
                        if l == c:
                            letter_counter += 1 # increase letter_counter
                            # if current key value is equal to 1...
                            if hand_dict[c] == 1: 
                                del hand_dict[c] # ... remove it, or...
                            else:
                                hand_dict[c] -= 1 #... decrease it by 1...
                # at the end of word iteration
                # if letter_counter is equal to word size...
                if letter_counter == len(word):
                    score = getWordScore(word, n) # find the word score
                    total_score += score # increase total_score with score for current word
                    print('"', word,'"', "earned", score, "points.","Total:", total_score, "points")
                else:
                    print("Invalid word, please try again.\n")
    if word == ".":
        print("Goodbye! Total score: ", total_score, " points.")
    else:
        print("\nRun out of letters. Total score: ", total_score, " points.")



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    print("playGame not yet implemented.") # <-- Remove this line when you code the function
   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
