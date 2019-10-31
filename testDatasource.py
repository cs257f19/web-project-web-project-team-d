import unittest
from datasource import *

class DatasourceTester(unittest.TestCase):

    def setUp(self) -> None:
        self.ds = DataSource()

    def test_in_spotlight_true(self):
        input = 'T'
        list = self.ds.getKickstartersInSpotlight(input)
        result = True
        for row in list:
            if row[10].upper() != 'T':
                result = False
                break
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()