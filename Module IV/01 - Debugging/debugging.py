def lambdas(number: int, rang: int):
    y = list(filter(lambda x : number%x == 0, range(1,rang+1)))
    print(y)


def divisor(number: int, rang: int):
    divisor_list = [i for i in range(1, rang+1) if number%i == 0]
    print(divisor_list)


def run():
    number = int(input("What's the number you want to know the dividers: "))
    rang = int(input("What's the range? : 1 - "))

    print("\nResult using List Comprehensions: ")
    divisor(number, rang)

    print("\nResult using Lambda functions: ")
    lambdas(number, rang)


if __name__ == "__main__":
    run()