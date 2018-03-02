import time

def timeit(func):
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()

        if 'log_time' in kwargs:
            name = kwargs.get('log-name', func.__name__.upper())
            kwargs['log-time'][name] = int((te-ts) * 1000)
        else:
            print('%r %2.2f ms'%(func.__name__.upper(), (te-ts) *1000))
        return result
    return timed

# A Non-Generator Soln
@timeit
def nonGenerator():
    wwwlog = open("access-log")
    total = 0
    for line in wwwlog:
        bytestr = line.rsplit(None,1)[1]
        if bytestr != '-':
            total += int(bytestr)

    print("Total", total)

# A Generator Solution
@timeit
def generator():
    wwwlog = open("access-log")
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
    bytes = (int(x) for x in bytecolumn if x != '-')

    print("Total", sum(bytes))

if __name__ == '__main__':
    nonGenerator()
    generator()