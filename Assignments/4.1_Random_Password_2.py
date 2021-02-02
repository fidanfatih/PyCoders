
import tkinter as tk
from random import choice,shuffle

def generate():
    entry.delete(0, 'end')

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits='0123456789'
    specials="!@#$%^&*()"
    all_char=upper+lower+digits+specials 
    
    password = ""
    for i in range(0,2):
        password=password+ choice(specials)
    for i in range(0,2):
        password = password + choice(upper)
    for i in range(0,2):
        password = password + choice(digits)
    for i in range(0,4):
        password = password + choice(all_char)
          
    password=list(password)
    shuffle(password)
    return "".join(password)

def button():
    entry.insert(10,generate())


generator=tk.Tk()

generator.title("Password Generator 1.0v")
generator.geometry("400x200")

intro_text=tk.Label(generator,text=" Click the button to generate a password ",fg="maroon",font=("Microsoft Sans Serif","11","bold"))
intro_text.pack(pady=20)

password_text = tk.Label(generator, text=" Password ",fg="maroon",font=("Microsoft Sans Serif","14","bold"))
password_text.pack(pady=1)

entry = tk.Entry(generator,text= generate)
entry.pack(pady=10)

button =tk.Button(generator, text = " GENERATE ",width=15,height =2,fg="maroon",command=button,font=("Microsoft Sans Serif","10","bold"))
button.pack(pady=5)

generator.mainloop()