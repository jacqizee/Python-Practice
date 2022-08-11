from nodes import ListNode

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, node_value):
        node_to_add = ListNode(node_value)
        node_to_add.next = self.head
        self.head = node_to_add

    def add_to_tail(self, node_value):
        if self.head is None:
            self.add_to_head(node_value)

        node_to_add = ListNode(node_value)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node_to_add
            
    def insert_after(self, node_value, prev_node):
        node_to_add = ListNode(node_value)
        