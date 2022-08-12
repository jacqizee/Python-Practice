import unittest
from singly_linked import SinglyLinkedList
from nodes import ListNode

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        head = ListNode('hello')
        self.linked_list = SinglyLinkedList(head)
        self.linked_list.add_to_tail('hello!!!')

    def test_print_list(self):
        self.linked_list.print_list()

    def test_add_to_head(self):
        print(self.linked_list)
        self.linked_list.add_to_head('hello again')

if __name__ == '__main__':
    unittest.main()