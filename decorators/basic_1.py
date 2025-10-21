from functools import wraps

def decorator_function(original_function):
    @wraps(original_function)
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        original_function()
        print("Wrapper executed this after {}".format(original_function.__name__))
    return wrapper_function

@decorator_function
def greet():
    print("Hello, World!")

greet()

print(greet.__name__) # This will print 'wrapper_function' instead of 'greet'
# after @wraps(original_function), it would be 'greet'


