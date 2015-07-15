#! /usr/bin/env python


class linked_list(object):
    """Simple, single linked list data structure"""

    head = None
    size = 0

    def insert(self, node):
        node.pointer = self.head
        self.head = node
        self.size += 1


class node(object):
    """Node container for linked list"""

    def __init__(self, data):
        # Single linked so only one pointer required
        self.pointer = None
        self.data = data


def nth(Node, k):
    if Node is None:
        return 0
    i = nth(Node.pointer, k) + 1
    if i == k:
        print Node.data
    return i


if __name__ == '__main__':
    a = linked_list()
    n1 = node('first')
    a.insert(n1)
    print a.head.data
    print a.size
    n2 = node('second')
    a.insert(n2)
    print a.head.data
    print a.size
    n3 = node('third')
    a.insert(n3)
    n4 = node('forth')
    a.insert(n4)
    print 'testing nth'
    nth(n4, 3)
