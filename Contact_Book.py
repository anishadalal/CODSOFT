contacts = []

def add_contact():
    print("\nAdd New Contact")
    name = input("enter name: ")
    phone = input("Enter contact number: ")
    contacts.append({"name": name, "phone": phone})
    print("Contact added!")

def view_contacts():
    print("\nContact List: ")
    if not contacts:
        print("No contact found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\nSearch Contact: ")
    query = input("Enter name to search: ").lower()
    results = [c for c in contacts if query in c ['name'].lower() or query in c['phone']]
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contact found.")
    
def update_contact():
    print("\nUpdate Contact: ")
    query = input("Enter name or contact number to update: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new contact number: ") or contact['phone']
            print("Contact updated!")
            return
    print("Contact not found!")

def delete_contact():
    print("\nDelete Contact: ")
    query = input("Enter name or contact number to delete: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contacts.remove(contact)
            print("Contact Deleted!")
            return
    print("Contact not found.")

def main():
    while True:
        print("Conatct Book: ")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Quitting the program!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()