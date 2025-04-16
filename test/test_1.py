from model import Problem
from model import to_np_array
from algorithms import *

def make_test(func):
    func.__is_test__ = True
    return func

@make_test
def one_equals_true():
    assert 1 == True

@make_test
def zero_equals_true():
    assert 0 == True

@make_test
def create_problem_sample():
    sample_capacity = 20
    sample_items = [(1, 3, 2), (2, 4, 1), (3, 5, 4)]
    problem = Problem(sample_capacity, sample_items)
    assert sample_capacity == problem.total_capacity
    assert 4 == problem.items[0]['profit']

@make_test
def access_item_by_names():
    sample_capacity = 20
    sample_items = [(1, 3, 2), (2, 4, 1), (3, 5, 4)]

    problem = Problem(sample_capacity, sample_items)

    target_profit = 4

    assert sample_capacity == problem.total_capacity
    assert target_profit == problem.items[0]['profit']

@make_test
def sort_by_profit_weight():
    sample_capacity = 20
    sample_items = [(1, 3, 2), (2, 4, 1), (3, 5, 4)]

    problem = Problem(sample_capacity, sample_items)

    target_sorted_items =  to_np_array([(2, 4, 1), (1, 3, 2), (3, 5, 4)])

    assert True == (target_sorted_items == problem.items).all()
