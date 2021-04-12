from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_new_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def remove_node_by_index(self, position):
        current_node = self.get_head()
        prev = None
        for index in range(0, position):
            if current_node.get_link_node() is not None:
                prev = current_node
                current_node = current_node.get_link_node()
            else:
                raise Exception("The LinkedList does not contain a Node on that position")
        if current_node.get_link_node() is not None:
            prev.set_link_node(current_node.get_link_node())
        else:
            prev.set_link_node(None)

    def remove_first_occurence(self, value_to_remove):
        current_node = self.get_head()
        if current_node.get_value() == value_to_remove:
            self.head = current_node.get_link_node()
        else:
            while current_node:
                next_node = current_node.get_link_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_link_node(next_node.get_link_node())
                    current_node = None
                else:
                    current_node = next_node

    def remove_head(self):
        if self.get_head().get_link_node() is not None:
            self.head = self.get_head().get_link_node()
        else:
            self.head = None
            # raise Exception("Head is the only element in the linked list")

    def stringify(self):
        current_node = self.get_head()
        if self.head is None:
            return None
        string = str(self.head.get_value())
        while current_node.get_link_node() is not None:
            current_node = current_node.get_link_node()
            string += '-' + str(current_node.get_value())
        return string
