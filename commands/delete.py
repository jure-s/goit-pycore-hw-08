from utils.decorator import input_error
from models.address_book import AddressBook

@input_error
def delete_contact(args, book: AddressBook):

    name, *_ = args
    if book.find(name):
        book.delete(name)
        return f"Contact {name} deleted."
    return f"Contact {name} not found."
