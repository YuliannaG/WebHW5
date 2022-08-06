import multiprocessing
from datetime import time, timedelta, datetime


def calculations(n):
    result = []
    i = 1
    while i <= n:
        if n % i == 0:
            result.append(i)
        i += 1
    return result


def factorize(*number, option: int = 1):
    start_time = datetime.now()
    match option:
        case 0:
            results = []
            for n in number:
                result = calculations(n)
                results.append(result)
        case 1:
            with multiprocessing.Pool(8) as p:
                results = p.map_async(calculations, list(number)).get()

    finish_time = datetime.now()
    length = finish_time - start_time
    print(length)
    print(results)
    return results
    # raise NotImplementedError()


if __name__ == '__main__':
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
