from threading import Thread
import time


def calc_squares():
    for i in range(1, 11):
        time.sleep(0.05)
        print(f"Квадрат {i} = {i ** 2}")


def calc_cubes():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f"Куб {i} = {i ** 3}")


if __name__ == "__main__":
    thread1 = Thread(target=calc_squares)
    thread2 = Thread(target=calc_cubes)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
