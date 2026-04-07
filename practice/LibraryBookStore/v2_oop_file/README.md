# 📚 Library Management System (Python)

A clean and minimal **Command-Line Library Management System** built using Python.
This project demonstrates core programming concepts such as **Object-Oriented Programming (OOP)** and **file handling**, while providing a practical system to manage books.

---

## 🚀 Features

* 📖 Add new books to the library
* 📋 View all books with real-time status *(Available / Issued)*
* 📤 Issue a book by title
* 📥 Return a book by title
* 💾 Persistent storage using:

  * `library.txt` *(text format)*
  * `library.json` *(JSON format)*
  * 🗄️ Database integration (MySQL)
* 🧭 Simple and interactive menu-driven CLI

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Concepts Used:**

  * Object-Oriented Programming (OOP)
  * File Handling (Text & JSON)

---

## 📂 Project Structure

```

v2_oop_file/
│   ├── MySql queries/
├── Main.py          # Main application logic
├── db.py
├── library.txt      # Text-based storage (optional)
└── library.json     # JSON-based storage (optional)

```

---

## ⚙️ How It Works

1. Run the program:

   ```bash
   python Main.py
   ```

2. Choose from the menu:

   ```
   ===== Library Menu =====
   1. Add Book
   2. Show Books
   3. Issue Book
   4. Return Book
   5. Exit
   ```

3. Perform operations interactively via terminal input.

---

## 💡 Example Book Entry

```

Title: Atomic Habits
Author: James Clear
Status: Available

```

## 🤝 Contribution

Feel free to fork this repository and improve it.
Pull requests are always welcome!

---

## 📜 License

This project is open-source and available under the **MIT License**.

---
