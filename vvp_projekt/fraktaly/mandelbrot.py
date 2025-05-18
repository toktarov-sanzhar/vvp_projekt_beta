"""Funkce pro výpočet Mandelbrotovy množiny"""
import numpy as np
from numba import jit

@jit(nopython=True)
def mandelbrot(c: complex, max_iter: int) -> int:
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter
