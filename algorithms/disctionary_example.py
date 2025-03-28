# 1. Two Sum (LeetCode 1)
def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i
    return []

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """
       Groups anagrams together using sorted word as key.
       Time Complexity: O(n * k log k) where k = length of each word
       Space Complexity: O(n)
       """
    anagram_map = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())
def is_isomorphic(s, t):
    """
    Checks if two strings are isomorphic.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(s) != len(t):
        return False

    map_st, map_ts = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in map_st and map_st[c1] != c2) or (c2 in map_ts and map_ts[c2] != c1):
            return False
        map_st[c1] = c2
        map_ts[c2] = c1
    return True

def length_of_longest_substring(s):
    """
    Returns the length of the longest substring without repeating characters.
    Uses sliding window with hash map.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Sample test
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print("Two Sum result:", two_sum(nums, target))

    # Group Anagrams
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped Anagrams:", group_anagrams(words))

    # Isomorphic Strings
    print("Is 'egg' and 'add' isomorphic?", is_isomorphic("egg", "add"))
    print("Is 'foo' and 'bar' isomorphic?", is_isomorphic("foo", "bar"))

    # Longest Substring Without Repeating Characters
    s = "abcabcbb"
    print("Length of Longest Substring:", length_of_longest_substring(s))
