from Calculator.Calculator import Calculator
from Statistics.populationmean import popmean
from pprint import pprint
class Statistics(Calculator):
    def __init__(self):
        super().__init__()

    def popmean(self, a, b, c):
        self.result = popmean(a, b, c)
        pprint(self.result)
        return self.result

