"""create Time"""


class Time:
    def __init__(self, hour: int, minutes: int, second: int):
        self.hour = hour
        self.minutes = minutes
        self.second = second

    @property
    def hour(self, hour):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if 0 < hour <= 23:
            self.__hour = hour
        else:
            raise "hour match not allowed"

    @property
    def minutes(self, minutes):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if 0 < minutes <= 59:
            self.__minutes = minutes
        else:
            raise "minute match not allowed"

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        if 0 < second <= 59:
            self.__second = second
        else:
            raise "second match not allowed"

    def __str__(self):
        return f"time is {self.__hour} : {self.__minutes} : {self.__second}"


time = Time(20, 20, 40)
print(time)
