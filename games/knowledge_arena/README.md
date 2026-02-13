📊 Player Performance Tracker

A simple command-line based player performance tracking system built using Python.
This project allows users to create profiles, record test results, track scores, and calculate accuracy. Player data is stored persistently using file handling.

--------------------------------
🚀 Features:

👤 Create a new player profile
📂 Load existing player data
🧮 Track score, correct answers, and total attempts
📈 Automatically calculate accuracy percentage
💾 Persistent storage using a text file
🖥️ Interactive command-line menu

--------------------------------
🗂️ Project Structure:

project/
│
├── main.py          # Program entry point and menu system
├── player.py       # Player class and file handling logic
└── players.txt      # Data storage file (auto-created)

--------------------------------
⚙️ How It Works:

The program loads existing player data from players.txt.
The user enters their name.
If the profile exists, it loads the saved data.
If not, a new profile is created.

--------------------------------
The user can:

📊 View statistics
➕ Add test results
💾 Save and exit

All data is saved in a structured format:
name,score,correct,attempts

--------------------------------
🛠️ Technologies Used:

🐍 Python 3
🧱 Object-Oriented Programming (OOP)
📁 File Handling
🗃️ Dictionaries for data storage
🧠 Key Concepts Implemented

--------------------------------
Class design (Player)
Instance methods
Default constructor arguments
Data persistence
Input validation
Loop-based menu system

--------------------------------
🖥️ Example Usage:

Enter your name: Dhruv
Welcome back! Dhruv
1. Show Stats
2. Add Test Result
3. Exit
