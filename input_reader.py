class InputReader:

    def __init__(self, filename):
        self.filename = filename
        self.lines = None
        with open(file=self.filename) as file:
            self.lines = self.get_lines()

    def get_lines(self):
        with open(file=self.filename) as file:
            lines = [line.rstrip("\n") for line in file.readlines()]
            return lines
