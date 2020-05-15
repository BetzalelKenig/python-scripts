

def func_logger(func):
    import logging
    logging.basicConfig(
        filename=f'{func.__name__}.log', level=logging.INFO,
        format='%(asctime)s:%(name)s:%(message)s')

    def wrapper(*args, **kwargs):
        logging.info(
            f'Run with args: {args}, and kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper


def func_timer(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print(f'{func.__name__} run in: {end} sec')
        return result
    return wrapper
import time

@func_timer
def print_msg(msg):
    time.sleep(1)
    print(msg)


print_msg('Hi')
