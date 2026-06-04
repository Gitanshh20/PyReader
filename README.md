# 📖 PyReader 1.20

> A simple Text-to-Speech (TTS) application built with Python that reads your text aloud using Windows Speech Synthesizer.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Windows](https://img.shields.io/badge/Windows-Supported-blue?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ✨ Features

- 🔊 Convert text into speech
- ⚡ Fast and lightweight
- 🪟 Uses Windows built-in speech engine
- 🔄 Continuous input mode
- 🚪 Type `exit` to close the program

---

## 📂 Project Structure

```text
PyReader/
│
├── main.py
└── README.md
```

---

## 🛠 Requirements

- Python 3.x
- Windows OS
- PowerShell

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/YourUsername/PyReader.git
```

### Navigate to Project Directory

```bash
cd PyReader
```

### Run the Program

```bash
python main.py
```

---

## 💻 Example

```text
PyReader 1.20 | Code by Gitansh

Enter Your text:- Hello World
```

🔊 Output:

```text
Hello World
```

(The text will be spoken through your speakers.)

---

## 📜 Source Code

```python
import os

print("PyReader 1.20 | Code by Gitansh")

while True:
    
    text = input("Enter Your text:- ")

    if 'exit' in text:
        break

    os.system(
        f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
    )
```

---

## 🎯 Future Updates

- 🎨 GUI Interface
- 🎙️ Multiple Voice Support
- ⚙️ Speech Speed Control
- 💾 Save Audio as MP3/WAV
- 🌙 Dark Mode

---

## 👨‍💻 Author

### Gitansh

🐍 Python Developer  
🤖 Future AI Engineer

---

⭐ **If you like this project, give it a Star!**
