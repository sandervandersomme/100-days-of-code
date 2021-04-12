from unittest import TestCase
from Node import Node

class TestNode(TestCase):
    def test_get_value_no_link(self):
        test_node = Node(2)
        self.assertTrue(test_node.get_value() == 2)
        self.assertIsNone(test_node.link_node)

    def test_get_value_with_link(self):
        test_node = Node(2, Node(3))
        self.assertTrue(test_node.get_value() == 2)
        self.assertTrue(test_node.link_node.get_value() == 3)

    def test_get_link_node(self):
        neighbor = Node(3)
        test_node = Node(2, neighbor)
        self.assertTrue(test_node.get_link_node() == neighbor)
        self.assertTrue(test_node.get_link_node().get_value() == 3)

    def test_set_link_node(self):
        neighbor = Node(3)
        test_node = Node(2)
        test_node.set_link_node(neighbor)
        self.assertTrue(test_node.link_node == neighbor)
        self.assertTrue(test_node.link_node.get_value() == 3)
