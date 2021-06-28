#   Filtering odds using lists comprehensions
# #


def filter_odds(complete_list):
    list = [i for i in complete_list if i%2 != 0]
    return list


def run():
    my_list = [1,5,9,7,5,3,2,8,4,6,10,11,15,14,18,19,13,23,24,22,20,82,46,64,69,96,77,26,48,25,12]
    odds_list = filter_odds(my_list)
    print(odds_list)


if __name__ == "__main__":
    run()