#
##


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Google',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Google',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Google',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Google',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


#


def filtering_python_by_list_comprehensions():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"].lower() == "python"]
    print("\nPython Developers:")
    print(all_python_devs)


def filtering_google_workers_by_list_comprehensions():
    all_google_workers = [worker["name"] for worker in DATA if worker["organization"].lower() == "google"]
    print("\nGoogle Developers:")
    print(all_google_workers)


def filtering_adults_by_high_order_functions():
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print("\n+18 Developers:")
    print(adults)


def filtering_olds_by_high_order_functions():
    old_people = list(map(lambda worker: worker | {"old": worker["age"] >= 70}, DATA))
    print("\n+70 Developers:")
    print(old_people)


def run():
    filtering_python_by_list_comprehensions()
    filtering_google_workers_by_list_comprehensions()
    filtering_adults_by_high_order_functions()
    filtering_olds_by_high_order_functions()


if __name__ == "__main__":
    run()