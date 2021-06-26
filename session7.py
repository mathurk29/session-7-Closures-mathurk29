def closure_docstring():
    ''' Returns a closure. 
        
        Closure: Takes a function and returns a boolean whether the docstring of fn is greater than 50 or not.
        
    '''
    doc_length = 0
    def inner(fn):
        nonlocal doc_length
        doc_length = len(fn.__doc__) if fn.__doc__ else 0
        return True if doc_length > 50 else False
        
    return inner
    
################################################################################################################################################################################################

def next_fibonnaci():
    ''' 
        Returns a closure which calculates the next number in Fibonacci sequence.

        Free-vars are used to store the current state of the Fibonacci sequence.    
    '''
    fib1 = 0
    fib2 = 1
    count = 0
    def inner():
        nonlocal fib1, fib2
        nonlocal count
        suffix = 'st' if count ==1 else ('nd' if count == 2 else 'th')
        print(f'Here is your {count}{suffix} fib no: {fib1}')
        result = fib1
        temp = fib2
        fib2 += fib1
        fib1 = temp
        count += 1
        return result
    return inner

################################################################################################################################################################################################

arith_counter = {'add':0, 'mul':0,'div':0}


def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def arith(fn):
    ''' 
        Returns a closure which updates the global arith_counter with the number of times a function is called.

        Closre: The function passed with the extended scope of global counter arith_counter.
    '''  
    def inner(*args, **kwargs):
        global arith_counter
        arith_counter[fn.__name__] +=1 
        return fn(*args, **kwargs)
    return inner

print(arith_counter)

