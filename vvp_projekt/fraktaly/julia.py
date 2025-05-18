"""Funkce pro výpočet Juliovy množiny."""
import numpy as np
from numba import jit

@jit(nopython=True)
def julia(z: complex, c: complex, max_iter: int) -> int:
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter
