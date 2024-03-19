def parse_input(user_input):
    #розділити введений рядок на частини (команду та аргументи)
    parts = user_input.split()
    if not parts:
        raise ValueError("No command entered.")  #перевіряємо наявність команди
    cmd = parts[0].strip().lower()  #отримуємо команду і перетворюємо її на нижній регістр
    args = parts[1:]  #отримуємо аргументи
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments.")  #перевіркяєм правильність кількості аргументів
    name, phone = args
    if name in contacts:
        raise KeyError("Contact already exists.")  #перевіряєм, чи контакт вже існує
    contacts[name] = phone
    return "Contact added."

def change_contacts(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments.")  #перевіряєм правильність кількості аргументів
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact not found.")  #перевіряєм наявність контакту для зміни
    contacts[name] = phone
    return "Contact updated successfully."

def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid number of arguments.")  #перевірка правильності кількості аргументів
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found.")  #перевіряємо наявність контакту для відображення
    return contacts[name]

def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid number of arguments.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact not found.")
    return f"Phone number for {name}: {contacts[name]}"

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return all_contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, contacts))

            elif command == "change":
                print(change_contacts(args, contacts))

            elif command == "show":
                print(show_contact(args, contacts))
                
            elif command == "phone":  # обробка команди "phone"
                print(show_phone(args, contacts))

            elif command == "all":  #обробка команди "all"
                print(show_all_contacts(contacts))            

            else:
                print("Invalid command.")
        except (ValueError, KeyError) as e:
            print("Error:", e)  #оббробка помилок вводу користувача

if __name__ == "__main__":
    main()