foo = ['abc'] # ['ba']
baz = 'd'
bow = ''.join(foo)
# print(foo, str(foo))
# print(type(bow))

hello = []

for i in range(len(bow) + 1) : # to check how many itteration 
    bar = ''

    for j in range(len(bow)) : # to add the letter
        if i == j : 
            bar += baz

        bar += bow[j]
    
    if i == len(bow): 
        bar  += baz

    hello.append(bar)
    

print(hello)