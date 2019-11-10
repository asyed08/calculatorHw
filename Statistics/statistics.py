from Calculator.Calculator import Calculator
from Statistics.population_variance import population_variance
from Statistics.population_standard_deviation import population_standard_deviation


from CsvReader.CsvReader import CsvReader
from Statistics.mean import mean

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def pop_variance(self, a, b, c, d, e, f,):
        self.result = population_variance(a, b, c, d, e, f)
        return self.result

    def population_standard_deviation(self, a, b, c, d, e, f):
        self.result = population_standard_deviation(a, b, c, d, e, f)
        return self.result