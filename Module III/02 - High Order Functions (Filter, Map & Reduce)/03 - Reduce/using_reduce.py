#   Using reduce
##


from functools import reduce


def reducing(my_list):
    result = reduce(lambda x, y: x*y, my_list)
    return result


def run():
    my_list = [2,2,2,2,2]
    result = reducing(my_list)

    print("List: ")
    print(my_list)
    print("Result: " + str(result))


if __name__ == "__main__":
    run()