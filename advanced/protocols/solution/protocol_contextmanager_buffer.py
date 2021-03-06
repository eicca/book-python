"""
>>> from inspect import isclass, ismethod
>>> assert isclass(File)
>>> assert hasattr(File, 'append')
>>> assert hasattr(File, '__enter__')
>>> assert hasattr(File, '__exit__')
>>> assert ismethod(File(None).append)
>>> assert ismethod(File(None).__enter__)
>>> assert ismethod(File(None).__exit__)

>>> with File('_temporary.txt') as file:
...    file.append('One')
...    file.append('Two')
...    file.append('Three')
...    file.append('Four')
...    file.append('Five')
...    file.append('Six')

>>> open('_temporary.txt').read()
'One\\nTwo\\nThree\\nFour\\nFive\\nSix\\n'
"""
from sys import getsizeof


class File:
    BUFFER_LIMIT: int = 100

    filename: str
    content: list[str]

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.content = list()

    def append(self, line: str) -> None:
        self.content.append(line + '\n')
        if getsizeof(self.content) >= self.BUFFER_LIMIT:
            self._write()

    def _write(self):
        with open(self.filename, mode='a') as file:
            file.writelines(self.content)
        self.content = []

    def __enter__(self) -> 'File':
        with open(self.filename, mode='w') as file:
            file.writelines(self.content)
        return self

    def __exit__(self, *arg) -> None:
        self._write()
