import tkinter as tk

def display_fullname():
    entered_name = entry_input.get()
    entry_output.delete(0, tk.END)
    entry_output.insert(0, entered_name)

root = tk.Tk()
root.title("Midterm in OOP")
root.geometry("350x250")

label_prompt = tk.Label(root, text="Enter your fullname:", fg="red", font=("Arial", 10))
label_prompt.pack(pady=(20, 5))

entry_input = tk.Entry(root, width=25, font=("Arial", 10))
entry_input.pack(pady=5)

button_display = tk.Button(root, text="Click to display your Fullname", fg="red", font=("Arial", 10), command=display_fullname)
button_display.pack(pady=10)

entry_output = tk.Entry(root, width=25, font=("Arial", 10))
entry_output.pack(pady=5)

root.mainloop()