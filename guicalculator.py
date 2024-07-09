'''import tkinter as tk
from tkinter import ttk

def button_click(event):
    # Function to handle button clicks and update the display
    global expression
    button = event.widget
    text = button['text']
    
    if text == '=':
        try:
            result = eval(expression.get())
            expression.set(result)
        except:
            expression.set("Error")
    elif text == 'C':
        expression.set("")
    else:
        expression.set(expression.get() + text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to store the expression
expression = tk.StringVar()

# Create the entry widget for displaying the expression
entry = ttk.Entry(root, textvariable=expression, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create buttons and place them in the grid
row = 1
col = 0
for button_label in buttons:
    ttk.Button(root, text=button_label, width=10, command=lambda btn=button_label: expression.set(expression.get() + btn)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Bind click events to handle button clicks
for widget in root.winfo_children():
    widget.bind('<Button-1>', button_click)

root.mainloop()'''

from tkinter import *

root= Tk()
root.geometry("450x250")
root.title("My GUI")
root.mainloop()
