import unittest
from bfs1 import findNodeByText, Node


SMALL_TREE = Node("1",[
    Node("2", [], "breadther"),
    Node("3"),
    Node("4", [
        Node("5"),
        Node("2", [], "deeper")
    ])
])

class TestBFS(unittest.TestCase):
    def test_bfs_on_small_tree(self):
        foundNode = findNodeByText(SMALL_TREE, "2")
        self.assertEqual(foundNode.note, "breadther")

if __name__ == '__main__':
    unittest.main()
