# 🧮 PyCalc — A Simple GUI Calculator using PySide6

PyCalc is a beginner-friendly calculator app built with **Python** and **PySide6 (Qt for Python)**.  
It provides a clean, functional GUI that supports basic arithmetic operations such as addition, subtraction, multiplication, division, and modulo.  

This project demonstrates how to structure a PySide6 application using multiple widget layers and layouts.

---

## 🚀 Features

- 🪶 Simple and clean PySide6 interface  
- ➕ Supports addition, subtraction, multiplication, division, and modulo  
- 🧹 Includes `C` (clear all) and `CE` (backspace) buttons  
- 🔢 Button-based input with a single `QLineEdit` display  
- 🧠 Expression evaluation powered by `simpleeval`  

---

## 🧩 Tech Stack

- **Language:** Python 3  
- **GUI Framework:** PySide6  
- **Expression Evaluator:** simpleeval  

---

## 🗂️ Project Structure

```

📁 PyCalc/
├── main.py
├── mainwindow.py
└── README.md

````

- `main.py` — Entry point of the application  
- `mainwindow.py` — Contains all widget classes (MainWindow, MainWidget, Layers, and Logic)  

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Adrian7373/PyCalc.git
cd PyCalc
````

### 2️⃣ Install dependencies

```bash
pip install PySide6 simpleeval
```

### 3️⃣ Run the app

```bash
python main.py
```

---

## 🧱 Code Structure Overview

The calculator is organized into layered widgets:

* **MainWindow** – Root QMainWindow
* **MainWidget** – Container widget
* **HorizontalLayoutsHolder** – Holds the display and all button rows
* **LayerZero–LayerFour** – Horizontal button rows for operations and digits

Each button connects to its own slot function that updates the shared `QLineEdit` display.

---

## 🎯 What I Learned

* How to create and manage multiple **layouts** in PySide6
* How to handle **signals and slots** for button events
* How to structure a multi-class GUI application
* How to safely evaluate user input using `simpleeval`

---

## 🧑‍💻 Author

**Adrian Ablaza**
📚 BSIT Student at Nueva Ecija University of Science and Technology
💻 Passionate about Python, GUI Development, and Software Design

---

## 🏁 Future Improvements

* Add keyboard input support
* Add dark/light theme toggle
* Add history and memory functions
* Add scientific operations (sin, cos, log, etc.)

---

## 📸 Screenshot 

<img width="389" height="531" alt="Screenshot 2025-10-17 191409" src="https://github.com/user-attachments/assets/976dbd62-1431-457b-ac12-97e1161f0b2d" />


