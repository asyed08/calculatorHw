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

    def test_median(self):
        test_data = CsvReader("Tests/Data/median.csv").data
        pprint(test_data)
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(
                self.statistics.median(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'],
                                    row['Value 6'], row['Value 7']), result)
            self.assertEqual(self.statistics.result, result)

    def test_mode(self):
        test_data = CsvReader("Tests/Data/mode.csv").data
        pprint(test_data)
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.statistics.mode(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5']), result)
            self.assertEqual(self.statistics.result, result)

    def test_populationstandarddeviation(self):
        test_data = CsvReader("Tests/Data/Population_Standard_Deviation.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(round(self.statistics.population_standard_deviation(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']),2), result)
            self.assertEqual(round(self.statistics.result,2), result)

    def test_populationvar(self):
        test_data = CsvReader("Tests/Data/PopulationVar.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(
                round(self.statistics.pop_variance(row['Value 1'], row['Value 2'], row['Value 3'],
                                                              row['Value 4'], row['Value 5'], row['Value 6']),2), result)
            self.assertEqual(round(self.statistics.result,2), result)

    def test_samplestandarddeviation(self):
        test_data = CsvReader("Tests/Data/Sample_Standard_Deviation.csv").data
        for row in test_data:
            result = float(row['Answer'])
            self.assertEqual(round(self.statistics.sample_standard_deviation(row['SampleSize'],row['Num1'],row['Num2'],row['Num3'],row['Num4'],row['Num5'],row['Num6'],row['Num7'],row['Num8']),2), result)
            self.assertEqual(self.statistics.result, result)

if __name__ == '__main__':
    unittest.main()