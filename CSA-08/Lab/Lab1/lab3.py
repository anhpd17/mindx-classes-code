from datetime import datetime

class CustomDate:
    def __init__(self):
        self.now = datetime.now()
    def get_date(self):
        print(now.strftime("%d/%m/%Y"))
    def get_time(self):
        print(now.strftime("%H:%M:%S"))

