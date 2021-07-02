#
# #


from os import remove


def create_file(file_dir: str):
    with open(file_dir, "w") as f:
        pass
    f.close()


def read_INT_in_file(file_dir: str):
    numbers = []

    with open(file_dir, "r", encoding="UTF-8") as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)
    f.close()


def read_file(file_dir: str):
    lines = []

    with open(file_dir, "r", encoding="UTF-8") as f:
        for line in f:
            lines.append(line[0:line.__len__()-1:])
        print(lines)
    f.close()


def write_file():
    names = ["Luis","Facundo","Christian","Jonathan","Rodrigo","Carlos","Diego", "Matías"]
    with open("./Files/names.txt", "w", encoding="UTF-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
    f.close()


def delete_file_content(file_dir: str):
    with open(file_dir, "w") as f:
        pass
    f.close()


def delete_file(file_dir: str):
    remove(file_dir)


def run():
    # print("Numbers:")
    # read_INT_in_file("./Files/numbers.txt")


    print("Names:")
    write_file()
    read_file("./Files/names.txt")


if __name__ == "__main__":
    run()