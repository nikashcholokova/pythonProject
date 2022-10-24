import value as value

inpt_list = ['a', 'b', 'c', 'd', 'e']


def create_dict(some_list: list) -> dict:
    dictionary = {}
    for index, val in enumerate(some_list):
        dictionary[index] = val
    return dictionary


print(create_dict(inpt_list))
