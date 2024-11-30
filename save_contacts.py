def save_contacts(contacts):
    """
    Save all contacts to a CSV file.
    """
    with open("contacts.csv", "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['email']},{contact['phone']},{contact['address']}\n")