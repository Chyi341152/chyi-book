import sys
import os.path

def main():
    sys.argv[:] = sys.argv[1:] # Must rewrite the command line arguments
    progname = sys.argv[0]
    sys.path.insert(0, os.path.dirname(progname))
    with open(progname, 'rb') as fp:
        code = compile(fp.read(), progname, 'exec')

    globs = {
        '__file__' : progname,
        '__name__' : '__main__',
        '__package__' : None,
        '__cached__' : None
    }
    exec(code, globs)
