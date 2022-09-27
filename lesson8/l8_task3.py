import value as value

some_list = ['a', 'b', 'c', 'd', 'e']
dictionary = {}


def create_dict(*args, **kwargs) -> dict:
    for index, val in enumerate(some_list):
        dictionary[index] = val
    return dictionary


print(create_dict(some_list, dictionary))
