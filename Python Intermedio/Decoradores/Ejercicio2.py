def validate_numbers(function):

    def wrapper(*args, **kwargs):

        for number in args:
            if not isinstance(number, (int, float)):
                raise TypeError("El parámetro debe ser un número")
        
        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise TypeError("El parámetro debe ser un número")

        result = function(*args, **kwargs)
        
        return result

    return wrapper


@validate_numbers
def add(a, b):
    return a + b


print(add(a=10, b=20))