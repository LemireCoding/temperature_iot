class Temperature:
    id = 0
    datetime = ""
    temp = 0
    humidity = 0

    def __init__(self, datetime: datetime, temp: int, humidity: int):
        self.datetime = datetime
        self.temp = temp
        self.humidity = humidity