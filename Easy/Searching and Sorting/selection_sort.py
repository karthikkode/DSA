input = [64, 34, 25, 12, 22, 11, 90]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

sorted_array = selection_sort(input)
print(sorted_array)
# Notes
# Selection sort divides the input list into two parts: the sorted part and the unsorted part.
# It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part
# and moves it to the end of the sorted part.