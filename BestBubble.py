# BestBubble
# Problem Description
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. The problem with bubble sort is its worst case scenario. When the smallest element is in the last position, then it takes more time to sort in ascending order, but takes less time to sort in descending order.

# An array is called beautiful if all the elements of the array are in either ascending or descending order. Given an array of numbers, find the minimum swap operations required to make the array beautiful.

# Constraints
# 0 < N < 1000

# 0 < Arr[i] < 1000

# Input
# First line contains of integer N denoting number of elements in the array.

# Second line consist of N integers separated by space denoting the elements of the array.

# Output
# Single integer denoting the least numbers of swap operations required to make the array beautiful.

# Time Limit (secs)
# 1

# Examples
# Example 1:

# Input:

# 5

# 4 5 3 2 1

# Output:

# 1

# Explanation:

# The number of swaps required to sort the elements in ascending order is 9.

# The number of swaps required to sort the elements in descending order is 1.

# The best way is to sort in descending order and swaps required is 1.

# Example 2:

# Input:

# 5

# 4 5 1 2 3

# Output 2:

# 4





#Code
def count_bubble_sort_swaps(arr, ascending=True):
    n = len(arr)
    swap_count = 0
    sorted_array = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and sorted_array[j] > sorted_array[j + 1]) or (not ascending and sorted_array[j] < sorted_array[j + 1]):
                sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]
                swap_count += 1
    return swap_count

def min_swaps_to_make_beautiful(arr):
    ascending_swaps = count_bubble_sort_swaps(arr, ascending=True)
    descending_swaps = count_bubble_sort_swaps(arr, ascending=False)

    return min(ascending_swaps, descending_swaps)

N = int(input())
arr = list(map(int, input().split()))

print(min_swaps_to_make_beautiful(arr))