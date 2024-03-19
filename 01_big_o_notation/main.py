# This algorithm has a O(n) time complexity (linear time)
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n * n)
    return squared_numbers


# This algorithm has a O(1) time complexity (constant time)
def find_first_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe


# This algorithm has a O(n^2) time complexity (squared time)
def has_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False


# This algorithm has a time complexity of a*n^2 + b*n + c
# To put it into big O terms, it has a O(n^2) time complexity
def find_duplicate_positions(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.append(numbers[i])

    positions = []
    for i in range(len(numbers)):
        if numbers[i] in duplicates:
            positions.append(i)
    return positions


# 1 - Fastest growing terms are kept
# 2 - Constants are dropped

# Take this function for example:
# time = 5*n^2 + 3*n + 20

# As the value of n grows, the rest of the function becomes irrelevant
# Example: n = 1000

# time = 5*1000^2 + 3*1000 + 20
# time = 5000000 + 3000 + 20
# time = 5000000 + 3020

# 3020 becomes irrelevant compared to 5000000


# This algorithm has linear time complexity
# It works for unsorted lists, but wastes time in sorted lists
def linear_search(numbers, num):
    for i in range(len(numbers)):
        if numbers[i] == num:
            return i
    return -1


# With each iteration, the number of steps is cut in half
# So, in big O terms, it has logarithmic time, O(log n)
def binary_search(numbers, num):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = len(numbers) // 2
        if numbers[middle] == num:
            return middle
        elif numbers[middle] < num:
            left = middle + 1
        else:
            right = middle - 1
    return -1
