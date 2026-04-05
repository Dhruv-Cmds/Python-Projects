# Bank Management System (OOP + File I/O) 🏦

A console-based Bank Management System built using Python.  
This project uses **Object-Oriented Programming** and **file handling** to manage bank accounts with persistent storage.

## Features
- Create a new bank account
- Deposit money
- Withdraw money
- Check account balance
- Data persistence using a (`.txt`/`.json `/`Mysql(Database)`)
- Menu-driven command-line interface

## Concepts Used
- Object-Oriented Programming (Classes & Methods)
- File Handling (read/write)
- Exception Handling
- Lists and basic control flow
- Input validation

## Project Structure
v2_oop_file/
├── MYSql queries/
├── Main.py
├── bank.json
└── bank.txt

## How to Run
Make sure Python is installed on your system. And MySql for Database

```bash

- python Main.py

### ⚠️ Warning

The database can store multiple users with the same name. However, this project uses the **name** field to identify users.

Because of this, if duplicate names are added, operations like **update, delete, or withdraw** may affect multiple accounts at once.

To avoid this issue, do not create multiple accounts with the same name.

> Note: This can be prevented by using a unique **ID**, but for learning purposes, the project intentionally uses names without changing the original structure.


Notes:-

 bank.txt is used to store account data permanently.
 Account data persists even after the program is closed.
 Do not delete bank.txt while the program is running.
 
Example Operations:-

 Create account with a starting balance
 Deposit and withdraw money securely
 Prevents invalid inputs and insufficient balance withdrawals