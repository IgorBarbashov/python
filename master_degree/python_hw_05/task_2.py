from threading import Thread
import time

threads_number = 4
threads = []


def print_number():
    for i in range(1, 11):
        print(f"Число {i}")
        time.sleep(1)


if __name__ == "__main__":
    for i in range(threads_number):
        thread = Thread(target=print_number)
        threads.append(thread)
        thread.start()

    for tread in threads:
        thread.join()
