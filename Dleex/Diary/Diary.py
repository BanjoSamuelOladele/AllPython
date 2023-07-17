from Diary import Entry


class Diary:
    __entries = []

    def create_entry(self, title: str, body: str):
        entry = Entry.Entry(title, body)
        self.__entries.append(entry)
