# channel.py
#
# A minimal object that implements a message channel over a pair
# of file descriptors (like a pipe)

import pickle

class Channel(object):
    def __init__(self, out_f, in_f):
        self.out_f = out_f
        self.in_f = in_f

    def send(self, item):
        pickle.dump(item, self.out_f) # seriablizing an object
        self.out_f.flush()

    def recv(self):
        return pickle.load(self.in_f) # unserializing an object

# Example of using the channel
if __name__ == '__main__':
    import subprocess # Launching a subprocess
    # subprocess.Popen() Execute a child on in a new process
    p = subprocess.Popen(['python3', 'child.py'],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE)
    ch = Channel(p.stdin, p.stdout)

    ch.send("Hello World")
    print(ch.recv())
    ch.send(42)
    print(ch.recv())
    ch.send([1,2,3,4,5])
    print(ch.recv())
