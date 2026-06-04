import os

print("PyReader 1.20 | Code by Gitansh")

while True:
    
    text = input("Enter Your text:- ")

    if 'exit' in text:
        break

    os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')
