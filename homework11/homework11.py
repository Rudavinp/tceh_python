from contextlib import contextmanager
import time


@contextmanager
def time_speed(value):
    start = time.time()
    yield value
    finish = time.time()
    print('[Finished in {}s]'.format(finish - start))


@contextmanager
def catch_all_errors(value):
    try:
        yield value
    except Exception as e:
        print('Ups error!', e)
