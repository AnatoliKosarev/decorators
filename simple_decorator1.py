from functools import wraps

user = {'username': 'john', 'access_level': 'admin'}


def user_has_permission(access_level):  # getting 'admin' argument passed to decorator assignment
    def my_decorator(func):
        @wraps(func)  # gives changed by decorator function its' original name and doc info
        def secure_func(*args, **kwargs):
            if user.get('access_level') == access_level:
                return func(*args, **kwargs)
        return secure_func
    return my_decorator


@user_has_permission('admin')  # passing access_level value to decorator
def my_function(panel):
    """
    Returns admin password
    """
    return f'Password for {panel} panel: 1234.'


print(my_function(panel='movies'))
print(my_function.__name__)
print(my_function.__doc__)