import datetime

class IsWeekDay:
    @staticmethod
    def check_if_today_is_a_weekday(date:datetime.datetime):
        today = date.weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(days[today])
        if today == 6 or today == 5:
            return False
        return True


if __name__ == "__main__":
    today = datetime.datetime.now()
    IsWeekDay.check_if_today_is_a_weekday(today)