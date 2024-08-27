from cs50 import get_string


def main():
    # here
    s = get_string("Text: ")
    words = count_words(s)
    letters = (count_letters(s) / words) * 100
    sentences = (count_sentences(s) / words) * 100
    index = 0.0588 * letters - 0.296 * sentences - 15.8
    index = round(index)
    if index <= 0:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    for i in range(0, 16):
        if index == i:
            print(f"Grade {i}")


def count_letters(s):
    # here
    numbers = 0
    for i in range(0, len(s)):
        if s[i].isalpha():
            numbers += 1
    return numbers


def count_words(s):
    numbers = 0
    for lap in s:
        if lap == " ":
            numbers += 1
    return numbers + 1


def count_sentences(s):
    summe = 0
    array = ["!", "?", "."]
    for idk in s:
        if idk in array:
            summe += 1
    return summe


if __name__ == "__main__":
    main()
