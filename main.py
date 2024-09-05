import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_csv(input_file, output_file=None, columns_to_keep=None):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Keep only the specified columns
    if columns_to_keep:
        df = df[columns_to_keep]
    
    # Drop rows with null values in the kept columns
    df = df.dropna()

    # If output_file is not provided, create one based on the input file name
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_cleaned.csv"
    
    # Save the cleaned data to the output CSV file
    df.to_csv(output_file, index=False)
    
    messagebox.showinfo("Success", f"File cleaned and saved as: {output_file}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)

def browse_save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def on_clean():
    input_file = input_entry.get()
    output_file = output_entry.get() or None
    columns_to_keep = ['3U SNW2X', '650', 'F']  # Example columns
    if input_file:
        clean_csv(input_file, output_file, columns_to_keep)
    else:
        messagebox.showerror("Error", "Please select an input file.")

# Create the GUI
root = tk.Tk()
root.title("CSV Cleaner")

tk.Label(root, text="Input CSV file:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output CSV file (optional):").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_save_file).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Clean CSV", command=on_clean).grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
