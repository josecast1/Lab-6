# Jose Castro
def encode(password):
    encoded_password = []
    for i in range(len(password)):
        result = int(password[i])
        result = (result + 3) % 10
        encoded_password.append(str(result))

    encoded_pass = ''.join(encoded_password)
    print("Your password has been encoded and stored!\n")
    return encoded_pass


def decode(password):
    decoded = ''
    for idx in range(len(password)):
        if int(password[idx]) < 3:
            decoded += str(((int(password[idx]) - 3) + 10))
        else:
            decoded += str(int(password[idx]) - 3)
    return decoded

def main():
    menu = True
    while menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        print("Please enter an option: ", end='')

        menu_input = int(input())

        if menu_input == 1:
            print("Please enter your password to encode: ", end='')
            password = input()
            encoded_pass = encode(password)
        elif menu_input == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass} and the original password is {decoded_pass}.\n")
        else:
            menu = False


if __name__ == '__main__':
    main()