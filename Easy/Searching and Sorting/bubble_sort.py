input = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_array = bubble_sort(input)
print(sorted_array)
# Notes
# Bubble sort repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
# The pass through the list is repeated until the list is sorted.
# The algorithm gets its name because smaller elements "bubble" to the top of the list.