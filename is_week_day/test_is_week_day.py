import unittest
import datetime
from unittest.mock import patch
from is_week_day import IsWeekDay, main_execution


class Test_Week_Day(unittest.TestCase):
    def test_assert_currentdate_is_a_weekday(self):
        today = datetime.datetime(2022, 1, 12)
        # is_weekday = IsWeekDay() # Arrange
        return_value = IsWeekDay.check_if_today_is_a_weekday(today)  # Act
        self.assertTrue(return_value)  # Assert
def test_assert_currentdate_not_a_weekday(self):
        today = datetime.datetime(2022, 1, 16)
        # is_weekday = IsWeekDay() # Arrange
        return_value = IsWeekDay.check_if_today_is_a_weekday(today)  # Act
        self.assertFalse(return_value)  # Assert

    def test_main_execution(self):
        today = datetime.datetime(2022, 1, 13)
        with patch("datetime.now", today, create=True):
            self.assertTrue(main_execution())


if __name__ == " __main__":
    unittest.main()
