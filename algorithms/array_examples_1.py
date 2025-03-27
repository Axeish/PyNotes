# arrays/examples.py

"""
Basic array operations implemented from scratch for understanding.
"""

# 1. Reverse an array

def reverse_array(arr):
    """
    Reverses the entire array using slicing.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return arr[::-1]

# 2. Rotate array to the right by k positions

def rotate_array(arr, k):
    """
    Rotates the array to the right ( negative indexes) by k positions.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    k %= len(arr)
    return arr[-k:] + arr[:-k]

# 3. Find max subarray sum (Kadane’s Algorithm)

def max_subarray_sum(arr):
    '''
    Implements Kadane's algorithm to find the maximum sum of any subarray.
    find max up to the last index
    find max of total
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    max_sum = curr_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# 4. Check if array has duplicates

def has_duplicates(arr):
    """
    Checks if the array contains any duplicate values.
    Compares length of array and set of array.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return len(set(arr)) != len(arr)

# 5. Implement prefix sum

def prefix_sum(arr):
    """
    Builds an array where each element at index i
    stores the sum of elements from 0 to i.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

# 6. Sliding window: max sum of subarray of size k
# LeetCode 643
def max_sum_subarray_k(arr, k):
    """
       Finds the maximum sum of a subarray of length k using sliding window.
       Steps:
       - Compute sum of first k elements as initial window
       - Slide window: subtract leftmost, add next element
       - Keep track of max sum seen so far
       Time Complexity: O(n)
       Space Complexity: O(n)
    """
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Sample test (can be removed or expanded into pytest later)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print("Reverse:", reverse_array(arr))
    print("Rotate by 2:", rotate_array(arr, 2))
    print("Max Subarray:", max_subarray_sum(arr))
    print("Has Duplicates:", has_duplicates([1, 2, 3, 4, 1]))
    print("Prefix Sum:", prefix_sum(arr))
    print("Max Sum Subarray of size 3:", max_sum_subarray_k(arr, 3))