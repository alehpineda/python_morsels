class float_range(object):
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        (self.start, self.stop, self.step) = (start, stop, step)

    def __iter__(self):
        i = self.start
        if self.step > 0:
            while i < self.stop:
                yield i
                i += self.step
        else:
            while i > self.stop:
                yield i
                i += self.step

    def __len__(self):
        div, mod = divmod(self.stop-self.start, self.step)
        return max(0, int(div if mod == 0 else div+1))

    def __reversed__(self):
        i = self.start + (len(self)-1)*self.step
        for _ in range(len(self)):
            yield i
            i -= self.step

    def __eq__(self, other):
        if isinstance(other, float_range):
            return len(self) == len(other) and list(self) == list(other)
        elif isinstance(other, range):
            return len(self) == len(other)
        else:
            return True

    def __ne__(self, other):
        return not self.__eq__(other)
