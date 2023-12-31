# -*- coding: utf-8 -*-
"""Infotrixs_Task-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qcRK1U-W6NUt9llobCCoUT17wDgJZwGR
"""

import json
import pandas as pd

contacts = []

CONTACTS_FILE = "contacts.json"

def save_contacts():
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)
    print("Contacts saved successfully!")

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts.extend(json.load(file))
        print("Contacts loaded successfully!")
    except FileNotFoundError:
        pass

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")

    # Check if a contact with the same name, phone, and email already exists
    for contact in contacts:
        if (contact['name'].lower() == name.lower() and
                contact['phone'] == phone and
                contact['email'].lower() == email.lower()):
            print("A contact with the same name, phone, and email already exists.")
            return

    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }

    contacts.append(contact)
    print("Contact added successfully!")

def search_contact():
    name = input("Enter the name to search: ")

    found_contacts = []
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            found_contacts.append(contact)

    if found_contacts:
        print("Found contact(s):")
        for contact in found_contacts:
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("--------------------")
    else:
        print("No contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")

            contact['phone'] = phone
            contact['email'] = email

            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    found_contacts = []
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            found_contacts.append(contact)

    if found_contacts:
        print("Found contact(s) to delete:")
        for contact in found_contacts:
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("--------------------")

        confirmation = input("Are you sure you want to delete these contacts? (yes/no): ")
        if confirmation.lower() == "yes":
            contacts[:] = [contact for contact in contacts if contact not in found_contacts]
            print("Contact(s) deleted successfully!")
        else:
            print("Deletion canceled.")
    else:
        print("No contacts found.")



def print_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def main():
    load_contacts()

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
             delete_contact()
        elif choice == '5':
            save_contacts()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

df = pd.read_json("contacts.json")

df.head()


df = pd.read_json("contacts.json")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
print(df)