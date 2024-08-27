from cs50 import get_float


def main():
    # here
    while True:
        dollars = get_float("Change owed: ")
        if dollars > 0:
            break
    centes = round(dollars * 100)
    print(centes)
    quarters = calculate_quarters(centes)
    centes = centes - quarters * 25
    #
    dimes = calculate_dimes(centes)
    centes = centes - dimes * 10
    #
    nickels = calculate_nickels(centes)
    centes = centes - nickels * 5
    #
    pennies = calculate_pennies(centes)
    centes = centes - pennies * 1
    # printing
    coins = quarters + dimes + nickels + pennies
    print(coins)


def calculate_quarters(centes):
    counter = 0
    while centes >= 25:
        counter += 1
        centes -= 25
    return counter


def calculate_dimes(centes):
    counter = 0
    while centes >= 10:
        counter += 1
        centes -= 10
    return counter


def calculate_nickels(centes):
    counter = 0
    while centes >= 5:
        counter += 1
        centes -= 5
    return counter


def calculate_pennies(centes):
    counter = 0
    while centes >= 1:
        counter += 1
        centes -= 1
    return counter


if __name__ == "__main__":
    main()
