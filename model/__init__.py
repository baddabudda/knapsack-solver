import numpy as np

def to_np_array(list) -> np.array:
    types = [('id', int), ('profit', int), ('weight', int)]
    return np.array(list, dtype=types)

class Problem:
    def __init__(self, total_capacity, items, apply_sort_by_ratio=True):
        self.total_capacity = total_capacity
        self.items = to_np_array(items)

        if apply_sort_by_ratio:
            self.sort_by_ratio()

    def sort_by_ratio(self):
        ratios = self.items['profit'] / self.items['weight']
        sorted_indices = np.argsort(-ratios)
        self.items = self.items[sorted_indices]

class Result:
    def __init__(self, occupied_capacity, total_profit, items_taken):
        self.occupied_capacity = occupied_capacity
        self.total_profit = total_profit
        self.items_taken = to_np_array(items_taken)