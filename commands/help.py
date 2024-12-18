def help_command():
    """
    Повертає список підтримуваних команд.
    """
    return (
        "Supported commands:\n"
        "1. add [name] [phone] - Add a new contact or a phone to an existing contact.\n"
        "2. change [name] [old_phone] [new_phone] - Change a phone number for a contact.\n"
        "3. phone [name] - Show phone numbers for a contact.\n"
        "4. all - Show all contacts in the address book.\n"
        "5. add-birthday [name] [DD.MM.YYYY] - Add a birthday for a contact.\n"
        "6. show-birthday [name] - Show the birthday for a contact.\n"
        "7. birthdays - Show upcoming birthdays within the next week.\n"
        "8. delete [name] - Delete a contact and all its data.\n"
        "9. hello - Greet the bot.\n"
        "10. help - Show this list of commands.\n"
        "11. close or exit - Exit the program and save the address book."
    )
