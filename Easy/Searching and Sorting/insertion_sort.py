input = [1,2,3,4,5]

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        curr = i
        for j in range(i-1, -1, -1):
            if arr[j] < arr[curr]:
                break
            elif arr[j] > arr[curr]:
                arr[j], arr[curr] = arr[curr], arr[j]
                curr-=1
    
    return arr

sorted_array = insertion_sort(input)
print(sorted_array)

"""
Notes: Insertion Sort Algorithm
--------------------------------

1. **Algorithm Overview:**
    - Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
    - It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
    - It is efficient for small data sets and mostly sorted arrays.

2. **How It Works:**
    - The algorithm divides the array into a sorted and an unsorted part.
    - It iterates from the second element to the last element.
    - For each element, it compares it with the elements in the sorted part and inserts it into the correct position by shifting larger elements one position to the right.

3. **Code Explanation:**
    - The function `insertion_sort(arr)` takes a list `arr` as input.
    - `n = len(arr)` gets the length of the array.
    - The outer loop (`for i in range(n)`) iterates through each element.
    - `curr = i` keeps track of the current index being inserted.
    - The inner loop (`for j in range(i-1, -1, -1)`) compares the current element with each element in the sorted part (from right to left).
    - If an element in the sorted part is less than the current element, the loop breaks (since the correct position is found).
    - If an element in the sorted part is greater, the two elements are swapped, and `curr` is decremented to continue checking previous elements.
    - This process continues until the correct position is found for the current element.
    - The sorted array is returned.

4. **Time Complexity:**
    - Best Case: O(n) (when the array is already sorted)
    - Average and Worst Case: O(n^2)

5. **Space Complexity:**
    - O(1) (in-place sorting)

6. **Stability:**
    - Insertion sort is a stable sorting algorithm (does not change the relative order of equal elements).
"""
        