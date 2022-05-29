import os


def format_files():
    os.system("yapf -ir .")


# uvicorn yapf:format_file --reload --port 1000
