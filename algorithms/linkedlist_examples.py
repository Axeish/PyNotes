# linked_lists/examples.py

"""
Basic linked list operations implemented from scratch in Python.
Covers definitions, common algorithms, and interview patterns.
"""

# Define a Node for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    """Helper function to print the linked list"""
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


# LeetCode 206

def reverse_linked_list(head):
    """
    Reverses a singly linked list.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# 2. Detect cycle in a linked list

# LeetCode 141

def has_cycle(head):
    """
    Uses Floyd’s Tortoise and Hare algorithm to detect a cycle.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
# LeetCode 876

def find_middle_node(head):
    """
    Uses fast and slow pointer technique.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# LeetCode 21

def merge_two_lists(l1, l2):
    """
    Merges two sorted linked lists and returns the head of the new list.
    Time Complexity: O(n + m)
    Space Complexity: O(1) (reuses existing nodes)
    """
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

def is_palindrome(head):
    """
    Checks whether the linked list is a palindrome.
    Reverses the second half and compares both halves.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp

    # Compare first half and reversed second half
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

def get_intersection_node(headA, headB):
    """
    Finds the intersection node of two linked lists, if any.
    Time Complexity: O(n + m)
    Space Complexity: O(1)
    """
    if not headA or not headB:
        return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# Sample test for reverse
if __name__ == "__main__":
    # Create 1 -> 2 -> 3 -> 4
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    print("Original Linked List:")
    print_linked_list(node1)

    reversed_head = reverse_linked_list(node1)
    print("Reversed Linked List:")
    print_linked_list(reversed_head)
