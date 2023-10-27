# importing logarithm from numpy
from numpy import log2

# getting X and Y from user 
numberX = int(input('Enter number X: '))
numberY = int(input('Enter number Y: '))

# resultes varibales 
x_raised_by_y = numberX ** numberY
logX = int(log2(numberX))

# printing results 
print(f"X ** Y = {x_raised_by_y}")
print(f"log(X) = {logX}")

