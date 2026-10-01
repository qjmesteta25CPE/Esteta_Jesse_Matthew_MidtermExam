import tkinter as tk

def change_color():
    color_button.config(bg="yellow", activebackground="yellow")

root = tk.Tk()
root.title("Special Midterm Exam in OOP")
root.geometry("400x400")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

color_button = tk.Button(
    root, 
    text="Click to Change Color", 
    command=change_color,
    font=("Arial", 11),
    padx=10,
    pady=5
)

color_button.grid(row=0, column=0)

root.mainloop()