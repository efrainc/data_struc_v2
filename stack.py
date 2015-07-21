#! /usr/bin/env python


class node(object):
    """Node container for linked list"""

    def __init__(self, data):
        # Single linked so only one pointer required
        self.pointer = None
        self.data = data


class stack(object):
    """Simple Stack Data Structure"""

    def __init__(self):
        self.head = None

    def insert(self, Node):
        Node.pointer = self.head
        self.head = Node

    def remove(self):
        holder = self.head
        self.head = self.head.pointer
        return holder

    def __str__(self):
        return self.head.data


if __name__ == '__main__':
    a = node('first')
    b = node('second')
    c = node('third')
    sta = stack()
    sta.insert(a)
    sta.insert(b)
    sta.insert(c)
    print sta
    sta.remove()
    print sta
    sta.remove()
    print sta
  