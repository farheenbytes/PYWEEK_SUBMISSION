contacts = []

# ---------------- ADD CONTACT ----------------
def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    contacts.append((name, number))
    save_contact(name, number)
    print("Contact saved!\n")


# ---------------- SAVE CONTACT TO FILE ----------------
def save_contact(name, number):
    with open("contacts.txt", "a") as file:
        file.write(name + " | " + number + "\n")


# ---------------- LOAD CONTACTS FROM FILE ----------------
def load_contacts():
    contacts.clear()
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                if "|" in line:
                    name, number = line.strip().split(" | ")
                    contacts.append((name, number))
    except FileNotFoundError:
        pass


# ---------------- READ CONTACTS ----------------
def read_contacts():
    load_contacts()
    print("\n--- Saved Contacts ---")
    for i, (name, number) in enumerate(contacts, start=1):
        print(f"{i}. {name} - {number}")
    print()


# ---------------- EDIT CONTACT ----------------
def edit_contact():
    load_contacts()
    read_contacts()

    if not contacts:
        print("No contacts to edit.\n")
        return

    choice = int(input("Enter contact number to edit: ")) - 1

    if 0 <= choice < len(contacts):
        name = input("Enter new name: ")
        number = input("Enter new number: ")
        contacts[choice] = (name, number)
        save_all_contacts()
        print("Contact updated!\n")
    else:
        print("Invalid choice.\n")


# ---------------- DELETE CONTACT ----------------
def delete_contact():
    load_contacts()
    read_contacts()

    if not contacts:
        print("No contacts to delete.\n")
        return

    choice = int(input("Enter contact number to delete: ")) - 1

    if 0 <= choice < len(contacts):
        contacts.pop(choice)
        save_all_contacts()
        print("Contact deleted!\n")
    else:
        print("Invalid contact.\n")


# ---------------- SAVE ALL CONTACTS ----------------
def save_all_contacts():
    with open("contacts.txt", "w") as file:
        for name, number in contacts:
            file.write(name + " | " + number + "\n")


# ---------------- MAIN MENU ----------------
while True:
    print("Contact System")
    print("\n1. Add Contact")
    print("2. Read Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    opt = input("Select option: ")

    if opt == '1':
        add_contact()

    elif opt == '2':
        read_contacts()

    elif opt == '3':
        edit_contact()

    elif opt == '4':
        delete_contact()

    elif opt == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.\n")
