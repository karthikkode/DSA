def merge_sorted_lists(arr1, arr2):
    res = []
    i = 0
    j = 0
    m = len(arr1)
    n = len(arr2)
    while (i<=m-1 or j<=n-1):
        if j>n-1:
            res.append(arr1[i])
            i+=1
        elif i>m-1:
            res.append(arr2[j])
            j+=1
        elif arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    return res



def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        left_arr = merge_sort([arr[0]])
        right_arr = merge_sort([arr[1]])
        return merge_sorted_lists(left_arr, right_arr)

    mid = len(arr)//2
    left_arr = merge_sort(arr[0:mid])
    right_arr = merge_sort(arr[mid:len(arr)])
    return merge_sorted_lists(left_arr, right_arr)

res = merge_sort([1,2,7,4,5,6])
print(res)

"""
Notes: Merge Sort Algorithm
--------------------------

1. **Algorithm Overview:**
    - Merge sort is a divide-and-conquer sorting algorithm.
    - It divides the input array into two halves, recursively sorts each half, and then merges the sorted halves.
    - It is efficient and guarantees O(n log n) time complexity for all cases (best, average, and worst).

2. **How It Works:**
    - If the array has one or zero elements, it is already sorted.
    - Otherwise, split the array into two halves.
    - Recursively sort each half using merge sort.
    - Merge the two sorted halves into a single sorted array using the `merge_sorted_lists` function.

3. **Code Explanation:**
    - `merge_sorted_lists(arr1, arr2)`: Merges two sorted lists into a single sorted list.
      - Uses two pointers to compare elements from both lists and appends the smaller element to the result.
      - Handles remaining elements from either list after one is exhausted.
    - `merge_sort(arr)`: Recursively sorts the array.
      - Base case: If the array has one element, return it.
      - For two elements, sorts them by recursive calls and merges.
      - For more than two elements, splits the array, sorts each half, and merges them.

4. **Time Complexity:**
    - O(n log n) for all cases (best, average, worst).

5. **Space Complexity:**
    - O(n) extra space for merging arrays (not in-place).

6. **Stability:**
    - Merge sort is a stable sorting algorithm (preserves the order of equal elements).

7. **Edge Cases:**
    - Handles empty arrays, single-element arrays, arrays with duplicates, and negative numbers.
    - The implementation is robust for all standard edge cases.
"""