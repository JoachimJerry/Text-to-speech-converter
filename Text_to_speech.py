import tkinter as tk
from tkinter import ttk
import pyttsx3

class TextToSpeechGUI:
    def __init__(self, master):
        self.master = master
        master.title("Text to Speech")
        master.geometry("500x300")
        master.configure(bg='yellow')
        
        self.label = ttk.Label(master, text="Enter text to convert to speech:")
        self.label.pack(pady=10)
        self.textbox = tk.Text(master, height=5, width=50)
        self.textbox.pack(pady=5)
        
        self.voice_label = ttk.Label(master, text="Select voice:")
        self.voice_label.pack(pady=10)
        self.voice_var = tk.StringVar(value="male")
        self.voice_male = ttk.Radiobutton(master, text="Male", variable=self.voice_var, value="male")
        self.voice_male.pack(anchor="w")
        self.voice_female = ttk.Radiobutton(master, text="Female", variable=self.voice_var, value="female")
        self.voice_female.pack(anchor="w")
        self.voice_child = ttk.Radiobutton(master, text="Child", variable=self.voice_var, value="child")
        self.voice_child.pack(anchor="w")
        
        self.speed_label = ttk.Label(master, text="Select speed:")
        self.speed_label.pack(pady=10)
        self.speed_var = tk.DoubleVar(value=1.0)
        self.speed_slow = ttk.Radiobutton(master, text="Slow", variable=self.speed_var, value=0.5)
        self.speed_slow.pack(anchor="w")
        self.speed_normal = ttk.Radiobutton(master, text="Normal", variable=self.speed_var, value=1.0)
        self.speed_normal.pack(anchor="w")
        self.speed_fast = ttk.Radiobutton(master, text="Fast", variable=self.speed_var, value=1.5)
        self.speed_fast.pack(anchor="w")
        
        self.speak_button = ttk.Button(master, text="Speak", command=self.speak_text)
        self.speak_button.pack(side="right", padx=10, pady=10, fill="x")
        self.quit_button = ttk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(side="right", padx=10, pady=10, fill="x")
        
        self.engine = pyttsx3.init()
        
    def speak_text(self):
        text = self.textbox.get("1.0", tk.END)
        voice = self.voice_var.get()
        speed = self.speed_var.get()
        
        if voice == "male":
            self.engine.setProperty('voice', 'english+m3')
        elif voice == "female":
            self.engine.setProperty('voice', 'english+f4')
        elif voice == "child":
            self.engine.setProperty('voice', 'english+f3')
        
        self.engine.setProperty('rate', int(speed * 180))
        
        self.engine.say(text)
        self.engine.run
