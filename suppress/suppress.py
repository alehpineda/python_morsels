from contextlib import contextmanager


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
