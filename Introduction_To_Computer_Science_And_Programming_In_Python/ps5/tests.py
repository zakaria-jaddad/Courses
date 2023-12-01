# this is some tests to understand what is working in a lecture code 

def intTostring(i : int) : 
    """ 
    - input i : number
    - output resualt : string
    converts given int to a string 

    inptu: 503 : int -> output: 503 : string
    
    Time complixety O( log(n) ) 
        - Where n is i -> (n = i)
        - Because each time we reduce the size of the problem by half
    """

    numbers = '0123456789'
    response = ''

    while i > 0 : 

        response = numbers[i % 10] + response
        i = i // 10

    return response


def fib_iter(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        fib_i = 0
        fib_ii = 1
        for i in range (n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
            print(fib_ii)
        return fib_ii


def bisection_2_pointers(L: list, element: int) : 
    """ 
        givng 2 pointers 
        i want to know where is my number 
        pointer 1: lower
        pointer 2: upper
    """
    lower = 0
    upper  = len(L) - 1

    while lower != upper : # Assume that list hasn't redundancy

        middle = (lower + upper) // 2

        if L[middle] > element : 
            upper = middle

        elif L[middle] < element : 
            lower = middle

        else : 
            return element
            

    return 'not found '


""" 
def bisection_2_pointers_version_2(L: list, element: int) : 

    def helper_bisection(low, high, L, element) : 

        if low == high : 
            return low == element
        

        middle = (low + high) // 2

        if element == L[middle] : 
            return True
        
        if element > L[middle] : 

            if low == middle : 
                return False # nothing is to search 

            return helper_bisection(low=middle + 1, high=high, L=L, element=element)
        else : 
            return helper_bisection(low=low, high=middle - 1, L=L, element=element)
        


    if len(L) == 0 : 
        return False 
    
    return helper_bisection(0, len(L) - 1, L, element)

"""

def bisection_2_pointers_version_2(L: list, element: int) : 


    def bisection_helper(L, element, low, high) : 

        if low == high  : 
            return False
        
        middle = (low + high) // 2
        print(low, high, middle)

        if L[middle] == element : 
            return True

        if  element > L[middle] : 

            if middle == low : 
                return False
        
            return bisection_helper(L, element, middle + 1, high)

        else : 

            return bisection_helper(L, element, low, middle - 1)




    if len(L) == 0 : 
        return False


    return bisection_helper(L, element, 0, len(L) - 1)



# print(intTostring(500))

# print(fib_iter(300))

print(' ------------------ ')

# print(bisection_2_pointers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20))

print(bisection_2_pointers_version_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))

