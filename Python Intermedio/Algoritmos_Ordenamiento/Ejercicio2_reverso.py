def bubble_sort(numbers):
    for j in range(len(numbers) - 1):
        swapped = False

        for i in range(len(numbers) - 1, j, -1):
            if numbers[i] < numbers[i - 1]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
                swapped = True

        if not swapped:
            break

    return numbers



numbers = [5, 3, 8, 1, 4]


print("Lista ordenada:", bubble_sort(numbers))
