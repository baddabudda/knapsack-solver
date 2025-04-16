def make_test(func):
    func.__is_test__ = True
    return func

@make_test
def one_equals_true():
    assert 1 == True

@make_test
def zero_equals_true():
    assert 0 == True