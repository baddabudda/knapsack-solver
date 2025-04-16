import numpy as np

class Problem:
    def __init__(self, total_capacity, items):
        types = [('id', int), ('price', int), ('weight', int)]
        self.total_capacity = total_capacity
        self.items = np.array(items, dtype=types)