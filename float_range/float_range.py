class float_range(object):
    def __init__(self, *args):
        self.args = args
        self.numargs = len(self.args)
        if not self.numargs:
            raise TypeError("you need to write at least a value")
        elif self.numargs > 3:
            raise TypeError(f"Expected at most 3 arguments, got {self.numargs}")

    def __iter__(self):
        numargs = len(self.args)
        if numargs == 3 and self.args[2] < 0:
            (start, stop, step) = self.args

            i = start
            while stop < i:
                yield float(i)
                i += step

        else:
            if numargs == 1:
                stop = self.args[0]
                start = 0.0
                step = 1.0

            elif numargs == 2:
                (start, stop) = self.args
                step = 1.0

            elif numargs == 3:
                (start, stop, step) = self.args

            i = start
            while i < stop:
                yield float(i)
                i += step

    def __len__(self):
        return len(list(self.__iter__()))

    def __reversed__(self):
        return reversed(list(self.__iter__()))

    def __eq__(self, other):
        if isinstance(other, float_range):
            return len(self) == len(other) and list(self) == list(other)
        elif isinstance(other, range):
            return len(self) == len(other)
        else:
            return True

    def __ne__(self, other):
        return not self.__eq__(other)
