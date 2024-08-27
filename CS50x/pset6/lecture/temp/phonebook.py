import csv
from cs50 import get_string


name = get_string("give me a name :")
number = get_string("give me a phone number :")

with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])