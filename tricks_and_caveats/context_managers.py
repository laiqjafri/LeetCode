import logging
from contextlib import contextmanager

logging.basicConfig(level=logging.INFO)


class ManagedFile:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger("ManagedFile")

    def __enter__(self):
        self.logger.info("Opening")
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.info("Closing")
        self.file.close()


@contextmanager
def file_context(name: str):
    file = None
    try:
        file = open(name, 'w')
        yield file
    finally:
        if file:
            file.close()


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print("\t" * self.level + text)


indent = Indenter()
indent.print("Starting Indenter")
with indent:
    indent.print("Hello")
    with indent:
        indent.print("Laiq")
        with indent:
            indent.print("Jafri")


with ManagedFile('./test.txt') as f:
    f.write("Hello Again\n")
    f.write("Bye Bye")


with file_context('./text2.txt') as f:
    f.write("Hello Mr. Context Manager\n")
    f.write("Good Bye")
