# Secure Password Manager (Python OOP)

A console-based **Password Manager** application that allows users to securely store, retrieve, and manage their login credentials for different websites. This project utilizes Python's **Object-Oriented Programming (OOP)** principles and **JSON** for persistent data storage.

## 🔐 Key Features

- **Secure Input:** Uses the `getpass` library to hide passwords while typing in the terminal.
- **Data Persistence:** Stores your credentials in a `password.json` file, so they remain saved even after closing the program.
- **CRUD Operations:**
  - **Create:** Add new website credentials.
  - **Read:** View a list of all stored websites and search for specific usernames.
  - **Delete:** Remove credentials you no longer need.
- **Privacy by Design:** In the search feature, passwords are masked (e.g., `*******`) to prevent shoulder-surfing.
- **Case-Insensitive Search:** Automatically converts website names to lowercase for easier searching.

## 🛠️ Built With

- **Python 3.10+**
- **JSON Module:** For local database management.
- **getpass Module:** For secure password entry.

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/password-manager-python.git](https://github.com/your-username/password-manager-python.git)
