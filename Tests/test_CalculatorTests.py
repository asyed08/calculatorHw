import unittest
from pprint import pprint

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_subtraction(self):
        test_data = CsvReader('Tests/Data/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data = CsvReader('Tests/Data/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('Tests/Data/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('Tests/Data/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), round(float(row['Result']),9))
            self.assertEqual(self.calculator.result, round(float(row['Result']),9))

    def test_square(self):
        test_data = CsvReader('Tests/Data/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareroot(self):
        test_data = CsvReader('Tests/Data/squareroot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), round(float(row['Result']),8))
            self.assertEqual(self.calculator.result, round(float(row['Result']),8))

   def test_median(self):
        test_data = CsvReader("Tests/Data/median.csv").data
        pprint(test_data)
        for row in test_data:
           result = float(row['Result'])
           self.assertEqual(self.statistics.med(row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6'], row['Value 7']), result)
           self.assertEqual(self.statistics.result, result)

 def test_mode(self):
        test_data = CsvReader("Tests/Data/mode.csv").data
        pprint(test_data)
        for row in test_data:
           result = int(row['Result'])
           self.assertEqual(self.statistics.mode(row['Value 1'], row['Value 2']), result)
           self.assertEqual(self.statistics.result, result)


if __name__ == '__main__':
    unittest.main()

