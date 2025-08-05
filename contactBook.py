contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added!")

def display_contacts():
    for name, number in contacts.items():
        print(f"{name}: {number}")

add_contact("Shubham", "9876543210")
add_contact("Amit", "9123456789")
print("\nContact Book:")
display_contacts()
