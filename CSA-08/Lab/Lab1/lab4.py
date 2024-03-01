from datetime import datetime
class DateHandler:
    def format_date(self, date):
        print(date.strftime("%d/%m/%Y"))
    def get_between_days(self, start_date, end_date):
        print((end_date-start_date).days)
d1 = DateHandler()
d1.format_date(2023, 11, 3)