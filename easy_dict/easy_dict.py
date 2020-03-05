class EasyDict(object):
    def __init__(self, _dict={}, normalize=False, **kwargs):

        self._normalize = normalize

        for key, value in _dict.items():
            self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def __getitem__(self, key):
        return getattr(self, self.normalized(key))

    def __setitem__(self, key, value):
        setattr(self, self.normalized(key), value)

    def get(self, key, default=None):
        return getattr(self, self.normalized(key), default)

    def __eq__(self, other):
        if isinstance(other, EasyDict):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def normalized(self, key):
        if self._normalize:
            return key.replace(' ', '_')
        else:
            return key
