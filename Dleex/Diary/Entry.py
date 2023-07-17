class Entry:
    # __uniqueId = 0
    # __title = ""
    # __body = ""

    def __int__(self, title: str, body:str):
        self.__title = title
        self.__body = body

    def updateGist(self, title, body):
        self.__title = title
        self.__body = body

    def setId(self, unique_id):
        self.__uniqueId = unique_id

    def get_id(self):
        return self.__uniqueId

