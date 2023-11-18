# Problem Set 4B
# Name: Zakaria Jaddad
# Collaborators: None
# Time Spent: -

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

def get_valid_words_counter(text, word_list) : 
    """ 
    text : string  
    word_list : list of valid words 

    Retruns number of valid words valid words in input text -> int 
    """

    valid_words_counter = 0

    for word in text : 
        # check word validation and if word from string is an alphabetical
        if word.isalpha() : 
            if is_word(word_list, word) : 

                valid_words_counter += 1
        
    return valid_words_counter
### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text : str):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.__message_text = text

        self.__valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.__message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.__valid_words.copy() # returns a copy of valid words using .copy method 

    def build_shift_dict(self, shift : int):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                another letter (string). 
        '''

        # shift error handel 
        if not (shift >= 0 and shift < 26) : 
            return 'the amount by which to shift every letter of the alphabet \
                    shift value : 0 <= shift < 26'

        # initla varibales decleration 
        LOWER_LETTERS = string.ascii_lowercase
        UPPER_LETTERS = string.ascii_uppercase
        letters_map = {}

        for letter in self.__message_text : 

            # check if letter is not in dic
            if not letter in letters_map : 

                if letter.isalpha() : 

                    # checkes is letter is lower or upper case
                    if letter in LOWER_LETTERS : 

                        letter_index = LOWER_LETTERS.index(letter)

                        letters_map[letter] = LOWER_LETTERS[(letter_index + shift) % 26]

                    else : # letter is upper case 

                        letter_index = UPPER_LETTERS.index(letter)

                        letters_map[letter] = UPPER_LETTERS[(letter_index + shift) % 26]

                else : 
                    letters_map[letter] = letter


        return letters_map

    def apply_shift(self, shift : int):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
                down the alphabet by the input shift
        '''

        # get mapped letter dictionary
        mapped_letters = self.build_shift_dict(shift = shift)

        # Initialisation of returned string  
        cipher_text = ''

        # itterate over all letters in message text
        for letter in self.get_message_text() : 
            cipher_text += mapped_letters[letter]


        return cipher_text


class PlaintextMessage(Message):
    def __init__(self, text : str, shift : int):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.__shift = shift
        self.__encryption_dic = Message.build_shift_dict(self, shift)
        self.__message_text_encrypted = Message.apply_shift(self, shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.__shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.__encryption_dic

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.__message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''

        # checking 
        if not (shift >= 0 and shift < 26) : 
            return 'the new shift that should be associated with this message. \
                    0 <= shift < 26'

        self.__shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        """ 
            get cipher text 

            each time cipher is more by one shift and check if all words are words using is_word() function 
                if all return the shift 
        """

        all_shifts_valid_words = []

        word_list = CiphertextMessage.get_valid_words(self)

        shift = 1

        while shift < 26 : 
            
            # get cipherd text by current shift value 
            shifted_text = CiphertextMessage.apply_shift(self, shift).split(' ') # type list 

            # append number of valid words in the shifted text
            all_shifts_valid_words.append(get_valid_words_counter(text=shifted_text, word_list=word_list))

            shift += 1 
    
        decrypted_text =  CiphertextMessage.apply_shift(self, all_shifts_valid_words.index(max(all_shifts_valid_words)) + 1)

        return (all_shifts_valid_words.index(max(all_shifts_valid_words)) + 1, decrypted_text)






if __name__ == '__main__':

    # Example test case (PlaintextMessage)

    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)

    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    print('\n\n-------\n\n')

    #   Message Class
    text = PlaintextMessage('hello this is some text, HELLO THIS IS SOME TEXT', 12)
    print('Cipherd Text', text.get_message_text_encrypted())
    print('Message Text', text.get_message_text())
    print('shift', text.get_shift())

    print('\n\n-------\n\n')

    # Cipherd Class
    ciphertext = CiphertextMessage(text.get_message_text_encrypted())
    print('Cipher Message Text', ciphertext.get_message_text())

    print('Expected Output shoud be input above ', ciphertext.apply_shift(ciphertext.decrypt_message()[0])) 

    print('\n\n-------\n\n')



    # story Example 
    story = get_story_string()

    cipher_story = CiphertextMessage(story)

    # print('Input Story :', cipher_story.get_message_text())
    print('Best Shifed value :', cipher_story.decrypt_message())
    print('\n\n-------\n\n')
    print('Actual Story Output :', cipher_story.decrypt_message())
