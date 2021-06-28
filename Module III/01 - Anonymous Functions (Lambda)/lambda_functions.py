palindrome = lambda string: string[::-1]


def ask_name():
    string = input("What's the string you want to know if  a palindrome string? : ")
    return string


def check(string):
    if palindrome(string) == string:
        print("The string '" + string + "' is a palindrome")
    else:
        print("The string '" + string + "' isn't a palindrome")


def run():
    string = ask_name()
    check(string)


if __name__ == "__main__":
    run()