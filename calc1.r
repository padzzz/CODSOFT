import tkinter as tk

window = tk.Tk()
window.title('Calculator')

entry = tk.Entry(window, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=5, pady=5)


def myclick(number):
    entry.insert(tk.END, number)


def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tk.messagebox.showinfo("Error", f"Invalid Expression: {e}")


def clear():
    entry.delete(0, tk.END)


buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('4', 2, 0),
    ('5', 2, 1), ('6', 2, 2), ('7', 3, 0), ('8', 3, 1),
    ('9', 3, 2), ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
    ('*', 5, 2), ('/', 6, 0), ('=', 6, 1), ('C', 6, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, padx=15, pady=5, width=3 if text != 'C' else 12,
                       command=lambda t=text: myclick(t) if t != '=' else equal() if t != 'C' else clear())
    button.grid(row=row, column=col, pady=2)

window.mainloop()
