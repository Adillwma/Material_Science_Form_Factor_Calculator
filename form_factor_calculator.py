# -*- coding: utf-8 -*-
# Form Factor Calculator v1.0.3
# Created on Wed Mar 30 04:20:08 2022
# Author: Adill Al-Ashgar
# Contact: adillwmaa@gmail.com

import numpy as np

def find_form_factor(length, width, shape='strip', terms=10):
    """
    Calculates the form factor for a rectangular strip, or a cicular rod of homegenous material.
    When inputting the dimensions make sure length > width.

    Args:
        length (float): Length of the material strip or rod.
        width (float): Width of the rectangular strip or diameter of the rod.
        shape (str, optional): Shape of the material sample. Default is 'strip'. Options are 'strip' or 'rod'.
        terms (int, optional): Number of terms to use in the summation in the case of a strip. Default is 10 (summation is shown to converge around 10 terms).

    Returns:
        float: The calculated form factor for the material sample.

    Refrences:
        Strip: Read, B. E., and G. D. Dean. "The Determination of Dynamic Properties of Polymers and 
               Composites, Adam Hilger, Ltd." Herts, England (1978).

        Rod: 

    """    

    if shape == 'rod':
        form_factor = np.pi**4 * width * 0.25   # Simplfied from pi^4 * radius / 2 as we have diameter not radius

    elif shape == 'strip':
        summation=0
        for i in range(0, terms):
            summation = summation + (1 / ((2 * terms + 1)**5)) * np.tanh(((2 * terms + 1) * np.pi * length) / 2 * width)
        f = (1/3) * (1 - ((192 * width) / (np.pi**5 * length)) * summation)
        form_factor = length * width**3 * f

    return form_factor


# Example
length = 0.00234
width = 2E-4
print(f"Form factor: {find_form_factor(length, width)}")


