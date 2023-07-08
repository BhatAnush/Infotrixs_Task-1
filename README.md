# Contact Management System
**This project is made during the week-1 of the Infotrixs python development internship.** 

This is a simple contact management system implemented in Python. It allows users to perform operations such as adding, searching, updating, and deleting contacts. Here's a step-by-step explanation of how the code works:

1. The code starts by importing the required modules: `json` and `pandas`. `json` module is used to handle JSON data, and `pandas` is used to work with data in tabular form.

2. The `contacts` list is initialized as an empty list. This list will store the contacts entered by the user.

3. `CONTACTS_FILE` is set to "contacts.json". This constant specifies the name of the JSON file where the contacts will be saved.

4. The `save_contacts()` function is defined. This function is responsible for saving the contacts to the JSON file. It opens the file in write mode using the `open()` function, and then uses `json.dump()` to write the contacts list to the file in JSON format. Finally, it prints a message indicating that the contacts have been saved successfully.

5. The `load_contacts()` function is defined. This function is responsible for loading the contacts from the JSON file. It uses a `try-except` block to handle the case where the file does not exist. It opens the file in read mode using the `open()` function, and then uses `json.load()` to load the JSON data from the file into the `contacts` list. If the file is not found, the `except FileNotFoundError` block is executed, and it simply does nothing. After loading the contacts, it prints a message indicating that the contacts have been loaded successfully.

6. The `add_contact()` function is defined. This function allows the user to add a new contact. It prompts the user to enter the contact's name, phone number, and email address using the `input()` function. It then checks if a contact with the same name, phone, and email already exists in the `contacts` list by iterating over the list and comparing the values. If a duplicate contact is found, it prints a message indicating that the contact already exists and returns. If the contact is not a duplicate, it creates a dictionary `contact` with the entered details, appends it to the `contacts` list, and prints a message indicating that the contact has been added successfully.

7. The `search_contact()` function is defined. This function allows the user to search for a contact by name. It prompts the user to enter the name to search using the `input()` function. It then iterates over the `contacts` list and checks if the name matches any of the contacts' names (case-insensitive). If a match is found, the contact is added to the `found_contacts` list. After searching all the contacts, it checks if any contacts were found. If contacts are found, it prints the details of each found contact (name, phone, and email) using a loop. If no contacts are found, it prints a message indicating that no contacts were found.

8. The `update_contact()` function is defined. This function allows the user to update a contact's phone number and email address. It prompts the user to enter the name of the contact to update using the `input()` function. It then iterates over the `contacts` list and checks if the name matches any of the contacts' names (case-insensitive). If a match is found, it prompts the user to enter the new phone number and email address using the `input()` function. It then updates the contact's details in the `contacts` list and prints a message indicating that the contact has been updated successfully. If no matching contact is found, it prints a message indicating that the contact was not found.

9. The `delete_contact()` function is defined. This function allows the user to delete one or more contacts. It prompts the user to enter the name of the contact to delete using the `input()` function. It then iterates over the `contacts` list and checks if the name matches any of the contacts' names (case-insensitive). If a match is found, the contact is added to the `found_contacts` list. After searching all the contacts, it checks if any contacts were found. If contacts are found, it prints the details of each found contact (name, phone, and email) using a loop. It then prompts the user for confirmation to delete the contacts. If the user confirms by entering "yes" (case-insensitive), it removes the contacts from the `contacts` list using a list comprehension and prints a message indicating that the contacts have been deleted successfully. If the user cancels or no contacts were found, it prints an appropriate message.

10. The `print_menu()` function is defined. This function prints the menu options for the contact management system. It simply displays the menu options using the `print()` function.

11. The `main()` function is defined. This function serves as the entry point of the program. It first calls the `load_contacts()` function to load any existing contacts from the JSON file. Then, it enters a loop that displays the menu options, prompts the user for a choice using the `input()` function, and executes the corresponding function based on the user's choice. If the user enters "5", it calls the `save_contacts()` function to save the contacts to the JSON file and exits the loop.

12. The `if __name__ == '__main__':` block checks if the script is being run directly (as opposed to being imported as a module). If it is the main script, it calls the `main()` function to start the contact management system.

13. After the `main()` function returns (i.e., the user chooses to exit the program), the code uses `pandas` to read the contacts from the JSON file into a DataFrame (`df`). It then prints the first few rows of the DataFrame using the `head()` method.

14. Finally, the code uses `pandas` to read the contacts from the JSON file into another DataFrame (`df`). It sets some options to display all columns and remove truncation of text content. It then prints the entire DataFrame, displaying all the contacts.
