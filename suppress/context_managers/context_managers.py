import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('test_dir'):
    print(os.listdir())
