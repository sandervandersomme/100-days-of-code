from Node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_item: Node = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.is_full():
            raise Exception("Stack overflow")
        self.top_item = Node(value, self.top_item)
        self.size += 1

    def peek(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        return self.top_item.get_value()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack underflow")
        item = self.top_item
        self.top_item = item.get_link_node()
        self.size -= 1
        return item.get_value()

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.limit


if __name__ == '__main__':
    st = Stack()
    st.push(2)
    st.peek()
