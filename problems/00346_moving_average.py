# 346. Moving Average from Data Stream
# Easy
#
# 848
#
# 84
#
# Add to List
#
# Share
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
#
#
# Example 1:
#
# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]
#
# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = []
        self.size = size
        self.pointer = 0

    def next(self, val: int) -> float:
        if self.pointer < self.size:
            self.window.append(val)
            self.pointer += 1
        else:
            self.window[self.pointer % self.size] = val
            self.pointer += 1

        return sum(self.window) / (self.pointer if self.pointer < self.size else self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
