from functools import wraps

def required_admin(func):
    """
    A decorator to check if the user has the required role to access a function.
    
    :param required_role: The role required to access the function.
    """
    @wraps(func)
    def wrapper(user_role):
        if user_role != 'admin':
            print("Access denied: Admins only.")
            return None
        else:
            return func(user_role)
    return wrapper

@required_admin
def access_admin_panel(user_role):
    print("Access granted to admin panel.")

access_admin_panel('user')  # Should print access denied message
access_admin_panel('admin')  # Should print access granted message
    