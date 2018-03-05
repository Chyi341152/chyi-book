# recvcount.py
#
# Example of a co-routine

def coroutine(func):
    def start(*args, **kwargs):
        c = func(*args, **kwargs)
        c.__next__()
        return c
    return start

@coroutine
def recv_count():
    try:
        while True:
            n = (yield) # Yield expression
            print("T-minus", n)
    except GeneratorExit:
        print("Kaboom!")

r = recv_count()

for i in range(5,0,-1):
    r.send(i) # pushing values into the pipeline using .send()

r.close()

