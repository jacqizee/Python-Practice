import unittest
from assignment import label_nodes
from tree_node import TreeNode

class TestAssignment(unittest.TestCase):
    def setUp(self) -> None:
        print('\n')

    def test_1(self):
        root = TreeNode(0, 0)
        one = TreeNode()
        two = TreeNode()
        three = TreeNode()
        four = TreeNode()
        five = TreeNode()
        six = TreeNode()
        seven = TreeNode()

        root.add_child(one)
        one.children = [two, three]
        two.children = [four, five]
        five.children = [six, seven]

        print('one')
        label_nodes(root)
        self.assertEqual(root.return_coords(), [(0, 0), (1, 0), (2, 0), (2, 3), (3, 0), (3, 1), (4, 1), (4, 2)])

    def test_2(self):
        root = TreeNode(0, 0)
        one = TreeNode()
        two = TreeNode()
        three = TreeNode()
        four = TreeNode()
        five = TreeNode()
        six = TreeNode()
        seven = TreeNode()
        eight = TreeNode()

        root.add_child(one)
        one.children = [two, three]
        two.children = [four, five]
        three.children = [eight]
        five.children = [six, seven]

        label_nodes(root)
        self.assertEqual(root.return_coords(), [(0, 0), (1, 0), (2, 0), (2, 3), (3, 0), (3, 1), (3, 3), (4, 1), (4, 2)])
    
    def test_3(self):
        root = TreeNode(0, 0)
        one = TreeNode()
        two = TreeNode()
        three = TreeNode()
        four = TreeNode()
        five = TreeNode()
        six = TreeNode()

        root.children = [one, two]
        one.children = [three, four]
        two.children = [five, six]

        label_nodes(root)
        self.assertEqual(root.return_coords(), [(0, 0), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3)])

    def test_4(self):
        root = TreeNode(0, 0)
        one = TreeNode()
        two = TreeNode()
        three = TreeNode()
        four = TreeNode()
        five = TreeNode()
        six = TreeNode()
        seven = TreeNode()
        eight = TreeNode()
        nine = TreeNode()

        root.children = [one]
        one.children = [two, three]
        two.children = [four, five]
        five.children = [six, seven]
        three.children = [eight]
        eight.children = [nine]

        label_nodes(root)
        self.assertEqual(root.return_coords(), [(0, 0), (1, 0), (2, 0), (2, 3), (3, 0), (3, 1), (3, 3), (4, 1), (4, 2), (4, 3)])

    def test_5(self):
        root = TreeNode(0, 0)
        one = TreeNode()
        two = TreeNode()
        three = TreeNode()
        four = TreeNode()
        five = TreeNode()
        six = TreeNode()
        seven = TreeNode()

        root.children = [one, two, three]
        one.children = [four, five, six, seven]

        label_nodes(root)
        self.assertEqual(root.return_coords(), [(0, 0), (1, 0), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3)])
    
    def test_6(self):
        root = TreeNode(0, 0)
        one = TreeNode()
        two = TreeNode()
        three = TreeNode()
        four = TreeNode()
        five = TreeNode()
        six = TreeNode()
        seven = TreeNode()
        eight = TreeNode()
        nine = TreeNode()
        ten = TreeNode()

        root.children = [one, two, three]
        one.children = [four, five, six]
        four.children = [ten]
        two.children = [seven, eight]
        three.children = [nine]

        label_nodes(root)
        self.assertEqual(root.return_coords(), [(0, 0), (1, 0), (1, 3), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0)])

if __name__ == '__main__':
    unittest.main()