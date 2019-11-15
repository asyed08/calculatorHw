from Calculator.Calculator import Calculator
from Statistics.populationmean import popmean
from Statistics.samplemean import sampmean
from Statistics.median import median
from Statistics.mode import mode
from Statistics.PopulationVar import population_variance
from Statistics.PopulationSD import population_standard_deviation
from Statistics.SampleSD import sample_standard_deviation
from Statistics.zscore import zscore
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

    def pop_variance(self, a, b, c, d, e, f,):
        self.result = population_variance(a, b, c, d, e, f)
        return self.result

    def population_standard_deviation(self, a, b, c, d, e, f):
        self.result = population_standard_deviation(a, b, c, d, e, f)
        return self.result
      
    def mode(self, a, b, c, d, e):
        self.result = mode(a, b, c, d, e)
        return self.result

    def sample_standard_deviation(self,samplesize,a,b,c,d,e,f,g,h):
        self.result = sample_standard_deviation(samplesize,a,b,c,d,e,f,g,h)
        return self.result

    def zscore(self, datapoint, a,b,c,d,e,f):
        self.result = zscore(datapoint,a,b,c,d,e,f)
        return self.result
