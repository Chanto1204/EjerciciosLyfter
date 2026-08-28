
def order_string(text):
    
    my_list = text.split("-")
    my_list.sort()
    result = "-".join(my_list)

    return result


text = "python-variable-funcion-computadora-monitor"
result = order_string(text)
print(result)