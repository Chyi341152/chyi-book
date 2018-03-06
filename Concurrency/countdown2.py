# countdown2.py
#
# An example of launching a function into a separate thread

import time
import threading
import multiprocessing

def countdown(count):
    while count > 0:
        print("Counting down", count)
        count -= 1
        time.sleep(1)
    return

# Sample execution
# Creates a Thread object, but its run() method just calls the given function
t1 = threading.Thread(target=countdown, args=(10,))
t1.start()

t2 = threading.Thread(target=countdown, args=(20,))
t2.start()

p1 = multiprocessing.Process(target=countdown, args=(10,))
p1.start()

