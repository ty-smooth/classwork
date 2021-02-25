# Coding Exercise 1

import logging
logging.basicConfig(filename='output.log', format='%(message)s', level=logging.INFO)

import numpy as np

arr = np.zeros(10)
logging.info(f"Problem 2: {arr}")

arr = np.ones(10)
logging.info(f"Problem 3: {arr}")

arr = np.ones(10)*5
logging.info(f"Problem 4: {arr}")

arr = np.arange(10, 51)
logging.info(f"Problem 5: {arr}")

arr = np.arange(10, 51, 2)
logging.info(f"Problem 6: {arr}")

arr = np.arange(9).reshape(3, 3)
logging.info(f"Problem 7: {arr}")

arr = np.identity(3)
logging.info(f"Problem 8: {arr}")

num = np.random.rand(1)
logging.info(f"Problem 9: {num}")
