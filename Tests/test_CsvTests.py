import unittest
from CsvReader.CsvReader import ClassFactory, CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/addition.csv')

    def test_return_data_as_objects(self):
        rows = self.csv_reader.return_data_as_objects('row')
        self.assertIsInstance(rows, list)
        test_class = ClassFactory('row', self.csv_reader.data[0])
        for row in rows:
            self.assertEqual(row.__name__, test_class.__name__)

if __name__ == '__main__':
    unittest.main()