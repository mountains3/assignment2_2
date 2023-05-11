# -*- coding: utf-8 -*-
"""
Created on Wed May 09 09:40:10 2023

@author: Lenovo
"""
import numpy as np

# Define a function to calculate the maximum slope for each pixel
def calculate_slope(data, cell_size):
    rows = len(data)
    cols = len(data[0])

    # Pad the data with edge values
    padded_data = np.pad(data, ((1, 1), (1, 1)), mode='edge')

    # Initialize a blank list to store the maximum slope for each pixel
    max_slope = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate over each pixel
    for row in range(rows):
        for col in range(cols):
            # Get the elevation of the current pixel
            current_elevation = padded_data[row+1][col+1]

            # Initialize the maximum difference and maximum slope value
            max_diff = 0
            max_slope_value = 0

            # Iterate over the 8 neighboring pixels of the current pixel
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue

                    # Calculate the row and column indices of the neighboring pixel
                    new_row, new_col = row + i + 1, col + j + 1

                    # Calculate the elevation difference between the neighboring pixel and the current pixel
                    diff = abs(current_elevation - padded_data[new_row][new_col])

                    # Record the maximum elevation difference
                    max_diff = max(max_diff, diff)

                    # Calculate the slope value between the neighboring pixel and the current pixel
                    max_slope_value = max(max_slope_value, max_diff / (np.sqrt(i ** 2 + j ** 2) * cell_size))

            # Store the Rate of elevation change value of the current pixel in the max_slope list
            max_slope[row][col] = round(max_slope_value, 2)

    # Return the list of Rate of elevation change values for each pixel
    return max_slope


# Define a function to calculate the aspect (slope direction) for each pixel
def calculate_aspect(data, cell_size):
    rows = len(data)
    cols = len(data[0])

    # Pad the data with edge values
    padded_data = np.pad(data, ((1, 1), (1, 1)), mode='edge')

    # Initialize a blank list to store the aspect (slope direction) for each pixel
    aspect = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate over each pixel
    for row in range(rows):
        for col in range(cols):
            # Use the padded data to calculate the slope direction of the current pixel
            dz_dx = ((padded_data[row+1][(col + 1) % (cols+2)] - padded_data[row+1][(col - 1) % (cols+2)]) / (2 * cell_size))
            dz_dy = ((padded_data[(row + 1) % (rows+2)][col+1] - padded_data[(row - 1) % (rows+2)][col+1]) / (2 * cell_size))
            aspect[row][col] = round((np.rad2deg(np.arctan2(dz_dy, -dz_dx)) + 360) % 360, 2)

    # Return the list of aspect (slope direction) values for each pixel
    return aspect



