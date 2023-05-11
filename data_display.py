# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:07:28 2023

@author: Lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


def display_data(elevations, max_slopes, aspect, window):
    rows, cols = elevations.shape

    # Create a matplotlib figure
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))

    # Plot the elevation data
    im1 = axs[0].imshow(elevations, cmap='gray', interpolation='nearest')
    axs[0].set_title('Elevation Data')
    fig.colorbar(im1, ax=axs[0])

    # Plot the maximum slope data
    im2 = axs[1].imshow(max_slopes, cmap='viridis', interpolation='nearest')
    axs[1].set_title('Max Rate of elevation change')
    fig.colorbar(im2, ax=axs[1])

    # Calculate the slope angle for each pixel
    slope_angles = np.arctan(max_slopes) * (180 / np.pi)
    im3 = axs[2].imshow(slope_angles, cmap='magma', interpolation='nearest', vmin=0, vmax=90)
    axs[2].set_title('Slope (Angle) Data')
    fig.colorbar(im3, ax=axs[2])

    # Plot the aspect (slope direction) data
    im4 = axs[3].imshow(aspect, cmap='hsv', interpolation='nearest')
    axs[3].set_title('Aspect Data')
    fig.colorbar(im4, ax=axs[3])

    # Convert the matplotlib figure to a Tkinter-compatible image format
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


    # Add an explanation text box
    explanation = tk.Text(window, height=2, width=100)
    explanation.pack(side=tk.BOTTOM)
    explanation.insert(tk.END, "From left to right: Elevation Data, Max Rate of elevation change, Slope (Angle) Data, Aspect Data")
    explanation.configure(state='disabled')
