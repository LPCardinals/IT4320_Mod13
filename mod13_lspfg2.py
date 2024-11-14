import unittest
import re
from datetime import datetime



class TestInputs(unittest.TestCase):


    def test_symbol(self):
        self.assertTrue(re.match(r'^[A-Z]{1,7}$', 'AAPL'))
        self.assertTrue(re.match(r'^[A-Z]{1,7}$', 'MSFT'))
    
        self.assertFalse(re.match(r'^[A-Z]{1,7}$', 'aapl')) 
        self.assertFalse(re.match(r'^[A-Z]{1,7}$', 'APPLE123'))  
        self.assertFalse(re.match(r'^[A-Z]{1,7}$', ''))  

    def test_chart_type(self):
        self.assertIn('1', ['1', '2'])
        self.assertIn('2', ['1', '2'])

        self.assertNotIn('3', ['1', '2'])  
        self.assertNotIn('A', ['1', '2'])  

    def test_time_series(self):
        self.assertIn('1', ['1', '2', '3', '4'])
        self.assertIn('4', ['1', '2', '3', '4'])

        self.assertNotIn('5', ['1', '2', '3', '4']) 
        self.assertNotIn('0', ['1', '2', '3', '4']) 
        self.assertNotIn('A', ['1', '2', '3', '4']) 

    def test_start_date(self):
        self.assertTrue(self.is_valid_date_format('2023-01-01'))
        self.assertTrue(self.is_valid_date_format('2022-12-31'))

        self.assertFalse(self.is_valid_date_format('01-01-2023')) 
        self.assertFalse(self.is_valid_date_format('2023-1-1')) 
        self.assertFalse(self.is_valid_date_format('2023/01/01')) 

    def test_end_date(self):
        self.assertTrue(self.is_valid_date_format('2023-01-01'))
        self.assertTrue(self.is_valid_date_format('2022-12-31'))

        self.assertFalse(self.is_valid_date_format('01-01-2023')) 
        self.assertFalse(self.is_valid_date_format('2023-1-1')) 
        self.assertFalse(self.is_valid_date_format('2023/01/01')) 

    def is_valid_date_format(self, date_string):
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    unittest.main()
