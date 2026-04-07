## 📌 Student Management System

### 📖 Overview

A modular **Student Management System** built using Python and Object-Oriented Programming principles.
The application supports storing student records, managing marks, and evaluating academic performance.
Data persistence is handled via file storage (TXT/JSON) and extended to database integration (MySQL).

---

### 🧠 Core Concepts

* Object-Oriented Programming (Classes & Objects)
* Data Structures (Lists)
* File Handling (TXT / JSON)
* Database Integration (MySQL)
* CRUD Operations
* Basic Data Processing & Aggregation

---

### 🚀 Features

* Add and manage student records
* Store and retrieve marks
* Calculate average scores dynamically
* Pass/Fail evaluation based on performance
* Persistent storage using:

  * Text files (`.txt`)
  * JSON files (`.json`)
  * MySQL database (latest version)
* Modular and scalable code structure

---

### 🛠 Tech Stack

* **Language:** Python 3
* **Concepts:** OOP, File Handling
* **Database:** MySQL
* **Libraries:** `mysql-connector-python`

---

### 📂 Project Structure

```
v2_oop_file/
│── MySql queries/
│    │── main.sql     # SQL schema
│── Main.py        # Entry point
│── db.py          # Database connection
│── student.json   # JSON storage (optional)
│── student.txt    # txt storage (optional)
│── requirements.txt
```

---

### ▶️ How to Run

1. Navigate to the project directory:

```bash
cd "Student Management System/v2_oop_file"
```

2. Run the application:

```bash
python Main.py
```

---

### ⚙️ Setup Requirements

* Install dependencies:

```bash
pip install -r requirements.txt
```

* Setup MySQL database:

```bash
mysql -u root -p < main.sql
```


### 👨‍💻 Author

Dhruv

---
