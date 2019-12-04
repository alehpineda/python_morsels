from collections import OrderedDict
from collections.abc import MutableSet

class OrderedSet(object):
    def __init__(self, lista):
        self.lista = OrderedDict.fromkeys(lista)
        #self.lista = MutableSet(lista)
    
    
    def __iter__(self):
        for element in self.lista:
            yield element
    

    def __len__(self):
        return len(self.lista)

    
    def __contains__(self, key):
        return key in self.lista


    # Bonus 1 - add and discard
    def add(self, palabra):
        self.lista.__setitem__(palabra, palabra)


    def discard(self, palabra):
        try:
            del self.lista[palabra]
        except KeyError:
            pass


    # Bonus 2 - Equality
    def __eq__(self, other):
        if not isinstance(other, OrderedSet):
            return self.lista.keys()==other
        
        return list(self.lista.keys())==list(other.lista.keys())

    # Bonus 3 - Supports index
    def __getitem__(self, i):
        return list(self.lista.items())[i][0]