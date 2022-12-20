from pathlib import Path


class Day:
    def __init__(self, num):
        self._num = str(num).rjust(2)
        self.valid_file = Path("inputs") / f"{self._num}.txt"
        self.test_file = Path("inputs") / f"{self._num}_test.txt"

    @property
    def test_input(self):
        return open(self.test_file, "r")

    @property
    def valid_input(self):
        return open(self.valid_file, "r")

    @property
    def test_content(self):
        return self.test_input.read()

    @property
    def valid_content(self):
        return self.valid_input.read()

    @property
    def test_lines(self):
        return self.test_content.splitlines()

    @property
    def valid_lines(self):
        return self.valid_content.splitlines()
