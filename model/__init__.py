import numpy as np

def to_np_array(list) -> np.array:
    types = [('id', int), ('profit', int), ('weight', int)]
    return np.array(list, dtype=types)

class Problem:
    def __init__(self, total_capacity, items):
        self.total_capacity = total_capacity
        self.items = to_np_array(items)
    
    def get_item_profit(self, id):
        return self.items[id][1]
    
    def get_item_weight(self, id):
        return self.items[id][2]

class Result:
    def __init__(self, occupied_capacity, total_profit, items_taken):
        self.occupied_capacity = occupied_capacity
        self.total_profit = total_profit
        self.items_taken = to_np_array(items_taken)