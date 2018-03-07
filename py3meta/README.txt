Guide to the code samples:

debugly/
    Simple metaprogramming concepts illustrated with
    examples focused on debugging.

structly/
    Structure definitions with signatures.

typely/
    Structure definitions with type checking/validation
    and descriptors.

execly/
    Structure definitions with optimized code generation
    using exec().

importly/
    Importing structure definition files and generating
    code via import hooks.

Classes Deconstructed

    Consider a class:
        class Spam:
            def __init__(self, name):
                self.name = name
            def bar(self):
                print("I'm Spam.bar:%s" %self.name)
    Step 1:
        Body of class is isolated
        body = '''
            def __init__(self, name):
                self.name = name
            def bar(self):
                print("I'm Spam.bar:%s" %self.name)
            '''
    Step 2:
        The class dictionary is created
        clsdict = type.__prepare__('Spam', ())
    Step 3:
        Body is executed in returned dict
        exec(body, globals(), clsdict)
    Step 4:
        Class is constructed from its name, base classes, and the dictionary
        Spam = type('Spam',(),clsdict)
        >>> s = Spam('Guido')
        >>> s.bar()
