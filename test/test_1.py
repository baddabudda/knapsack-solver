from model import Problem

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
    assert 4 == problem.items[1][1]
