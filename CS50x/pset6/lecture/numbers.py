import sys

numbers = [10, 1, 3, 50, 4, 5, 6, 7, 44, 11, 23]
if 2 in numbers:
    print("found")
    sys.exit(0)
print("not found")
sys.exit(1)