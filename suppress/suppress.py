from contextlib import ContextDecorator


class suppress(ContextDecorator):
    def __init__(self, *exception_types):
        self.exception_types = exception_types
    

    def __enter__(self):
        return self


    def __exit__(self, exception_type, exception, traceback):
        self.exception = exception
        self.traceback = traceback
        return isinstance(exception, self.exception_types)

