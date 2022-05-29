import os


def formatter():
    os.system("yapf -ir . --style setup.cfg -p --verbose --parallel")
