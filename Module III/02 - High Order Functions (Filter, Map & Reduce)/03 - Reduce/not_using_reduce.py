#   Not using reduce
##

def reducing(my_list):
    result = 0
    for i in my_list:
        result *= i
    return result


def run():
    my_list = [2,2,2,2,2]
    result = reducing(my_list)

    print("List: ")
    print(my_list)
    print("Result: " + str(result))


if __name__ == "__main__":
    run()