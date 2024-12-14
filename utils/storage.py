import pickle
import os
from models.address_book import AddressBook

ADDRESSBOOK_FILE = "contacts/addressbook.pkl"

def save_data(book: AddressBook, filename=ADDRESSBOOK_FILE):

    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print(f"Address book saved to {filename}.")

def load_data(filename=ADDRESSBOOK_FILE) -> AddressBook:

    if os.path.exists(filename):
        with open(filename, "rb") as f:
            print(f"Address book loaded from {filename}.")
            return pickle.load(f)
    print(f"No saved address book found. Starting with a new one.")
    return AddressBook()
