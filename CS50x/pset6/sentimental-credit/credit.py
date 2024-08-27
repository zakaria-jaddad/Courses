def main():
    n = 0
    while int(n) < 1:
        n = input("how much")
        digit = credit(n)
        print(digit, n[0], n[1])
        digit_1 = int(n[0])
        digit_2 = int(n[1])
        if (digit % 10) - 6 == 0 and digit_1 == 3 and (digit_2 == 4 or digit_2 == 7):
            print("AMEX")
        elif (digit % 10 == 0 and digit_1 == 4) and len(n) >= 13:
            print("VISA")
        else:
            if digit == 48:
                print("AMEX")
            elif digit == 44:
                print("VISA")
            for i in range(1, 6):
                if digit_1 == 5 and digit_2 == i and digit % 10 == 0:
                    print("MASTERCARD")
                    return 0
            print("INVALID")


def credit(n):
    # here
    summe = 0
    for i in range(0, len(n), 2):
        x = int(n[i]) * 2
        x = str(x)
        if len(x) == 2:
            summe += int(x[0]) + int(x[1])
        else:
            summe += int(x)
    for i in range(1, len(n), 2):
        summe += int(n[i])
    return summe


if __name__ == "__main__":
    main()
