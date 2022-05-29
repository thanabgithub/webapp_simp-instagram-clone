import os


def formatter():
    os.system("yapf -ir ./app --style setup.cfg -p --verbose --parallel")
