from functools import wraps

def logging_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Logging: Called function '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Logging: Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@logging_activity
def brew_coffee(coffee_type, size="medium", sugar=False):
    return f"Brewing a cup of {coffee_type} with size and sugar: {size} {', with sugar' if sugar else 'without sugar'}."

brew_coffee("espresso")