import json
import time


def acdc_album():
    time_count = 0
    with open('acdc.json', 'r') as f:
        text = json.load(f)
    # pprint(text)
    for txt in text['album']['tracks']['track']:
        time_count += int(txt['duration'])

    return time_count


print(time.strftime('%H:%M:%S', time.gmtime(acdc_album())))
