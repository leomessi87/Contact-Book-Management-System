import add_contact
import view_contacts
import remove_contact
import search_contact

# Load existing contacts from file
contacts = add_contact.load_contacts()

while True:
    print("\n=== Contact Book Management System ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("0. Exit")
    
    choice = input("Select an option: ").strip()

    if choice == "1":
        contacts = add_contact.add_contact(contacts)
    elif choice == "2":
        view_contacts.view_contacts(contacts)
    elif choice == "3":
        contacts = remove_contact.remove_contact(contacts)
    elif choice == "4":
        search_contact.search_contact(contacts)
    elif choice == "0":
        print("Exiting the Contact Book Management System. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid number.")
