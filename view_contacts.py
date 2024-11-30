def view_contacts(contacts):
    """
    Display all contacts in a user-friendly format.
    """
    if not contacts:
        print("No contacts found.")
        return
    
    print("\n=== Contact List ===")
    print(f"{'Name':<15} {'Email':<25} {'Phone':<15} {'Address':<30}")
    print("-" * 85)
    
    for contact in contacts:
        print(f"{contact['name']:<15} {contact['email']:<25} {contact['phone']:<15} {contact['address']:<30}")
