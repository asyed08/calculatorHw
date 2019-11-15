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




if __name__ == '__main__':
    unittest.main()