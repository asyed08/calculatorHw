import unittest

from Statistics.statistics import Statistics
import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/PopulationData.csv')

    def test_instantiate_statscalculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_pop_mean_statistics(self):
        test_data = CsvReader('Tests/Data/PopulationData.csv').data
        answers = CsvReader('Tests/Data/StatsAnswers.csv').data
        for column in test_data:
            result = self.answers(float(column['Population Mean']))
            self.assertEqual(self.statistics.popmean['Number'], result)


if __name__ == '__main__':
    unittest.main()