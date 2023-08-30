Task-5: Contact Book

Question: Implement a simple contact book that allows users to add, view, and search for contacts (name and phone number).

Code:
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

Logic:
1. The variable contacts is a list that will store the contact information- name and phone number.
2. The program enters an infinite loop where the user can repeatedly choose actions.
3. The user chooses an action by entering a number(1 or 2 or 3).
4. If the user chooses 1, the program asks for the name and phone number of the contact.
5. The contact is then added to the contacts list.
6. If the user chooses 2, the program loops through the contacts list and displays all names and phone numbers.
7. If the user chooses 3, the program asks for a search term.
8. It then searches through the contacts list and displays results.
9. If the user chooses 4, the program ends.
10. If user enters a different number or an invalid entry, program loops back to the menu.
