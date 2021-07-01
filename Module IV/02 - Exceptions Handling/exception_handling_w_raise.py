#
# #


from typing import Type


def palindrom(word):
    try:
        if len(word) == 0: #or len(word) == 1:
            raise ValueError("You can't send an empty or len = 1 string, please type at least a string with len = 2")
        elif TypeError:
            raise TypeError("You must to type a string, not a number")
        else:
            word = word[::-1]
            print(word)
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)


def run():
    word = input("Please, type a word: ")
    palindrom(word)


if __name__ == "__main__":
    run()