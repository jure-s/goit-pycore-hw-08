from utils.decorator import input_error
from models.field import Name, Phone
from models.address_book import AddressBook
from models.record import Record

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(Name(name))
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(Phone(phone))
    return message