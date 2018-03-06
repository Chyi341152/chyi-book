# spam/__init__.py

__all__ = []

# explicit export decorator
def export(defn):
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn

from . import *
from . import *