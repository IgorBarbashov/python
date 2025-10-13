import functools

# кастомный декоратор в функциональном стиле
# декотратор - это high order function
def decorator(func):
    def wrap(*args):
        count = 0
        while count < 10:
            func(*args)
            count +=1       
    return wrap


@decorator
def my_func(x: int, y: int) -> int:
    print(x + y)


# кастомный декоратор с параметрами в функциональном стиле
def param_decorator(limit):
    def decorator(func):

        @functools.wraps(func) # этот декоратор нужен чтобы корректно использовать метаданные функции к которой применяется декоратор
        def wrap(*args):
            count = 0
            while count < limit:
                func(*args)
                count +=1 
                print(count)      
        return wrap

    return decorator


@param_decorator(33)
def privet_func():
    """ Say Hello"""
    print("Hello")


class ClassDecorator:
    def __init__(self, func):

        # этот декоратор нужен чтобы корректно использовать метаданные функции к которой применяется декоратор
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *arg, **kwargs):
        count = 0
        while count < 10:
            self.func(*arg, **kwargs)
            count +=1 
            print(count)     


@ClassDecorator
def privet_class():
    """ Say Hello"""
    print("Hello")


if __name__ == "__main__":

    my_func(2, 2)

    privet_func()

    privet_class()

    print(privet_class.__name__) # видим метаданные вызываемой функции privet_class
    print(privet_class.__doc__)
