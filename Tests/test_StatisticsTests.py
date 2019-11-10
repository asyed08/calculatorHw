import unittest

from Statistics.statistics import Statistics
from CsvReader.CsvReader import CsvReader

from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()



    def test_instantiate_statscalculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_pop_mean_statistics(self):
        test_data = CsvReader('Tests/Data/PopMean.csv').data
        for row in test_data:
            answer = float(row['Answer'])
            self.assertEqual(self.statistics.popmean(row['Num1'], row['Num2'], row['Num3']), answer)
            self.assertEqual(self.statistics.result, answer)

    def test_samp_mean_stats(self):
        test_data = CsvReader('Tests/Data/SampleMean.csv').data
        for row in test_data:
            answer = float(row['Answer'])
            self.assertEqual(self.statistics.sampmean(row['SampleSize'],row['Num1'],row['Num2'],row['Num3'],row['Num4'],row['Num5']),answer)
            self.assertEqual(self.statistics.result, answer)

if __name__ == '__main__':
    unittest.main()