# 253. Meeting Rooms II
# Medium
#
# 3722
#
# 59
#
# Add to List
#
# Share
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
#
#
#
# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: 1
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[0])

        rooms_required = []

        heapq.heappush(rooms_required, intervals[0][1])

        for i in range(1, len(intervals)):
            if rooms_required[0] <= intervals[i][0]:
                heapq.heappop(rooms_required)

            heapq.heappush(rooms_required, intervals[i][1])

        return len(rooms_required)
