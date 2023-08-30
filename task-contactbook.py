contacts = []

while True:
    print("Choose an action: 1 - Add contact, 2 - View contacts, 3 - Search contacts, 4 - Quit")
    choice = input("User chooses: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts.append({"name": name, "phone": phone})
        print("Contact added successfully.\n")
    elif choice == '2':
        print("Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
        print()
    elif choice == '3':
        search_term = input("Enter search term: ").lower()
        search_results = [contact for contact in contacts if search_term in contact['name'].lower()]
        
        print("Search results:")
        for idx, contact in enumerate(search_results, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
        print()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid action.\n")
