def my_wraps(original_func):
    """
    Простой аналог functools.wraps:
    переносит __name__, __doc__ и __module__
    """

    def decorator(wrapper_func):
        wrapper_func.__name__ = original_func.__name__
        wrapper_func.__doc__ = original_func.__doc__
        wrapper_func.__module__ = original_func.__module__
        return wrapper_func

    return decorator
