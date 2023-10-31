# Problem Set 2, hangman.py
# Name: Zakaria Jaddad
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from os import system

WORDLIST_FILENAME = "words.txt"

# warn user for typing (non alphbetical letter, al guessed letter)
def warn_user(WARNING_COUNTER, GUESSES_COUNTER) : 


    if WARNING_COUNTER <= 0 : 
        GUESSES_COUNTER -= 1
    
    WARNING_COUNTER -= 1

    return WARNING_COUNTER, GUESSES_COUNTER


def no_vowel_in_word(guesses_counter : int) : 

    return guesses_counter - 2


def get_unique_letters_number(secret_word_letters) : 

    unique_letters = ''

    for letter in secret_word_letters :

        if not letter in unique_letters : 
            unique_letters += letter

    return unique_letters


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    # itteration over all letters in the secret_word 
    for letter in secret_word :

        # checking if current letter (from secret_word) is not in the letters_guessed list 
        if not letter in letters_guessed :
            return False
        
    # other wise return True
    return True



def get_guessed_word(secret_word, letters_guessed : list):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    GUESSED_WORD = ''

    for letter in secret_word : 

        if letter in letters_guessed : 

            GUESSED_WORD += letter

        else : 
            
            GUESSED_WORD += '_ '


    return GUESSED_WORD



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    AVAILABLE_LETTERS = ''

    for letter in string.ascii_lowercase : 
        
        if not letter in letters_guessed :

          AVAILABLE_LETTERS += letter

    
    return AVAILABLE_LETTERS

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    GUESSES_COUNTER = 6
    WARNING_COUNTER = 3


    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    LETTERS_GUESSED = []

    # one time Print Flag
    first_print = 0

    while (not is_word_guessed(secret_word, LETTERS_GUESSED) == True) :


        # print(is_word_guessed(secret_word, LETTERS_GUESSED))
        # print(get_available_letters(LETTERS_GUESSED))

        if (first_print == 0) : 

            # warning counter
            print(f"You have {WARNING_COUNTER} warning left.")
            
            # seperator 
            print('-----------')

        first_print += 1

        # guesses counter 
        print(f"You have {GUESSES_COUNTER} guesses left.")

        # available letters 
        print(f"Available letters: {get_available_letters(LETTERS_GUESSED)}")

        letter = input("Give Me A Letter : ").lower()

        # checking for letter is an alphabet 
        if str.isalpha(letter) == False : 

            WARNING_COUNTER, GUESSES_COUNTER = warn_user(WARNING_COUNTER, GUESSES_COUNTER)
            
            if WARNING_COUNTER >= 0 : 
                print(f"Oops! That is not a valid letter. You have {WARNING_COUNTER} warning(s) left: {get_available_letters(LETTERS_GUESSED)}")
            else : 
                print(f"Oops! That is not a valid letter. You have no warnings left so you lose one guess: {get_available_letters(LETTERS_GUESSED)}")

        # if it's indded an alphabet 
        else : 

            # checking if guessed letter in the gussed letters 
            if not letter in LETTERS_GUESSED : 

                LETTERS_GUESSED.append(letter)

                # good guess 
                if letter in secret_word : 
                    print(f"Good guess : {get_guessed_word(secret_word, LETTERS_GUESSED)}")

                # bad guess
                else : 

                    print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, LETTERS_GUESSED)}")

                    if letter in ['a', 'e', 'i', 'o', 'u', 'y'] : 
                        GUESSES_COUNTER = no_vowel_in_word(GUESSES_COUNTER)

                    else : 
                        GUESSES_COUNTER -= 1

            
            else : 
                WARNING_COUNTER, GUESSES_COUNTER = warn_user(WARNING_COUNTER, GUESSES_COUNTER)
                if WARNING_COUNTER >= 0 : 
                    print(f"Oops! You've already guessed that letter. You have {WARNING_COUNTER} warning(s) left: \n {get_guessed_word(secret_word, LETTERS_GUESSED)}")
                else : 
                    print(f"Oops! You've already guessed that letter. You have no warnings so you lose one guess: \n {get_guessed_word(secret_word, LETTERS_GUESSED)}")



        # game Termination
        if GUESSES_COUNTER <= 0 : # did this '<=' because for vouels it substract 2
            print(f"Sorry, you ran out of guesses. The word was : {secret_word}")
            return 

        print("\n---------------\n")


    # game Termination
    if is_word_guessed(secret_word, LETTERS_GUESSED) == True : 
        Total_score = GUESSES_COUNTER * len(get_unique_letters_number(secret_word))
        print(f"Congratulations, you won! \n Your total score for this game is: {Total_score}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------





def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    # checkes is 2 words has same lenght
    if (len(my_word) == len(other_word)) : 

        for i in range(len(my_word)) :

            if other_word[i] != '_' : 
                if not my_word[i] == other_word[i] : 
                    return False

    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    print(secret_word)
    print(match_with_gaps("that", '_ _ _ t'.replace(' ', '')))
    print("Welcome to the game Hangman!")
    # hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
