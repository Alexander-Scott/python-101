import datetime


class IsWeekDay:
    @staticmethod
    def check_if_today_is_a_weekday(date: datetime.datetime):
        today = date.weekday()
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        print(days[today])
        if today in [6, 5]:
            return False
        return True

    # @staticmethod
    # def my_method(val_1, val_2):
    #     return val_1 + val_2


def main_execution():
    today = datetime.datetime.now()
    return IsWeekDay.check_if_today_is_a_weekday(today)
