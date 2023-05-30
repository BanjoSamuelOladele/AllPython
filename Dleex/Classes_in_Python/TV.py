"""Televison"""


class TV:
    status = bool
    volume = __volume = 0
    channel = __channel = 0

    @classmethod
    def television_status(cls):
        return cls.status

    @classmethod
    def status_(cls):
        cls.status = True

    @classmethod
    def television_volume(cls):
        return cls.volume

    @classmethod
    def increase_volume(cls):
        if 0 <= cls.volume <= 100:
            cls.volume += 1

    @classmethod
    def decrease_volume(cls):
        if 0 <= cls.volume < 100:
            cls.volume -= 1
            if cls.volume < 0:
                cls.volume = 0

    @classmethod
    def decrease_channel(cls):
        if 0 <= cls.channel < 100:
            cls.channel -= 1
            if cls.channel < 0:
                cls.channel = 0

    @classmethod
    def increase_channel(cls):
        if 0 <= cls.channel <= 10:
            cls.channel += 1

    @classmethod
    def television_channel(cls):
        return cls.channel


television = TV
volume = 0
# television.status = True
while volume < 5:
    television.increase_volume()
    volume += 1
print(television.television_volume())
print(television.television_channel())
