# 🔐 Secure Account System

### 📖 Overview

A modular **Secure Account System** built using Python and Object-Oriented Programming (OOP) principles.  
The application simulates real-world banking operations such as account creation, deposits, withdrawals, and balance checks with secure **PIN-based authentication**.

Data persistence is handled via:
- File storage (TXT / JSON)
- Database integration (MySQL)

---

### 🧠 Core Concepts

* Object-Oriented Programming (Classes & Objects)
* Encapsulation
* Methods & Code Reusability
* File Handling (TXT / JSON)
* Database Integration (MySQL)
* CRUD Operations
* Input Validation & Error Handling

---

### 🚀 Features

* Create account with secure PIN  
* Deposit money with validation  
* Withdraw money with balance verification  
* Check account balance securely  
* Display account information  
* Persistent storage using:

  * Text files (`account.txt`)
  * JSON files (`account.json`)
  * MySQL database  

---

### 🛠 Tech Stack

* **Language:** Python 3  
* **Concepts:** OOP, File Handling  
* **Database:** MySQL  
* **Libraries:** `mysql-connector-python`, `python-dotenv`  

---

### 📂 Project Structure

Secure-Account-System/
│── Main.py # Entry point
│── db.py # Database connection
│── account.txt # TXT storage (optional)
│── account.json # JSON storage (optional)
│── requirements.txt


---

### ▶️ How to Run

1. Navigate to the project directory:

```bash
cd "Secure Account/v2_oop_file"

2. Install dependencies:

pip install mysql-connector-python python-dotenv

3. Create a .env file:
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=your_password
    DB_NAME=your_database

4. Run the application:
    python Main.py


⚙️ Setup Requirements
Make sure MySQL is installed and running
Create your database manually or via SQL script
Update .env with correct credentials

🔐 Security Features
PIN-based authentication
Input validation for all operations
Protection against invalid transactions
Controlled database access