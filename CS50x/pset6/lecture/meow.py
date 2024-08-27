def main():
    height = get_height()
    for i in range(height):
            print("meow")

def get_height():
    while True :
        try:
            n = int(input("height is :"))
            if n > 0:
                break
        except ValueError:
            print("this is not a number")
    return n

main()