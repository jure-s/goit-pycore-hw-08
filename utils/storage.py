import pickle
import os
from models.address_book import AddressBook

ADDRESSBOOK_FILE = "contacts/addressbook.pkl"

def ensure_storage_directory():

    directory = os.path.dirname(ADDRESSBOOK_FILE)
    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory, exist_ok=True)

def save_data(book: AddressBook, filename=ADDRESSBOOK_FILE):

    ensure_storage_directory()
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print(f"Address book saved to {os.path.abspath(filename)}.")

def load_data(filename=ADDRESSBOOK_FILE) -> AddressBook:

    ensure_storage_directory()
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            print(f"Address book loaded from {os.path.abspath(filename)}.")
            return pickle.load(f)
    print(f"No saved address book found in {os.path.abspath(filename)}. Starting with a new one.")
    return AddressBook()
