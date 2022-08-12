from nodes import ListNode

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        current_node = self.head
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        print(values)

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
            
    def insert_after_value(self, node_value, prev_value):
        node_to_add = ListNode(node_value)
        
        current_node = self.head

        while current_node.next:
            if current_node.value == prev_value:
                node_to_add.next = current_node.next
                current_node.next = node_to_add
            else:
                current_node = current_node.next
        
        print('Unable to find specified value, are you sure it is present in this linked list?')