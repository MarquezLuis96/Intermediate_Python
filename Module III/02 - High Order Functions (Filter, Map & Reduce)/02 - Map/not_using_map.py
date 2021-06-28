#   Powering using list comprehensions
##


def powering(list):
    powered_list = [i**2 for i in list]
    return powered_list


def run():
    list = [0,1,2,3,4,5,6,7,8,9]
    powered = powering(list)

    print("List:")
    print(list)
    print("Powered List:")
    print(powered)


if __name__ == "__main__":
    run()