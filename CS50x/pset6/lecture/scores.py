from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("what the score is ? ")
    scores += [score]

average = sum(scores) / len(scores)
print(f"Average is : {average} ")