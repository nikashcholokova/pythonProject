import requests
import pprint

unic_for_dict = '\U0001F937'
URL = 'https://script.google.com/macros/s/AKfycbwQo5l37-lE3cu9BUN8gqhW2nKfI0x7uSKq_wycFoBQ_p2-Yl97pR1z0a1S8zWybQuP4Q/exec'


def get_data(url: str = None) -> dict:
    """
    get data from given url
    :param url: str
    :return: dict
    """
    response = requests.get(url)
    data = response.json()

    return data


res = get_data(URL)

pprint.pprint(res)

assert type(get_data(URL)) == dict, "Sorry, but isn't a dict " + unic_for_dict
