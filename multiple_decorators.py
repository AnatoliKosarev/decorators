from functools import wraps

user = {'username': 'john', 'access_level': 'admin'}


def check_user_has_access(func):
    @wraps(func)
    def access_decorator(*args, **kwargs):
        if user.get('access_level') == 'admin':
            print('Permission granted')
            return func(*args, **kwargs)
        else:
            raise PermissionError('Access denied!')
    return access_decorator


def check_user_name_starts_with_j(func):
    @wraps(func)
    def name_decorator(*args, **kwargs):
        if user.get('username').startswith('j'):
            print('Name passed')
            return func(*args, **kwargs)
        else:
            raise PermissionError('Wrong name!')
    return name_decorator


@check_user_has_access
@check_user_name_starts_with_j
def core_function(panel):
    print(f'Secret {panel} info here.')


core_function('admin')