import session7
import random
import os
import inspect
import re

README_CONTENT_CHECK_FOR = [
    "Scopes",
    "Local",
    "Closure"
]

def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 550, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 25, 'You are not writing proper heading'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"




###############################################################################################################################################

def example0():
    pass

def example1():
    '''Rohan do not like short docstring. Work harder!'''
    pass

def example2():
    ''' This is a long docstring! Good job. Extra marks for good docstring.  '''
    pass

check_docstring = session7.closure_docstring()

def test_no_docstring():
    assert check_docstring(example0) == False, 'You can accept a function with empty docstring - but TSAI won\'t!'

def test_small_docstring():
    assert check_docstring(example1) == False, 'This was a small docstring, but you passed!'

def test_large_docstring():
    assert check_docstring(example2) == True, 'This was a large docstring, but you failed!'

def test_free_var():
    assert len(check_docstring.__code__.co_freevars) != 0, 'Oh! Did you think you would get away not using closures and freevars?'


#############################################################################################################################################


def test_fib_inital():
    next_fib = session7.next_fibonnaci()
    fib_series = []
    for _ in range(13):
        fib_series.append(next_fib())
    assert fib_series == [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], 'Pls check your logic'

def test_fibonacci_freevar():
    next_fib = session7.next_fibonnaci()
    print(next_fib.__code__.co_freevars)
    assert len(next_fib.__code__.co_freevars) != 0, 'Oh! Did you think you would get away not using closures and freevars?'

#############################################################################################################################################


def test_add():
    counter_add = session7.arith(session7.add)
    for _ in range(10):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        assert counter_add(x,y) == x + y, 'Wrong for addition of: ' + x + ' and ' + y
    assert session7.arith_counter['add'] == 10, 'Wrong for add'

def test_mul():
    counter_mul = session7.arith(session7.mul)
    for _ in range(10):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        assert counter_mul(x,y) == x * y, 'Wrong for multiplication of: ' + x + ' and ' + y
    assert session7.arith_counter['mul'] == 10, 'Wrong for multiply'

def test_div():
    counter_div = session7.arith(session7.div)
    for _ in range(10):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        if y == 0:
            continue
        assert counter_div(x,y) == x / y, 'Wrong for division of: ' + x + ' and ' + y
    assert session7.arith_counter['div'] == 10, 'Wrong for division'


#############################################################################################################################################

