# 460. LFU Cache
# Hard
#
# 2062
#
# 154
#
# Add to List
#
# Share
# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#
# Implement the LFUCache class:
#
# LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present.
# When the cache reaches its capacity, it should invalidate and remove the least frequently used key before
# inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency),
# the least recently used key would be invalidated.
# To determine the least frequently used key, a use counter is maintained for each key in the cache.
# The key with the smallest use counter is the least frequently used key.
#
# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation).
# The use counter for a key in the cache is incremented either a get or put operation is called on it.
#
#
#
# Example 1:
#
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# Explanation
# // cnt(x) = the use counter for key x
#     // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
# // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
# // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
# // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
# // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
# // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
# // cache=[3,4], cnt(4)=2, cnt(3)=3
#
#
# Constraints:
#
# 0 <= capacity, key, value <= 104
# At most 105 calls will be made to get and put.
#
#
# Follow up: Could you do both operations in O(1) time complexity?
from collections import defaultdict


class Node:
    def __init__(self, val, key, freq):
        self.val = val
        self.key = key
        self.freq = freq
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = Node(0, 0, 0)
        self.tail = Node(0, 0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def append(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        self.size += 1

    def pop(self):
        if self.size:
            node = self.tail.prev
            node.prev.next = self.tail
            self.tail.prev = node.prev
            self.size -= 1
            return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.lists = defaultdict(DLinkedList)
        self.min_freq = 0

    def _get(self, key: int) -> Node:
        # Remove the node from its current list and add to the next
        node = self.cache[key]
        old_freq = node.freq
        self.lists[node.freq].remove(node)
        node.freq += 1
        self.lists[node.freq].append(node)

        # Update the minimum frequency to next
        if old_freq == self.min_freq and self.lists[old_freq].size == 0:
            self.min_freq += 1

        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        return self._get(key).val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.cache:
            node = Node(value, key, 1)
            self.cache[key] = node
            self.lists[node.freq].append(node)
            if self.size < self.capacity:
                self.size += 1
            else:
                popped_node = self.lists[self.min_freq].pop()
                del self.cache[popped_node.key]

            self.min_freq = 1
        else:
            node = self._get(key)
            node.val = value
