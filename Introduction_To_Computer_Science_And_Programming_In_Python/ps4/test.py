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


# math test 

"""     
    #  i + k  >  26

    # 25 + 10 -> 9

    # 12 + 10 -> 22 

    i => index of letter 
    k => shift number 

"""

print((25 + 10) % 26, 9)
print((12 + 10) % 26, 22)