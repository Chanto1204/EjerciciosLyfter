
def is_prime(number):
    if number < 2:
        return False
    for divider in range(2 , number):
        if number % divider == 0:
            return False

    return True

def get_prime_number(my_list): 
    new_list = []
    for number in my_list:
        if is_prime(number):
            new_list.append(number)
            
    return new_list


my_list = [1, 4, 6, 7, 13, 9, 67]

result = get_prime_number(my_list)
print(result)


