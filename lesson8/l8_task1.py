coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def new_dict(*args, **kwargs) -> dict:
    dictionary = dict(zip(coin, code))
    return dictionary


print(new_dict(coin, code))
