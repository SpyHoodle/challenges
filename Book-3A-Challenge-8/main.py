import tkinter as tk
from tkinter import ttk
import json


class ConverterApp(tk.Tk):
    def __init__(self):
        # Inherit from tk.Tk
        super().__init__()

        # Set up the window
        self.frame = ttk.Frame(self)
        self.title("Unit Converter")
        self.resizable(False, False)
        self.frame.grid()

        # Parse units
        self.units = load_units("units.json")

    def draw(self):
        # Set grid orientation
        self.value_input.grid(column=0, row=1, padx=10, pady=10)
        self.value_output.grid(column=0, row=2, padx=10, pady=10)
        self.label_input.grid(column=0, row=0, padx=10, pady=10)
        self.unit_input.grid(column=1, row=1, padx=10, pady=10)
        self.unit_output.grid(column=1, row=2, padx=10, pady=10)
        self.button.grid(column=0, row=3, padx=10, pady=10)

    def click(self):
        print(self.value_input.get())


class Widgets:
    def __init__(self):
        # Input and output
        self.value_input = ttk.Entry(self, width=20)
        self.value_output = ttk.Entry(self, width=20, state="readonly")

        # Unit selection
        self.label_input = ttk.Label(self, text="")
        self.unit_input = ttk.Combobox(self, values=self.units, width=5)
        self.unit_output = ttk.Combobox(self, values=self.units, width=5)

        # Button to convert
        self.button = ttk.Button(self, text="Convert", command=self.click)


def load_json(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def load_units(file_name):
    set_units = load_json(file_name)
    units = []
    for category in set_units:
        for unit in set_units[category]:
            units.append(unit)
    return units


if __name__ == "__main__":
    app = ConverterApp()
    app.mainloop()
