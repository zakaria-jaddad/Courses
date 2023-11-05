# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Zakaria Jaddad
# Collaborators : <your collaborators>
# Time spent    : 3 Nov -> 

import math
import random
import string

VOWELS = 'aeiou*'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
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
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    

    # storing word points 
    word_points = 0

    for char in word.lower() : 

        # configur wildcard branch 
        if char != '*' : 
            word_points += SCRABBLE_LETTER_VALUES[char]


    # storing Second component

    second_component = (7 * len(word) - 3 * (n - len(word)))

    if  second_component < 1 : 
        second_component = 1

    # getting Total score 
    Total_score = word_points * second_component 

    return Total_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))


    """ 
        This function should be modified 

        in the vowels it should randomly take a reblace a vouwel from the hand 

        Approach  : 
            -> add the * in the VOWELS string 
            -> in the end check if doesn't exist 
                -> take a random number from 0 -> len(finalstring)
                -> add it to it 
    """

    for i in range(num_vowels - 1):

        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1


    hand['*'] = 1
    VOWELS.replace('*', '')

    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    # a copie of dic 
    copied_hand = hand.copy()

    for char in word.lower() : 

        if copied_hand.get(char, -1) != -1 : 

            copied_hand[char] = copied_hand[char] - 1

    return copied_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    POSSIBLE_WORDS = []
    new_hand = hand.copy()
    for char in word.lower() : 

        if new_hand.get(char, 0) == 0 :
            return False

        new_hand[char] = new_hand[char] - 1
        

    # get index of wildcard (*)
    wildcard_index = word.find('*')

    for vowel in VOWELS : 
        # checking for possible words by changing (*) -> vowels 
        if vowel != '*' : 
            new_word = word[0 : wildcard_index] + vowel + word[wildcard_index + 1 : len(word)]

            # if any new words exist return True
            if new_word.lower() in word_list : 
                return True

    if not word.lower() in word_list : 
        return False


    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    HAND_VALUE = 0

    for letter in hand :
        HAND_VALUE += hand[letter]

    return HAND_VALUE


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    TOTAL_SCORE = 0

    while calculate_handlen(hand) != 0 : 

        # show hand 
        print(f'Current Hand : {show_hand(hand)}')

        # ask user fro input 
        word = input(f'Enter word, or "!!" to indicate that you are finished: ')

        # break if !!
        if word == '!!' : 
            break # or return 

        # check if word is valid 
        if is_valid_word(word, hand, word_list) == False : 
            print('That is not a valid word. Please choose another word. ')
            print('------------')
        
        else : 
        
            word_score = get_word_score(word = word, n = calculate_handlen(hand))
            TOTAL_SCORE += word_score
            print(f'"{word}" earned {word_score} points. Total: {TOTAL_SCORE} points ')

            # update hand 
            hand = update_hand(hand,word)

    print(f'Total Score for this hand : {TOTAL_SCORE}')
    print('-------------')

    # return total score 
    return TOTAL_SCORE 


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    LETTER_VALUE = 0
    new_constants = CONSONANTS.replace(letter, '')

    # store value of deleted letter to user next letter
    LETTER_VALUE = hand[letter]
    del hand[letter]


    for char in hand : 
        new_constants = new_constants.replace(char, '')

    hand[random.choice(new_constants)] = LETTER_VALUE

    return hand

    
def show_hand(hand) : 
    
    new_hand = ""

    for char in hand : 

        for letter in range(hand[char]) : 
            new_hand += char + ' '

    return new_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    TOTAL_GAME_SCORE = 0

    number_hands = int(input('Enter Total Number Of Hands : '))

    for i in range(number_hands) : 
        while True :  

            HAND = deal_hand(HAND_SIZE)
            print(F'Current Hand : {show_hand(HAND)}')
            print('------------')

            substitute = input('Would You like to subtitute a letter : ').lower()

            if substitute == 'yes' : 
                subst_letter = input('Which letter would you like to replace : ').lower()
                print('------------')

                HAND = substitute_hand(HAND, subst_letter)


            # get hand score 
            hand_score = play_hand(HAND, word_list=word_list)

            replay_hand = input('Would you like to replay the hand? yes or no : ').lower()

            if replay_hand == 'no' : 
                TOTAL_GAME_SCORE += hand_score
                print(f'Total hand score is : {hand_score}')
                print('------------')
                break

    # Termination of the game 
    print(f'Total score over all hands: : {TOTAL_GAME_SCORE}')



#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    # print(is_valid_word('Qap*urr', {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1},word_list))
    # print(is_valid_word('EVIL', {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}, word_list))
    # print(is_valid_word('Even', {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}, word_list))

    # print(deal_hand(7))
    # print(calculate_handlen({'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}))
