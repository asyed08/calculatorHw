from Calculator.Calculator import Calculator


from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def popmean(self):
        self.result = mean(self.data)
        return self.result

