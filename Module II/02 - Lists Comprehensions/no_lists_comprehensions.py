import math


def ask_int(str_message):
    integer = int(input(str_message))
    return integer


def fill_list(lista, top_range):
    for n in range(1, (top_range + 1)):
        lista.append(int(n))


def no_split_by_3(no_split_list, top_range):
    for n in range(1, (top_range + 1)):
        if n % 3 != 0:
            no_split_list.append(int(math.pow(n,2)))
        else:
            continue


def run():
    list = []
    no_split_list = []
    top_range = ask_int("Type how many numbers you want in the list: ")
    
    fill_list(list, top_range)
    print("The numbers from 1 to " + str(top_range) + " are: ")
    print(list)
    print("\n")

    no_split_by_3(no_split_list, top_range)
    print("\n\nThe powered numbers from 1 to " + str(top_range) + " no splitable by 3 are: ")
    print(no_split_list)
    print("\n")


if __name__ == "__main__":
    run()