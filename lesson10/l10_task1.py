import datetime
import json
import requests
import csv


def check_currency(input_currency) -> bool:
    database = "symbols.json"
    data = json.loads(open(database).read())
    for current in data['symbols']:
        if current == input_currency:
            return True
    return False


def main():
    result = []
    url = "https://api.exchangerate.host/convert"
    currency_from = input("Enter currency from: ")
    currency_to = input("Enter currency to: ")
    while not(check_currency(currency_from)) and not(check_currency(currency_to)):
        print("Incorrect currencies entered")
        currency_from = input("Enter currency from: ")
        currency_to = input("Enter currency to: ")

    amount = input("Enter amount: ")
    date_range_end = datetime.datetime.now()
    date_range_start = datetime.datetime.strptime(input("Enter date value\n"), '%y-%m-%d')
    date_range = [date_range_start]
    while date_range_start < date_range_end:
        date_range_start += datetime.timedelta(days=1)
        date_range.append(date_range_start)
    for current in date_range:
        current_res = requests.get(url, params={
            "from": currency_from,
            "to": currency_to,
            "amount": amount,
            "date": current}).json()
        if current_res['success']:
            result.append((current_res['date'],
                          current_res['info']['rate'],
                          current_res['query']['amount'],
                          current_res['query']['from'],
                          current_res['query']['to'],
                          current_res['result']))
    f = open('result.csv', 'w')
    writer = csv.writer(f)
    writer.writerows(result)
    f.close()
    print(f"'date', 'from', 'to', 'amount', 'rate', 'result': {result}")


main()
