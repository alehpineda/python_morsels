from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *suppress_exception):
        self.suppress_exception = suppress_exception
        self._exception = None
        self._traceback = None
    

    def __enter__(self):
        return self


    def __exit__(self, exception, value, traceback):
        if exception and issubclass(exception, self.suppress_exception):
            self._exception = exception()
            self._traceback = traceback
            return True
        return False


    @property
    def exception(self):
        return self._exception


    @property
    def traceback(self):
        return self._traceback
