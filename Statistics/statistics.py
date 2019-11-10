from Calculator.Calculator import Calculator
from Statistics.populationmean import popmean

class Statistics(Calculator):
    def __init__(self):
        super().__init__()

    def popmean(self, a, b, c):
        self.result = popmean(a, b, c)
        return self.result

