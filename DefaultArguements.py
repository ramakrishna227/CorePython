import time


def print_time(default_time=time.ctime()):
    print("default time is", default_time, "current time is", time.ctime())
    time.sleep(3)
    print("default time is", default_time, "current time is", time.ctime())


if __name__ == '__main__':
    print_time()
