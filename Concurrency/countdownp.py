# countdown.py
#
# An example of defining a thread as a class

import time
import multiprocessing

class CountdownProcess(multiprocessing.Process):
    def __init__(self,count):
        multiprocessing.Process.__init__(self)
        self.count = count

    def run(self):
        while self.count > 0:
            print("Counting down", self.count)
            self.count -= 1
            time.sleep(1)
        return

# Sample execution
# To launch, create thread objects and call start()
p1 = CountdownProcess(10)
p1.start()

p2 = CountdownProcess(20)
p2.start()

# Threads execute until the run() method stops

