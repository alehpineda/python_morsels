from collections import UserDict


class EasyDict(UserDict):

    def __init__(self, _dict={}, normalize=False, **kwargs):
        self._normalize = normalize
        self.update(_dict)
        self.update(kwargs)

    @property
    def data(self):
        return self.__dict__

    def __getitem__(self, key):
        return self.__dict__[self.normalized(key)]

    def __setitem__(self, key, value):
        self.__dict__[self.normalized(key)] = value

    def normalized(self, key):
        return key.replace(' ', '_') if self._normalize else key
