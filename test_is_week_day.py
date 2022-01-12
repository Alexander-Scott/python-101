import unittest
import datetime
from is_week_day import IsWeekDay
# How to run all tests:
# python3 -m unittest discover .

class Test_Week_Day(unittest.TestCase):
   
    def test_assert_currentdate_is_a_weekday(self):
       today = datetime.datetime(2022,1,12)
       #is_weekday = IsWeekDay() # Arrange
       return_value = IsWeekDay.check_if_today_is_a_weekday(today)  # Act
       self.assertTrue(return_value) # Assert 
    
    def test_assert_currentdate_not_a_weekday(self):
       today = datetime.datetime(2020,8,16)
       #is_weekday = IsWeekDay() # Arrange
       return_value = IsWeekDay.check_if_today_is_a_weekday(today)  # Act
       self.assertFalse(return_value) # Assert 

if __name__ == ' __main__':
    unittest.main()
