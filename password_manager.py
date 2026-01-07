import json
import getpass

class PasswordManager:
    def __init__(self,filename="password.json"):
        self.filename = filename
        self.passwords = self.load_data()

    def load_data(self):
        try:
            with open(self.filename,"r")as f :
                return json.load(f)
        except FileNotFoundError:
            return{}
        

    def save_data(self):
        with open(self.filename,"w") as f :
            json.dump(self.passwords, f,indent=4)


    def add_password(self):
        site = input("Enter website name:").lower()

        if site in self.passwords:
            print("Password already exists")
            return
        
        username = input("Enter username: ")
        password = getpass.getpass("Enter password (hidden): ")

        self.passwords[site] = {
            "username": username,
            "password": password
        }

        self.save_data()
        print("Password saved successfully.")

    def view_all(self):
        if not self.passwords:
            print("No passwords saved.")
            return

        print("\n--- Saved Websites ---")
        for site in self.passwords:
            print("-", site)

    def search_password(self):
        site = input("Enter website to search: ").lower()

        if site in self.passwords:
            data = self.passwords[site]
            print(f"Website: {site}")
            print(f"Username: {data['username']}")
            print(f"Password: {'*' * len(data['password'])}")
        else:
            print("No password found for this website.")

    def delete_password(self):
        site = input("Enter website to delete: ").lower()

        if site in self.passwords:
            del self.passwords[site]
            self.save_data()
            print("Password deleted.")
        else:
            print("Website not found.")

def main():
    manager = PasswordManager()

    while True:
        print("\n====== PASSWORD MANAGER ======")
        print("1. Add password")
        print("2. View all websites")
        print("3. Search password")
        print("4. Delete password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                manager.add_password()
            case "2":
                manager.view_all()
            case "3":
                manager.search_password()
            case "4":
                manager.delete_password()
            case "5":
                print("Exiting... Stay safe 🔐")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()