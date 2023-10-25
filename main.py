# Jose Castro
def encode(password):
    password = input("Password:")

    for i in range(len(password)):
        result = int(password[i])
        result += 3
        print(result, end='')
    print("Your password has been encoded and stored!")

    return result
def main():
    menu = True
    while menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        print("Please enter an option: ")

        menu_input = input()

        if menu_input == 1:
            print("Please enter your password to encode: ")
            password = input()
            encode(password)
            encoded_pass = encode(password)
        elif menu_input == 2:

        else:
            menu = False


if __name__ == '__main__':
    main()