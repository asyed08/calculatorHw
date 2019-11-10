from Calculator.Calculator import Calculator
from Statistics.populationmean import popmean
from Statistics.samplemean import sampmean
from Statistics.median import median
from Statistics.mode import mode
from pprint import pprint
class Statistics(Calculator):
    def __init__(self):
        super().__init__()

    def popmean(self, a, b, c):
        self.result = popmean(a, b, c)
        pprint(self.result)
        return self.result

    def sampmean(self, samplesize, a, b, c, d, e):
        self.result = sampmean(samplesize, a, b, c, d, e)
        return self.result

    def median(self, a, b, c, d, e, f, g):
        self.result = median(a,b,c,d,e,f,g)
        return self.result

