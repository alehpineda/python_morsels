from collections import OrderedDict

class OrderedSet(object):
    def __init__(self, lista):
        self.lista = lista
    
    
    def __iter__(self):
        for element in self.lista:
            yield element
    

    def __len__(self):
        return len(self.lista)

    
    def __contains__(self, key):
        return key in self.lista
