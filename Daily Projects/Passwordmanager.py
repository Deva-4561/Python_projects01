passwords = {}  # Dictionary to store passwords

while True:
    print("\n--- Simple Password Manager ---")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        account = input("Enter account name: ")
        pwd = input("Enter password: ")
        passwords[account] = pwd
        print(f"Password saved for {account}.")

    elif choice == '2':
        if not passwords:
            print("No passwords saved.")
        else:
            print("\nSaved Passwords:")
            for account, pwd in passwords.items():
                print(f"{account}: {pwd}")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")