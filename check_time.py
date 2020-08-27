from datetime import datetime


def check_time(time):
    now = datetime.now().time()  # time object
    # print(time, (':').join(str(now).split(':')[:2]))
    return time == (':').join(str(now).split(':')[:2])
