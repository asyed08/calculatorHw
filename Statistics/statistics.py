from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from CsvReader.CsvReader import CsvReader


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/UnitTestStats.csv').data
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result
