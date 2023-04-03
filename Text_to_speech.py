import tkinter as tk
import pyttsx3

engine = pyttsx3.init()


def speak(text, voice, speed):
    engine.setProperty('rate', speed)
    voices = engine.getProperty('voices')
    if voice == 'Male':
        if len(voices) > 0:
            engine.setProperty('voice', voices[0].id)
    elif voice == 'Female':
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
    elif voice == 'Child':
        if len(voices) > 3:
            engine.setProperty('voice', voices[3].id)
    engine.say(text)
    engine.runAndWait()


def speak_button_click():
    text = text_input.get('1.0', tk.END)
    voice = voice_selection.get()
    speed = speed_selection.get()
    speak(text, voice, speed)


def quit_button_click():
    root.destroy()


root = tk.Tk()
root.title("Text to Speech")

root.configure(bg='yellow')

text_input = tk.Text(root, height=10, width=50)
text_input.pack(side=tk.TOP, padx=10, pady=10)

voice_selection = tk.StringVar(value='Male')
male_button = tk.Radiobutton(root, text='Male', variable=voice_selection, value='Male')
female_button = tk.Radiobutton(root, text='Female', variable=voice_selection, value='Female')
child_button = tk.Radiobutton(root, text='Child', variable=voice_selection, value='Child')
male_button.pack(side=tk.LEFT, padx=5, pady=5)
female_button.pack(side=tk.LEFT, padx=5, pady=5)
child_button.pack(side=tk.LEFT, padx=5, pady=5)

speed_selection = tk.IntVar(value=150)
speed_scale = tk.Scale(root, from_=50, to=300, variable=speed_selection, orient=tk.HORIZONTAL, label='Speed')
speed_scale.pack(side=tk.TOP, padx=10, pady=10)

speak_button = tk.Button(root, text='Speak', command=speak_button_click)
quit_button = tk.Button(root, text='Quit', command=quit_button_click)
speak_button.pack(side=tk.RIGHT, padx=5, pady=5)
quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()
