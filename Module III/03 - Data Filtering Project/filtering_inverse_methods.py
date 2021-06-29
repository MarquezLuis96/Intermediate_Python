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


def filtering_python_by_high_order_functions():
    python_list = list(filter(lambda worker: worker["language"].lower() == "python", DATA))
    python_list = list(map(lambda worker: worker["name"], python_list))
    print("\nPython Developers:")
    print(python_list)


def filtering_google_workers_by_high_order_functions():
    google_list = list(filter(lambda worker: worker["organization"].lower() == "google", DATA))
    google_list = list(map(lambda worker: worker["name"], google_list))
    print("\nGoogle Developers:")
    print(google_list)


def filtering_adults_by_lists_comprehensions():
    adults_list = [worker["name"] for worker in DATA if worker["age"] >= 18]
    print("\n+18 Developers:")
    print(adults_list)


def filtering_olds_by_lists_comprehensions():
    olds_list = [worker | {"old" : worker["age"] >= 70} for worker in DATA]
    print("\n+70 Developers:")
    print(olds_list)


def run():
    filtering_python_by_high_order_functions()
    filtering_google_workers_by_high_order_functions()
    filtering_adults_by_lists_comprehensions()
    filtering_olds_by_lists_comprehensions()

if __name__ == "__main__":
    run()