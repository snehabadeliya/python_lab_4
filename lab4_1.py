def merge_sort(arr):
    # Base case: if the length of the array is 1 or less, return the array (since it's already sorted)
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    return merge(left, right)

def merge(left, right):
    # Create a new list to store the merged result
    result = []

    # Initialize indices for the left and right arrays
    i = j = 0

    # Merge the two arrays by comparing elements and adding the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left or right arrays
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage:
arr = [10,2,6,7,12,22]
arr = merge_sort(arr)
print(arr) 
