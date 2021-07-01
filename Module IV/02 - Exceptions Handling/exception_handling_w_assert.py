#
# #


def divisor(number):
    divisor_list = [i for i in range(1, 101) if number%i == 0]
    return divisor_list


def run():
    num = input("Ingrese un número: ")

    assert num.isnumeric(), print("You typed a string, you must to type a number.")
    num = int(num)
    print(divisor(num))
    print("Program Finished")


if __name__ == "__main__":
    run()