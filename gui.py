# -*- coding: utf-8 -*-
"""
Created on Wed May 09 22:07:27 2023

@author: Lenovo
"""

import tkinter as tk
from tkinter import filedialog
from data_processing import calculate_slope, calculate_aspect
from data_display import display_data
import numpy as np

class GUI:
    def __init__(self, master):
        # Initialize the GUI window and set initial values for data variables
        self.master = master
        self.elevations = None
        self.max_slopes = None
        self.aspect = None
        
        # Create the buttons
        load_button = tk.Button(text="Load data", command=self.load_data)
        load_button.pack()
        
        # Disable the save button until data has been loaded
        self.save_button = tk.Button(text="Save Image", command=self.save_fig, state='disabled')
        self.save_button.pack()

    def load_data(self):
        # Open a file dialog to select a data file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            # Load elevation data from file
            self.elevations = np.loadtxt(file_path)
            
            # Calculate maximum slopes and aspect from elevation data
            cell_size = 1
            self.max_slopes = calculate_slope(self.elevations, cell_size)
            self.aspect = calculate_aspect(self.elevations, cell_size)
            
            # Save the calculated data to files
            np.savetxt(file_path + "_max_slopes.txt", self.max_slopes)
            np.savetxt(file_path + "_aspect.txt", self.aspect)
            
            # Display the data in the GUI
            display_data(self.elevations, self.max_slopes, self.aspect, self.master)
            
            # Enable the save button
            self.save_button.configure(state='normal')
            
    def save_fig(self):
        # Open a file dialog to select a file name and location for the image file
        filetypes = [('PNG Image', '*.png'), ('JPEG Image', '*.jpg')]
        file_path = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension='.png')
        
        # If a file path is chosen, save the image file
        if file_path:
            display_data.save_fig(file_path)




