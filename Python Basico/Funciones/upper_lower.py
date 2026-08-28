

def counter_letter(text):
    upper = 0
    lower = 0
    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1

    return upper, lower

text = "I love Nación Sushi"

upper, lower = counter_letter(text)

print(f"There's {upper} upper cases and {lower} lower cases")