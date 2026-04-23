import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers.copy()
    for num in range(len(numbers)):
        idx_min = num
        for n in range(num + 1, len(numbers)):
            if numbers[n] < numbers[num]:
                num = n
        numbers[num],numbers[idx_min] = numbers[idx_min], numbers[num]

    return numbers

def bubble_sort(numbers):
    numbers = numbers.copy()
    for num in range(len(numbers)):
        for n in range(0, len(numbers) - num - 1):
            if numbers[n] > numbers[n + 1]:
                numbers[n], numbers[n + 1] = numbers[n + 1], numbers[n]
    return numbers

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    print(selection_sort([5, 1, 4, 2, 8]))
    print(selection_sort(random_numbers(20)))
    print(bubble_sort([5, 1, 4, 2, 8]))
    print(bubble_sort(random_numbers(20)))
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

numbers = [5, 1, 4, 2, 8]

