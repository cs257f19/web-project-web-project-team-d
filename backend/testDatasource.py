import unittest
from datasource import *

class DatasourceTester(unittest.TestCase):

    def setUp(self) -> None:
        self.ds = DataSource()
        user = 'beckerr2'
        password = 'barn787sign'
        self.ds.connect(user, password)

    #Ensures the 'spotlight' column of each row is true on true input
    def test_in_spotlight_true(self):
        input = "T"
        list = self.ds.getKickstartersInSpotlight(input)
        result = True
        for row in list:
            if row[10].upper() != input:
                result = False
                break
        self.assertTrue(result)

    # Ensures the 'spotlight' column of each row is NOT true on false input
    def test_in_spotlight_true_input_false(self):
        input = "F"
        list = self.ds.getKickstartersInSpotlight(input)
        result = True
        for row in list:
            if row[10].upper() != 'T':
                result = False
                break
        self.assertFalse(result)

    # Ensures the 'spotlight' column of each row is  false on false input
    def test_in_spotlight_false(self):
        input = "f"
        list = self.ds.getKickstartersInSpotlight(input)
        result = True
        for row in list:
            if row[10] != input:
                result = False
                break
        self.assertTrue(result)

    # Ensures the 'spotlight' column of each row is NOT false on true input
    def test_in_spotlight_false_input_true(self):
        input = "T"
        list = self.ds.getKickstartersInSpotlight(input)
        result = True
        for row in list:
            if row[10].upper() != 'F':
                result = False
                break
        self.assertFalse(result)

    # Ensures that the returned list is empty
    def test_in_spotlight_bad_input(self):
        input = 0
        list = self.ds.getKickstartersInSpotlight(input)

        self.assertTrue(len(list) == 0)


if __name__ == '__main__':
    unittest.main()
