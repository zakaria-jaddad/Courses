
# # getting cube root of a number 

# cube = 27

# epsilon = 0.01

# guess = 0.0

# increment = 0.001

# number_of_guesses = 0

# while abs(guess**3 - cube) >= epsilon and guess <= cube: 


#     # increment the guess 
#     guess += increment

#     # increment counter by one
#     number_of_guesses += 1


# print(f'numner of guesses is {number_of_guesses}')

# # if guess is
# if abs(guess**3 - cube) >= epsilon : 
#     print (f'faild to get cube root of {cube}')

# else : 
#     print(f'cube root of {cube} is a bit like {round(guess)}')




""" 
    bisection cube root 
"""

cube = 0.5

epsilon = 0.001

high = cube

if cube < 1 :

    high = cube * 2
    low = cube

low = 0

number_of_guesses = 0

guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon: 

    if guess**3 < cube : 

        low = guess

    elif guess**3 > cube : 

        high = guess

    guess = (high + low) / 2.0

    number_of_guesses += 1
    print(guess)


print(f'number of guess is {number_of_guesses}')
print(f'square root of {cube} is slightly {guess}')
    