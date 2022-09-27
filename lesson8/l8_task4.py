import time


def what_time_is_it_now(*args):
    current_time = time.strftime('%H:%M')
    return current_time


def countdown(sec=None) -> int:
    for i in range(sec):
        print(str(sec - i))
        time.sleep(1)
    return i


(countdown(3))
print(what_time_is_it_now())







# for i in range(seconds):
#     print(str(seconds - i) + " Seconds Left")
#     time.sleep(1)
#
#
# print("Boom Time is Up ")
