#! /usr/bin/env python


class hash_table(object):
    """Hash Table Data Strucure: Generic Hash algorith"""

    def __init__(self, size):
        self.size = size
        self.table = [[] for x in xrange(self.size)]

    def insert(self, key, value):
        """Insert a key value pair into the hash table"""
        hashed = self.hash_value(key)
        check_keys = []
        for x in self.table[hashed]:
            check_keys.append(x[0])
        if key not in check_keys:
            self.table[hashed].append((key, value))
        else:
            print "Can't duplicate key value submittal"

    def hash_value(self, key):
        """Simple Hash using character values"""
        holder = 0
        for char in key:
            holder += ord(char) ** 2
        return holder % self.size

    def get(self, key):
        hashed = self.hash_value(key)
        if self.table[hashed]:
            for x in self.table[hashed]:
                if x[0] == key:
                    return x[1]
                else:
                    return 'Key Value does not exisit'
        return False


if __name__ == '__main__':
    test_hash = hash_table(100)
    test_hash.insert('hi', 'value_hi')
    print test_hash.get('hi')
    test_hash.insert('hi', 'value_2_hi')
    print test_hash.get('hi')
    print test_hash.table[41]

