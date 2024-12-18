from colorama import Fore, Style, init
from utils.parser import parse_input
from utils.storage import save_data, load_data
from commands.add import add_contact
from commands.change import change_contact
from commands.phone import show_phone
from commands.show_all import show_all
from commands.add_birthday import add_birthday
from commands.show_birthday import show_birthday
from commands.birthdays import birthdays
from commands.delete import delete_contact
from commands.help import help_command
from models.address_book import AddressBook

init(autoreset=True)

def main():

    book = load_data()

    print(Fore.CYAN + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            print(Fore.GREEN + "Good bye!")
            break
        elif command == "hello":
            print(Fore.YELLOW + "How can I help you?")
        elif command == "help":
            print(Fore.MAGENTA + help_command())
        elif command == "add":
            print(Fore.GREEN + add_contact(args, book))
        elif command == "change":
            print(Fore.GREEN + change_contact(args, book))
        elif command == "phone":
            print(Fore.CYAN + show_phone(args, book))
        elif command == "all":
            print(Fore.WHITE + show_all(book))
        elif command == "add-birthday":
            print(Fore.GREEN + add_birthday(args, book))
        elif command == "show-birthday":
            print(Fore.CYAN + show_birthday(args, book))
        elif command == "birthdays":
            print(Fore.YELLOW + birthdays(args, book))
        elif command == "delete":
            print(Fore.RED + delete_contact(args, book))
        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()
