def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # after each pass, the largest element moves to the end
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
sorted_arr = bubble_sort(arr[:])  # arr[:] keeps original array unchanged
print("Sorted array:", sorted_arr)
