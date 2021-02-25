# Coding Exercise 1

import logging
logging.basicConfig(filename='functional.log', format='%(message)s', level=logging.INFO)

import numpy as np

def create_zeros_array(number):
    arr = np.zeros(number)
    return arr

def create_ones_array(number, multiplier=1):
    arr = np.ones(number)
    arr = arr * multiplier
    return arr

def create_integer_array(start, stop, step=1):
    arr = np.arange(start, stop, step)
    return arr

arr = create_zeros_array(10)
logging.info(f"Problem 2: {arr}")

arr = create_ones_array(10)
logging.info(f"Problem 3: {arr}")

arr = create_ones_array(10, 5)
logging.info(f"Problem 4: {arr}")

arr = create_integer_array(10, 51)
logging.info(f"Problem 5: {arr}")

arr = create_integer_array(10, 51, 2)
logging.info(f"Problem 6: {arr}")

arr = create_integer_array(0, 9).reshape(3, 3)
logging.info(f"Problem 7: {arr}")

arr = np.identity(3)
logging.info(f"Problem 8: {arr}")

num = np.random.rand(1)
logging.info(f"Problem 9: {num}")
