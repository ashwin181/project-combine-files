import pyexcel as excel
import unittest
import combineCSV

class Test(unittest.TestCase):

    def test_small_merge(self):
        combineCSV.merge_csv(['','./fixtures/accessories.csv', './fixtures/clothing.csv', 'test.csv'])
        expected_sheet = excel.load("test.csv", name_columns_by_row=0)
        actual_sheet = excel.load("./test/test1.csv", name_columns_by_row=0)
        assert actual_sheet.to_dict() == expected_sheet.to_dict()

    def test_large_merge(self):
        combineCSV.merge_csv(['','./fixtures/clothing.csv', './fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv','./fixtures/clothing.csv', 'test.csv'])
        expected_sheet = excel.load("test.csv", name_columns_by_row=0)
        actual_sheet = excel.load("./test/test2.csv", name_columns_by_row=0)
        assert actual_sheet.to_dict() == expected_sheet.to_dict()
        
    def test_error_file_not_exist(self):
        self.assertRaises(Exception, combineCSV.merge_csv(['./fixtures/accessories.csv', 'random3.csv', 'test.csv']))
        self.assertRaises(Exception, combineCSV.merge_csv(['./random1.csv', 'random2.csv', 'test.csv']))
        self.assertRaises(Exception, combineCSV.merge_csv(['./accessories.csv', 'random3.csv']))

if __name__ == '__main__':
    unittest.main()
