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
