
def reverse_string(word):
    reverse_text = ""
    for index in range(len(word)-1,-1,-1):
        reverse_text += word[index]

    return reverse_text

word = "Hola mundo"

result = reverse_string(word)

print(result)