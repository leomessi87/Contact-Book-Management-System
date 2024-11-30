import save_contacts

def remove_contact(contacts):
    """
    Remove a contact by phone number.
    """
    phone = input("Enter the phone number of the contact to remove: ").strip()
    
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts.save_contacts(contacts)
            print("Contact removed successfully!")
            return contacts

    print("Error: No contact found with the provided phone number.")
    return contacts
