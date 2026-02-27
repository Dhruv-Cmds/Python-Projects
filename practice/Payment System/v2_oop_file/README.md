# 💳 Payment System (Polymorphism in Python)

**Author:** Dhruv  

A Python project that demonstrates **polymorphism** in Object-Oriented Programming by implementing multiple payment methods using a shared interface.

---

## 📖 Description

The Payment System models real-world payment methods using a common `Payment` base class.  
Different payment types such as **Cash**, **Card**, and **UPI** override the same `pay()` method but behave differently at runtime.

This project clearly demonstrates how **polymorphism** allows the same method call to produce different results depending on the object type.

---

## 🧠 OOP Concepts Used

- Polymorphism  
- Method Overriding  
- Base and Derived Classes  
- Runtime Method Dispatch  
- File Handling  

---

## ✨ Features

- Unified payment interface  
- Multiple payment methods (Cash, Card, UPI)  
- Demonstrates runtime polymorphism  
- Clean and extendable design  
- Easy to add new payment types  
- Persistent payment storage using file handling  

---

## 🛠 Tech Stack

- **Language:** Python 3  
- **Programming Paradigm:** Object-Oriented Programming (OOP)  

---

## 🚀 How to Run

1. Clone or download the repository  
2. Make sure Python 3 is installed  
3. Run the program:

```bash
python payment_system.py

📂 Output

Displays payment messages in the terminal

Saves each payment amount to pay.txt without overwriting previous data

📌 Example

500, Amount paid using cash.
600, Amount paid using card.
700, Amount paid using upi.

Contents of pay.txt:

500
600
700