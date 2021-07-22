from functools import wraps

user = {'username': 'john', 'access_level': 'admin'}


def user_has_permission(access_level):  # getting 'admin' argument passed to decorator assignment
    def my_decorator(func):
        @wraps(func)  # gives changed by decorator function its' original name and doc info
        def secure_func(*args, **kwargs):
            if user.get('access_level') == access_level:
                return func(*args, **kwargs)

        print('Return permission1')
        return secure_func
    print('Return permission2')
    return my_decorator


def name_starts_with_j(func):
    @wraps(func)
    def secure_name_check(*args, **kwargs):
        if user.get('username').startswith('j'):
            print('Name correct')
            return func(*args, **kwargs)
        else:
            print('Name doesn\'t start with "j"')
    print('Return name')
    return secure_name_check


@user_has_permission('admin')  # passing access_level value to decorator, if fails - @name_starts_with_j doesn't run even if its' value is correct
@name_starts_with_j
def my_function(panel):
    """
    Returns admin password
    """
    return f'Password for {panel} panel: 1234.'


print(my_function(panel='movies'))

