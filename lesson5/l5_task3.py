from lesson5 import l5_task1, MSG
import datetime
from lesson5.l5_task2 import is_valid_lenght, appending_to_file


def main_google(google_api_url):
    google_data = l5_task1.get_data(google_api_url)['data']
    for dictionary in google_data:
        if 90 <= dictionary['score'] <= 100 \
                and 9 <= dictionary['age'] <= 18 \
                and dictionary['has_rewards']:
            appending_to_file(
                is_valid_lenght(MSG.MSG_EXCELLENT_STUDENTS.format(datetime.datetime.now().date(),
                                                                  dictionary['name'],
                                                                  "\U0001F4AF",
                                                                  dictionary['score'],
                                                                  dictionary['notes'])))


if __name__ == "__main__":
    main_google(l5_task1.URL)
