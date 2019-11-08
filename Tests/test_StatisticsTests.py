import unittest

from Statistics.statistics import Statistics
import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statscalculator(self):
        self.assertIsInstance(self.statistics, Statistics)

