def run():
    my_list = [1, "Hello", True, 4.5]

    my_dict = {
        "firstname": "Luis",
        "lastname": "Marquez"
    }

    super_list = [
        {"firstname": "Luis","lastname": "Marquez"},
        {"firstname": "Jose","lastname": "Da Costa"},
        {"firstname": "Loly","lastname": "Arroyo"},
        {"firstname": "Maria","lastname": "Castro"},
        {"firstname": "Sofia","lastname": "Marquez"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5,6,7,8,9],
        "integer_nums": [-3,-2,-1,0,1,2,3,],
        "floating_nums": [1.1,4.5,6.43]
    }


    print("\nSuper Dictionary:")
    for key, value in super_dict.items():
        print(key, " = ", value)
    


    print("\nSuper List:")
    for list in super_list:
        for key, value in list.items():
            print(key, "\t = \t", value)


if __name__ == "__main__":
    run()