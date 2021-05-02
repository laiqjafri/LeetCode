# 252. Meeting Rooms
# Easy
#
# 918
#
# 50
#
# Add to List
#
# Share
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
#
#
#
# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: true
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda interval: interval[0])
        return all(intervals[i][1] <= intervals[i+1][0] for i in range(len(intervals) - 1))
