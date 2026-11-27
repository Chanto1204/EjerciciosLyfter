def bubble_sort(numbers):
    for j in range(len(numbers) - 1):  # O(n)
        swapped = False  # O(1)

        for i in range(len(numbers) - 1 - j):  # O(n) 
            if numbers[i] > numbers[i + 1]:  # O(1)
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # O(1)
                swapped = True  # O(1)

        if not swapped:  # O(1)
            break  # O(1)

    return numbers  # O(1)


numbers = [8, 3, 5, 1, 9, 2]

print("Lista ordenada:", bubble_sort(numbers))

