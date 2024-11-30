import save_contacts

def load_contacts():
    """
    Load contacts from the file and return them as a list of dictionaries.
    """
    contacts = []
    try:
        with open("contacts.csv", "r") as file:
            for line_number, line in enumerate(file, start=1):
                # Skip empty lines
                if not line.strip():
                    continue
                try:
                    name, email, phone, address = line.strip().split(",")
                    contacts.append({
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "address": address
                    })
                except ValueError:
                    print(f"Warning: Skipping invalid line {line_number} in contacts.csv: {line.strip()}")
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty contact list
        pass
    return contacts

def add_contact(contacts):
    """
    Add a new contact to the system. Ensures no duplicate phone numbers.
    """
    try:
        name = input("Enter Name: ").strip()
        if not name.isalpha():
            raise ValueError("Name must only contain letters.")
        
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit():
            raise ValueError("Phone number must be numeric.")
        
        address = input("Enter Address: ").strip()

        # Check for duplicate phone numbers
        for contact in contacts:
            if contact["phone"] == phone:
                print("Error: A contact with this phone number already exists.")
                return contacts

        # Add contact to the list
        contacts.append({
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        })
        save_contacts.save_contacts(contacts)
        print("Contact added successfully!")

    except ValueError as e:
        print(f"Error: {e}")
    return contacts
