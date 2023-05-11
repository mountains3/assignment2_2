# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:07:27 2023

@author: Lenovo
"""

import tkinter as tk
from gui import GUI

# Create the main window
window = tk.Tk()
window.title("Analysis of the location of physical activity")
window.geometry('1500x600')

# Create the GUI object
app = GUI(window)

# Start the main loop
window.mainloop()
