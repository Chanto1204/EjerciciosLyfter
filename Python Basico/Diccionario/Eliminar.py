list_of_keys = ["access_level", "age"]

employee = {
    "name": "Sebastian",
    "email": "se121@ecorp.com",
    "access_level": 2,
    "age": 24
}

for key in list_of_keys:
    employee.pop(key)

print(employee)