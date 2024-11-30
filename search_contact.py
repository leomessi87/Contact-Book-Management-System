def search_contact(contacts):
    """
    Search for a contact by name, email, or phone number.
    """
    search_term = input("Enter name, email, or phone number to search: ").strip().lower()
    
    results = [
        contact for contact in contacts
        if search_term in contact["name"].lower() or
           search_term in contact["email"].lower() or
           search_term in contact["phone"]
    ]
    
    if results:
        print("\n=== Search Results ===")
        print(f"{'Name':<15} {'Email':<25} {'Phone':<15} {'Address':<30}")
        print("-" * 85)
        for contact in results:
            print(f"{contact['name']:<15} {contact['email']:<25} {contact['phone']:<15} {contact['address']:<30}")
    else:
        print("No contacts found matching the search term.")
