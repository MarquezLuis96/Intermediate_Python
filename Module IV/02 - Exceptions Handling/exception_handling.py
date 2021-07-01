#
# #


def palindrom(word):
    try:
        word = word[::-1]
    except TypeError:
        print("I execute myself only if an exception happens")
        print("You can't type only strings")
    else:
        print("I just execute myself only if no exceptions happens")
        print(word)
    finally:
        print("I always execute myself")


def run():
    word = input("Please, type a word: ")
    palindrom(word)


if __name__ == "__main__":
    run()