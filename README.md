# EPAi Session 7  - Scopes and Closures

## Global and Local Scopes

Lexical Scope: The portion of the code where the assignment of a varibale to an object is binded, is called Lexical Scope of just Scope. The info about Scopes are stored in namespaces.

The all enclosing scope is built-in scope and the objects defined here (basically Python builins) are available across any module/file/class etc.

The highest level of scope **user-defined** scope is a <u>Module</u> i.e. variables assigned in one module are not visible to another module. This scope is called Global Scope.

Enlosing Scope: If a variable referenced in a scope is not defined there, it is search sequentially in the first enclosing scope, then the next enclosing scope and so on till the build-in scope. If the variable is not found till there - Python will say - object not found!

That implies, a varible, once defined, is available to all enclosed scope. 



## But

what would happen if we **assign** that variable with some value in the enclosed scope? This creates a NEW LOCAL VARIBALE in the enclosing scope. This newly created variable **MASKS** the variable from the enclosing scope!


Local -> Global -> build-in

```python
a = 10

def my_func():
    print(a) # Accesses a present in enclosing scope. prints 10

my_func()
```


```python
a = 10

def my_func():
    a = 5 # creates a new varibale `a` for scope of my_func(). Different from `a` of line 1
    print(a) # prints 5

my_func()
```

What if I want to **change** the varible present in the outer scope? We have a special keyword in Python called **global**

```python
a = 10

def my_func():
    global a # makes `a` of line 1 available for modification
    print(a) # prints 10
    a = 5 # DO NOT create a new ``a`` but changes the ``a`` from enclosing scope. Thanks to ``global``

my_func()
```


Note: For every function call a new scope is created and the new sets of variables are defined in that scope.

## Compile and Run time

What happens at Compile Time?

For a function definition, Python will look for all variable references

- if **assignments** are present - <u> Those variables are marked as local</u>, unless they are Global.

- if **assignments** are NOT present - <u>look them in the enclosing scope</u>

```python

a = 10

def f1():
    print(a) # only reference, no assignment - during Compile Time marked as Non-Local

def f2():
    a =1 # assignment - during Compile Time marked as local 

def f3():
    global a
    a = 1 # assignment - during Compile Time marked as global

def f4():
    print(a)
    a = 9 # assignment - during Compile Time marked as local 


f4()   #  NOTE: Run-time eror - as local var `a` is reference before declaration

```

## Non - Local Scopes

A function has its own local scope and global scope and built-in scope.

For nested functions - inner function also has access to the scope of outer function - enclosing scope - This is known as Non-Local Scope!
To acess a varibale of non-local scope, we need to use the keyword **nonlocal**

Beware 1: It will only look till last non-local scopes and not in Global or buil-in scope.

Beware 2: **nonlocal** only gives access to local variables of enclosing scope i.e. if the var is pulled into the enclosing scope from global scope - it will give Run-time error!

```python
a = 10
def outer():
    global a
    def inner():
        nonlocal a  # SyntaxError: no binding for nonlocal 'a' found
        a = 5
    inner()

```

## Closure
Suppose you need to count the number of time a user clicked a button on a webpage (tracking onClick) 

Approach I : 

```python
count = 0
def updateClickCount() : 
    count += 1
```
    
But, the pitfall is that any script on the page can change the counter, without calling updateClickCount( ) 

Approach 2: Let's then declare the variable inside the function! 

```python
def updateClickCount( ) : 
    count = 0
    count +=1 
```

Oops! Everytime we call updateC1 ickCount() function, counter is set to 0 and then 1 

Approach 3: Nested Functions!

```python
def countWrapper() : 
    count = 0
def updateC1ickCount(): 
    count = 1 
    updateClickCount( ) 
    return count 

 ```   
This COULD have solved the problem, ONLY if we could reach updateClickCount( ) fn from the outside and we also need to find a way to 
execute count = O only once not every time 


### Free Variables and Closure

Solution to above dilemma are <u>NonLocal variables</u>!

```python


def outer():
    counter = 0
    def inner():
        counter += 1 # This is called a Free Variable!
    return inner

fn = outer() # This actually returns the inner() - hence it is called Closure!
fn()

```
- Please appreciate why `counter` is called Free variable
- when `fn = outer()` finishes, `outer() `is completely executed.
- still when `fn()` i.e. `inner()` is called - it has access to the `outer()` variable i.e. `counter`. 
- Thus though the `outer()` dies, still `counter`lives as *Free varibale* of `inner()`
- The memory where `counter` exists and is allocated to both `outer()` and `inner()` is called a **cell**

- Hence, **Closure = Function + Extended Scope**



Please refer to docstrings for the explanation of functions of session7.py and test_session7.py

