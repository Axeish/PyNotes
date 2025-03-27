# LeetCode 88
def merge_sorted_arrays(nums1, m, nums2, n):
    """
    LeetCode 88 (in-place version)

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums2 into nums1 as one sorted array in-place.
    nums1 has extra space (length m + n) to hold additional elements from nums2.

    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge in reverse order
    # This method merges nums2 into nums1 from the back
    # It avoids overwriting values by filling nums1 from the end
    # This achieves O(1) space complexity (in-place)
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If any elements left in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# LeetCode 268
def find_missing_number(arr):
    """
    Finds the missing number from 0 to n in an array of size n-1.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr) + 1
    expected_sum = n * (n - 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# LeetCode 704
def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    Returns the index or -1 if not found.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# LeetCode 26
def remove_duplicates_sorted(arr):
    """
    Removes duplicates from a sorted array in-place.
    Returns the array up to the unique count.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return []
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]

# Sample test (can be removed or expanded into pytest later)

# LeetCode 283
def move_zeroes(arr):
    """
    Moves all zeroes to the end of the array while maintaining the order of non-zero elements.
    In-place using two pointers.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    insert_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos] = arr[i]
            insert_pos += 1
    for i in range(insert_pos, len(arr)):
        arr[i] = 0
    return arr

# Sample test (can be removed or expanded into pytest later)
if __name__ == "__main__":
    print("Merge Sorted Arrays:")
    nums1 = [1,2,3,0,0,0]
    merge_sorted_arrays(nums1, 3, [2,5,6], 3)
    print(nums1)

    print("Find Missing Number:", find_missing_number([0, 1, 3]))
    print("Binary Search (target=3):", binary_search([1, 2, 3, 4, 5], 3))
    print("Remove Duplicates:", remove_duplicates_sorted([1, 1, 2, 2, 3]))
    print("Move Zeroes:", move_zeroes([0, 1, 0, 3, 12]))