import time

def countdownSec(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('TimeOver!\n')

class countdown(object): # iterator object
    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

# a generator function is mainly a more convenient way of writing an iteration
def countdownGen(n): # Generators
    print("Counting down from", n)
    while n > 0:
        # yield produces a value, but suspends the function
        yield n # Instead of return a value, you generate a series of value
        n -= 1
