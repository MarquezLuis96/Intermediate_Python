import math


def pow_range(n_range):
    a = 0
    for n in n_range:
        n_range[a] = int(math.pow(2,n))
        a+=1
    print("\nPotencias: ")
    print(n_range)


def run():
    n_range = [0,1,2,3,4,5,6,7,8,9,10]
    pow_range(n_range)


if __name__ == "__main__":
    run()