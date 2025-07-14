from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import pyttsx3
import speech_recognition as sr

def check_pronunciation(target_word):
    attempts = 2
    for i in range(attempts):
        speak(f"Please pronounce the word {target_word}")
        spoken_text = listen()
        if spoken_text.lower() == target_word.lower():
            speak("You got a correct pronunciation!")
            result_label.config(text="Correct pronunciation!", fg="limegreen")
            return "Correct pronunciation!"
        else:
            speak("You got an incorrect pronunciation!")
            result_label.config(text="Incorrect pronunciation. Try again.", fg="red")
            return "Incorrect pronunciation."
    result_label.config(text="The attempt is over!", fg="orange")
    return "The attempt is over!"

def on_submit():
    target_word = entry.get()
    if not target_word.strip():
        result_label.config(text="Please enter a word.", fg="red")
        return
    result = check_pronunciation(target_word)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            return ""

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()

def system_window():
    window = tk.Toplevel(root)
    window.title("Automatic Pronunciation Mistake Detector")
    window.geometry("700x500")

root = tk.Tk()
root.title("Automatic Pronunciation Mistake Detector")
root.geometry("800x600")
root.config(bg="#f0f8ff")

title_label = tk.Label(root, text="Pronunciation Mistake Detector", font=("Helvetica", 28, "bold"), bg="#f0f8ff", fg="#4682b4")
title_label.pack(pady=30)

frame = Frame(root, bg="#add8e6", padx=30, pady=30, bd=2, relief=RIDGE)
frame.pack(pady=30)

entry_label = Label(frame, text="Enter word:", font=("Helvetica", 18), bg="#add8e6", fg="#00008b")
entry_label.grid(row=0, column=0, pady=10)

entry = Entry(frame, width=30, font=("Helvetica", 18), borderwidth=2, relief="groove", bg="#e0ffff", fg="#00008b")
entry.grid(row=0, column=1, pady=10, padx=10)

system_button = Button(frame, text='Check Pronunciation', bg='#00bfff', fg="white", font=("Helvetica", 18), command=on_submit)
system_button.grid(row=1, columnspan=2, pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#f0f8ff", fg="#ff4500")
result_label.pack(pady=20)

root.mainloop()
