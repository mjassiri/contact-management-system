import json
import os
FILEPATH = "/content/drive/MyDrive/contacts.json"

from google.colab import drive
drive.mount('/content/drive')

def load_contacts(filename=FILEPATH):
    try:
        with open(filename, "r") as file:
            contacts = json.load(file)
            print(f"Successfully loaded contacts from {os.path.abspath(filename)}")
            return contacts
    except FileNotFoundError:
        print(f"No existing contacts file found - starting fresh")
        return {}
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return {}

def save_contacts(contacts, filename=FILEPATH):
    try:
        print(f"Attempting to save to: {filename}")
        with open(filename, "w") as file:
            json.dump(contacts, file, indent=4)
        
        # Verify file exists
        if os.path.exists(filename):
            print(f"File saved and verified at: {filename}")
            # Print the contents to make sure data was written
            with open(filename, 'r') as file:
                saved_data = json.load(file)
                print("Saved contacts:", saved_data)
        else:
            print("Warning: File was not created!")
            
    except Exception as e:
        print(f"Error saving contacts: {e}")
        print(f"Current working directory: {os.getcwd()}")

def add_contact(contacts):
  name = input("Enter contact name:")
  if name in contacts:
    print("Contact already exists.")
  else:
    phone = input("Enter phone number:")
    email = input("Enter email address:")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

def view_contacts(contacts):
  if not contacts:
    print("No contacts available.")
  else:
    for name, details in contacts.items():
      print(f"Name:: {name}, Phone: {details['phone']}, Email: {details['email']}")

def search_contact(contacts):
  name = input("Enter the contact name to search: ")
  if name in contacts:
    details = contacts[name]
    print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
  else:
    print("Contact not found.")

def update_contact(contacts):
  name = input("Enter the contact name to update: ")
  if name in contacts:
    phone = input("Enter new phone number:")
    email = input("Enter new email address:")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact updated successfully")
  else:
    print("Contact not found.")

def delete_contact(contacts):
  name = input("Enter the contact name to delete: ")
  if name in contacts:
    del contacts[name]
    print("Contact deleted successfully!")
  else:
    print("Contact not found.")

def main():
  contacts = load_contacts()
  while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save and Exit")

    choice = input("Choose an option: ")
    if choice == "1":
      add_contact(contacts)
    elif choice == "2":
      view_contacts(contacts)
    elif choice == "3":
      search_contact(contacts)
    elif choice == "4":
      update_contact(contacts)
    elif choice == "5":
      delete_contact(contacts)
    elif choice == "6":
      save_contacts(contacts)
      break
    else:
      print("Invalid choice. Please try again.")

main()
