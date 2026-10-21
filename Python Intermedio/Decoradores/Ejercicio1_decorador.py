def my_decorator(function):

    def wrapper(*args, **kwargs):
        print(f"Parámetros: {args} , {kwargs}")

        result = function(*args, **kwargs)

        print(f"Retorno: {result}")

        return result

        
    return wrapper



@my_decorator
def add(a, b):
    return a + b


add(5, 10)