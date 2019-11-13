from contextlib import ContextDecorator
from contextlib import contextmanager

class suppress1(ContextDecorator):
    def __init__(self, *exception_types):
        self.exception_types = exception_types
    

    def __enter__(self):
        return self


    def __exit__(self, exception_type, exception, traceback):
        self.exception = exception
        self.traceback = traceback
        return isinstance(exception, self.exception_types)


# Solution using contexmanager

class ExceptionInfo(object):
    exception = None
    traceback = None

@contextmanager
def suppress(*exception_types):
    info = ExceptionInfo()
    try:
        yield info
    except exception_types as error:
        info.exception = error
        info.traceback = error.__traceback__
