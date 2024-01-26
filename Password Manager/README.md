# Password Manager

<!--Remove the below lines and add yours -->

This Python script serves as a simple password manager that allows users to store, retrieve, update, and delete passwords securely.

### Features

Encryption: Passwords are encrypted using Fernet symmetric key cryptography.
Data Storage: Passwords and associated information are stored in a JSON file (database.json).
PIN Protection: Access to the password manager is protected by a PIN.
Options: Users can show passwords, add new entries, update existing entries, and delete entries.

### Prerequisites
* Fernet
* json
* PrettyTable
* random
* string

### How to run the script

<!--Remove the below lines and add yours -->

```
$ python main1.0.py
```
Enter PIN: Upon running the script, you will be prompted to enter a PIN for authentication.
Menu Options:
Show Password: View all stored passwords along with associated information.
Add: Add a new entry to the password manager.
Update: Update an existing entry.
Delete: Delete an existing entry.
Quit: Exit the password manager.

### Screenshot/GIF showing the sample use of the script

<!--Remove the below lines and add yours -->

![input_image](Output.png)
### Important Files

config.json: Configuration file containing PIN and encryption key.
database.json: JSON file storing encrypted password entries.

## Working

Passwords are encrypted using Fernet symmetric key encryption provided by the cryptography library.
The script interacts with JSON files (config.json and database.json) for configuration and data storage.
Data manipulation functions handle adding, updating, deleting, and displaying password entries.
The script encrypts passwords before storing them and decrypts them when displaying.

## _Author Name_

<!--Remove the below lines and add yours -->
This script was created by [milliyin](https://github.com/milliyin)
Feel free to contribute to this project by submitting issues or pull requests.
