def bubble_sort(numbers):
    for j in range(len(numbers) - 1):
        swapped = False

        for i in range(len(numbers) - 1 - j):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

    return numbers




numbers = [8, 3, 5, 1, 9, 2]

print("Lista ordenada:", bubble_sort(numbers))


