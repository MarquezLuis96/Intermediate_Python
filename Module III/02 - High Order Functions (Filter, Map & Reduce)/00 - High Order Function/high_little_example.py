from typing import Callable


def greetings(function):
    function()


def hello():
    print("HELLO!!!")



def bye():
    print("BYE!!!")


def decide(string):
    if string.lower() == "hello":
        greetings(hello)
    elif string.lower() == "bye":
        greetings(bye)
    else:
        print("You typed a wring command")


def ask_greeting():
    string = input("What's your greeting? (hello/bye): ")    
    decide(string)


def run():
    ask_greeting()


if __name__ == "__main__":
    run()