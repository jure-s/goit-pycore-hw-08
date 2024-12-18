from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted."
        return f"Contact {name} not found."

    def get_upcoming_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=today.year)
                if next_birthday < today:
                    next_birthday = next_birthday.replace(year=today.year + 1)
                if 0 <= (next_birthday - today).days <= days:
                    upcoming.append((record.name.value, next_birthday.strftime("%d.%m.%Y")))
        return upcoming

    def __str__(self):
        return "\n".join([str(record) for record in self.data.values()])
