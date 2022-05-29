import os


def format_file():
    os.system("yapf -ir .")


# docker exec -it app bash
# uvicorn yapf:format_file --reload --port 1000
