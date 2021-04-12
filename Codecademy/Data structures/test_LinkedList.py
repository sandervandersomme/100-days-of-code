from unittest import TestCase
from LinkedList import LinkedList
from Node import Node


class TestLinkedList(TestCase):
    def test_get_head(self):
        """
        Test if head is returned correctly
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        self.assertTrue(ll.get_head().get_value() == 6)

    def test_insert_new_head(self):
        """
        Test if a new node is correctly inserted at the beginning of the linked list
        """
        ll = LinkedList()
        ll.insert_new_head(2)
        self.assertTrue(ll.get_head().get_value() == 2)

    def test_remove_node_by_index(self):
        """
        Test if node at given index is removed correctly
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.insert_new_head(4)
        ll.insert_new_head(5)
        ll.insert_new_head(2)
        self.assertTrue(ll.stringify() == "2-5-4-3-6")
        ll.remove_node_by_index(2)
        self.assertTrue(ll.stringify() == "2-5-3-6")

    def test_remove_node_by_index_index_out_of_range(self):
        """
        Test if exception is raised when trying to remove a node at an
        index that is out of the range of the linked list
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.insert_new_head(4)
        ll.insert_new_head(5)
        ll.insert_new_head(2)
        self.assertTrue(ll.stringify() == "2-5-4-3-6")
        self.assertRaises(Exception, ll.remove_node_by_index, 5)

    def test_remove_node_by_index_index_is_tail(self):
        """
        Test if a tailing node is removed correctly from a linked list
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.insert_new_head(4)
        ll.insert_new_head(5)
        ll.insert_new_head(2)
        self.assertTrue(ll.stringify() == "2-5-4-3-6")
        ll.remove_node_by_index(4)
        self.assertTrue(ll.stringify() == "2-5-4-3")
        self.assertIsNone(ll.get_head().get_link_node().get_link_node().get_link_node().get_link_node())

    def test_remove_first_occurence(self):
        """
        Test if first occurence of a given value is removed from the linked list
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.insert_new_head(4)
        self.assertTrue(ll.stringify() == "4-3-6")
        ll.remove_first_occurence(6)
        self.assertTrue(ll.stringify() == "4-3")
        self.assertIsNone(ll.get_head().get_link_node().get_link_node())

    def test_remove_first_occurence_is_head(self):
        """
        Test if first occurence of a given value is correctly removed
        if its corresponding node is the head of the linked list
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.insert_new_head(4)
        self.assertTrue(ll.stringify() == "4-3-6")
        ll.remove_first_occurence(4)
        self.assertTrue(ll.stringify() == "3-6")
        self.assertTrue(ll.get_head().get_value() == 3)

    def test_remove_first_occurence_is_head_is_only_element(self):
        """
        Test if first occurence of a given value is correctly removed
        if its corresponding node is the head and the only node in the linked
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.remove_first_occurence(6)
        self.assertIsNone(ll.get_head())

    def test_remove_head_only_element(self):
        """
        Test if head node is correctly removed when its the only element in the linked lis
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.remove_head()
        self.assertIsNone(ll.get_head())

    def test_remove_head_multiple_elements(self):
        """
        Test if the head node is correctly removed if there are multiple elements in the list
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.remove_head()
        self.assertTrue(ll.head.get_value() == 6)

    def test_stringify(self):
        """
        Test if the contents of a linked list are correctly returned as a string
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.insert_new_head(3)
        ll.insert_new_head(4)
        self.assertTrue(ll.stringify() == "4-3-6")
        ll.remove_head()
        self.assertTrue(ll.stringify() == "3-6")

    def test_stringify_no_elements(self):
        """
        Test if None is returned when Linked List is empty
        """
        ll = LinkedList()
        ll.insert_new_head(6)
        ll.remove_head()
        self.assertIsNone(ll.stringify())

