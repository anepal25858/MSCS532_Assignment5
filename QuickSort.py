import random
import time

# Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Middle element Pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort
def randomizedQS(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]  # Random pivot selection
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomizedQS(left) + middle + randomizedQS(right)

def measure_time(arr, sort_function):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

# Test case
test = [33, 10, 59, 27, 16, 75, 44, 18, 22, 50]

deterministic = quicksort(test)
randomized = randomizedQS(test)

# Print results
print(f"Test Array: {test}")
print(f"Deterministic Quicksort: {deterministic}")
print(f"Randomized Quicksort: {randomized}")

# Test arrays
def testCases(size):
    randomArr = [random.randint(0, size) for _ in range(size)]
    sortedArr = list(range(size))
    reverseArr = list(range(size, 0, -1))
    return randomArr, sortedArr, reverseArr

#different input size
if __name__ == "__main__":
    input = [100, 1000, 5000, 10000]
    for size in input:
        print(f"\nArray size: {size}")
        randomArray, sortedArray, reverseArray = testCases(size)

        # Testing Randomized Quicksort
        print("\nRandomized Quicksort:")
        print(f"Random Array: {measure_time(randomArray, randomizedQS):.5f} seconds")
        print(f"Sorted Array: {measure_time(sortedArray, randomizedQS):.5f} seconds")
        print(f"Reverse Sorted Array: {measure_time(reverseArray, randomizedQS):.5f} seconds")

        # Testing Deterministic Quicksort
        print("\nDeterministic Quicksort (first element as pivot):")
        print(f"Random Array: {measure_time(randomArray, quicksort):.5f} seconds")
        print(f"Sorted Array: {measure_time(sortedArray, quicksort):.5f} seconds")
        print(f"Reverse Sorted Array: {measure_time(reverseArray, quicksort):.5f} seconds")



