class ListNode:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

class DoublyListNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev