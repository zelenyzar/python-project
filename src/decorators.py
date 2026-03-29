import os
from functools import wraps


def log(filename=None):
    """Декоратор для фиксации запуска и выполнении функции"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_func = f"запуск {func.__name__}"
            result_func = None
            try:
                result_func = func(*args, **kwargs)
                result_str = f"{func.__name__} ok"
            except Exception as e:
                error_type = type(e).__name__
                result_str = f"{func.__name__} error: {error_type} {e}. Inputs: {args}, {kwargs}."

            if filename:
                dir = os.getcwd()
                path = os.path.join(dir,'data', f'{filename}.txt')
                with open(path, 'w', encoding='utf8') as f:
                    f.write(f"{start_func}\n{result_str}")
            else:
                print(start_func)
                print(result_str)
            return result_func
        return wrapper
    return decorator
