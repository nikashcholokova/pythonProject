from typing import Any
from lesson5 import l5_task1


def check_default_range(range_star: int, range_end: int, default: int = 99) -> bool:
    """
    check default range 
    :param range_star: int
    :param range_end: int
    :return: bool 
    """

    if range_star < default < range_end:
        return True
    return False


def is_int(x: Any) -> bool:
    """
    check is int
    :param x: any type
    :return: bool
    """

    if type(x) == int:
        return True
    return False


def is_valid_lenght(row: str, lenght: int = 150) -> str:
    """

    :rtype: object
    :param row: str
    :param lenght: int
    :return: str
    """

    if len(row) > lenght:
        return row[:lenght - 3] + '...'
    else:
        return row


def create_file(path_to_file: str = 'test_file.txt'):
    open(path_to_file, 'x')
    # print(file.name)
    # print(file.mode)


def appending_to_file(dictionary: str, path_to_file: str = 'test_file.txt'):
    file = open(path_to_file, 'a')
    file.write(dictionary + '\n')
    file.close()


if __name__ == "__main__":
    # print(l5_task1.get_data)
    # create_file()
    appending_to_file("Hello")

    assert check_default_range(0, 100), "Sorry, but isn't valid range " + "\U0001F937"
    assert is_int(8), "Isn't int"
    assert is_valid_lenght("*" * 190) == "*" * 147 + "...", "Invalid lenght"

