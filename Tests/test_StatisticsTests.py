import unittest

from Statistics.statistics import Statistics
from CsvReader.CsvReader import CsvReader

import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/PopulationData.csv')



    def test_instantiate_statscalculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_pop_mean_statistics(self):
        answers = CsvReader('Tests/Data/StatsAnswers.csv').data
        test_data = CsvReader('Tests/Data/PopulationData.csv').data
        pprint(answers)
        pprint(test_data)
        pprint(self.statistics.popmean(test_data))
        for row in answers:
            pprint(int(row['Population Mean']))
            self.assertEqual(self.statistics.popmean(test_data), int(row['Population Mean']))


if __name__ == '__main__':
    unittest.main()