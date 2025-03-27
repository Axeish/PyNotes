class Linked:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printlink(head):
    result = []
    while head:
        result.append(str(head.val))
        head=head.next
    print(">".join(result))

b = Linked(7,None)
c = Linked(8,None)
e = Linked(1,None)
d = Linked(12,b)
c.next = d
e.next = c

printlink(e)