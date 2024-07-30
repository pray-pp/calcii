import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("290x420")
root.configure(background="#2D2D2D")  # Dark background for the window

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="lucida 20", borderwidth=5, relief="solid", justify="right", 
                 bg="#1C1C1C", fg="white")  # Darker background and white text for entry
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

frame = tk.Frame(root, bg="#2D2D2D")  # Match the frame's background with the window
frame.pack(expand=True, pady=10)

for i, text in enumerate(button_texts):
    button = tk.Button(frame, text=text, font="lucida 15 bold", background="#4B4B4B", foreground="white",
                       borderwidth=4, highlightbackground="#F0A500", highlightthickness=0, width=4, height=2)
    button.grid(row=i//4, column=i%4, padx=5, pady=5)
    button.bind("<Button-1>", click)

root.mainloop()
