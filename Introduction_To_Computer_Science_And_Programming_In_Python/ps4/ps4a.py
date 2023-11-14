# Problem Set 4A
# Name: Zakaria jaddad
# Collaborators: None 
# Time Spent: 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    """ 

    FUNCTION Implementation Using Recurstion

        Base Case -> one letter Example : (input => 'a', output => ['a'])

        Let's assume that other case is : (input => 'ab', output => [?????])

            PSUEDO CODE : -> We know that length of the end resault list = !len(input)

                - loop from 0 -> len(input)

                    -  every time it get's the ouput from function 
                    -  insert it to it's position 



    

    """

    sequence_resault = []

    # base case 
    if len(sequence) == 1 : 
        return [sequence]
    

    # else the base case 
    first_letter = sequence[0] # get current letter 
    elements = get_permutations(sequence[1::]) # get all elements 


    for element in elements : 

        element = ''.join(element)

        # itterate over all letters in element +1 is additional for the furst_letter
        for element_letters_counter in range(len(element) + 1) : 

            new_element = ''

            # itterate over all letters in the current element 
            for j in range(len(element)) : 

                #  indexing first_letter to be added in the current letter 
                if element_letters_counter == j :
                    new_element += first_letter

                new_element += element[j]


            # if the end add first_letter to the word 
            if element_letters_counter == len(element) : # this cuz we itterate in the j loop just for len(element) 
                new_element += first_letter

            sequence_resault.append(new_element)

    return sequence_resault



def check_get_permutations(actual_output, get_permutations_output) : 
    """ 
        This function takes 2 input : 
            actual_output : list
            get_permutations_output : list

        Retruns : 
            True : if input does have same elements as output 
            False : if input doesn't have same elements as output 
    """

    for inputs in actual_output : 

        if not inputs in get_permutations_output : 
            return False
        
    return True
        

        
    



if __name__ == '__main__':
#   #EXAMPLE 1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('\n\n\n', check_get_permutations(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], get_permutations(example_input)))

    print('\n-------------------\n')

#   EXAMPLE 2
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
    print('Actual Output:', get_permutations(example_input))
    print('\n\n\n', check_get_permutations(['123', '132', '213', '231', '312', '321'], get_permutations(example_input)))


    print('\n-------------------\n')


#   EXAMPLE 3
    example_input = 'abcd'
    print('Input:', example_input)
    print('Expected Output:', ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
    print('Actual Output:', get_permutations(example_input))
    print('\n\n\n', check_get_permutations(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'], get_permutations(example_input)))


    print('\n-------------------\n')


#   EXAMPLE 4
    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(example_input))
    print('\n\n\n', check_get_permutations(['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'], get_permutations(example_input)))


    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

