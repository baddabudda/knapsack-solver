from test import *

def is_test(test_candidate) -> bool:
    if not callable(test_candidate):
        return False
    if not hasattr(test_candidate, '__is_test__'):
        return False
    
    return True

for name in dir(test_1):
    test = test_1.__dict__[name]

    if not is_test(test):
        continue
    
    print('Running \"{}\" ...'.format(test.__name__))

    try:
        test()
        print('Test \"{0}\" \033[92;1mOK\033[0m'.format(test.__name__))
    except Exception as e:
        print('Test \"{0}\" \033[91;1mFAIL\033[0m'.format(test.__name__))
        print('\033[96mException type: {0} | Info: {1}\033[0m'.format(type(e).__name__, e.__doc__))
    
    print()
