from math import sqrt


def create_dict(n):
    dictionary = {i: round((sqrt(i)), 5) for i in range(1, (n+1))}
    return dictionary


def run():
    n = int(input("How many numbers do you want?: "))
    dictionary = create_dict(n)
    print(dictionary)


if __name__ == "__main__":
    run()