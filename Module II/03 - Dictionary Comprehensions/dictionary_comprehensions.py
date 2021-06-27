def create_dict(n):
    dictionary = {i: i**3 for i in range(1, (n+1)) if i%3 != 0}
    return dictionary


def run():
    n = int(input("How many numbers do you want?: "))
    dictionary = create_dict(n)
    print(dictionary)


if __name__ == "__main__":
    run()