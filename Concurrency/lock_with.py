# lock_with.py
#
# A simple example of using a mutex lock for critical sections.
# Uses the context manager feature of Python 2.6.

import threading
import time

x      = 0                   # A shared value
x_lock = threading.Lock()    # A lock for synchronizing access to x

COUNT = 1000000
def foo():
    global x
    for i in range(COUNT):
        with x_lock:
            x += 1

def bar():
    global x
    for i in range(COUNT):
        with x_lock:
            x -= 1
def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()

        if 'log-time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log-name'][name] = int((te - ts) * 1000)
        else:
            print('%r %2.2f ms' % (method.__name__.upper(), (te - ts) * 1000))

        return result
    return timed

@timeit
def main():

    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(x)


if __name__ == '__main__':
    main()