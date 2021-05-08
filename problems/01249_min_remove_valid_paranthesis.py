# 1249. Minimum Remove to Make Valid Parentheses
# Medium
#
# 2084
#
# 48
#
# Add to List
#
# Share
# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
# Approach 1: Using a Stack and String Builder
# Intuition
#
# Let's start by looking at what it means for the parentheses of a string to be valid.
#
# The parentheses in a string are balanced if and only if these 2 conditions are met:
#
# There are the same number of "(" and ")" in the string.
# Scanning through the string from left to right and counting how many "(" and ")" there are so far, there should never be a time where there are more ")" than "(". We call count("(") - count(")") the balance of the string..
# Here's a simple pseudocode algorithm that checks for these conditions by scanning through the string and incrementing balance each time it sees a "(", and decrementing each time it sees ")". If at any point the balance is negative, which can only happen if we've seen more ")" than "(", then it returns false. If we get to the end, then it returns true only if the balance is 0, which means we've seen the same number of "(" as ")".
#
# function is_balanced_parentheses(string)
# balance = 0
# for each char in the string
# if char == "("
#     balance = balance + 1
# if char == ")"
#     balance = balance - 1
# if balance < 0
#     return false
# return balance == 0
# For example, "L(ee)(t(()co)d)e" is a balanced string. We'll use a table to show how the balance changes at each point in the string.
#
# A diagram showing that L(ee)(t(()co)d)e is a balanced string.
#
# The string "L(e)e(t)c)o)(d)e" is invalid because the balance goes negative.
#
# A diagram showing that L(e)e(t)c)o)(d)e is an unbalanced string.
#
#     And the string "L(e)e(t()c(o(d)e" is invalid because the balance is not 0 at the end.
#
#     A diagram showing that L(e)e(t()c(o(d)e is an unbalanced string.
#
# The question asks us to remove the minimum number of parentheses to make the string valid. So, how can we use the tricks above to achieve this? For starters, we know we'll need to remove any ")" that we encountered when balance was already 0. It would be impossible to remove less ")", because there are not enough "(" before them.
#
# Taking the 2nd example from above, here's what we get when we delete ")" that would have made the balance go negative.
#
# A diagram showing the balancing of L(e)e(t)c)o)(d)e.
#
#     Because we now finish with a zero balance, we know the string is valid.
#
# However, this isn't the full solution. Take a look at this example where we have removed any ")" from "L(e)))et((co)d(e" that would have caused a negative balance, but we still end with a non-zero balance.
#
# A diagram showing an attempt to balance L(e)))et((co)d(e
#
# A non-zero balance at the end occurs when there were "(" that were not closed with a ")". Clearly, we'll need to remove some "(" to reduce the balance at the end down to 0. But which should we remove? What will happen if we choose 2 random ones?
#
# Here is the string from above. The 2 "(" we have randomly chosen to remove have been crossed out (along with the 2 ")" from before) and we've checked the balance of the new string.
#
# A diagram showing a failed attempt to balance L(e)))et((co)d(e by removing invalid ) and then random (
#
# We've caused the balance to go negative while checking again. Even though we have the same number of "(" and ")" in the string, they don't match up. The last ")" is before the last "(". We don't want to do another round of removing ")", because that would no longer be optimal. We need to identify which "(" each of our ")" is actually pairing with. Here is the example with a different color to show each pair. A ")" always pairs with the closest "(" that doesn't already have a pair.
#
# A diagram using color to show pairs in L(e)))et((co)d(e
#
# The 2 "(" that don't pair with a ")" are the ones we should remove. This way, we know we won't cause a negative balance.
#
# So, remembering that each ")" was paired with the closest "(" that isn't already paired, how could we do this in code? We need to know the indexes of the problematic "(".
#
# We can use a stack. Each time we see a "(", we should add its index to the stack. Each time we see a ")", we should remove an index from the stack because the ")" will match with whatever "(" was at the top of the stack. The length of the stack is equivalent to the balance from above. We will need to do the:
#
#     Remove a ")" if it is encountered when stack was already empty (prevent negative balance).
# Remove a "(" if it is left on stack at end (prevent non-zero final balance).
# Here is an animation of using a stack to fix the string from above.
#     Algorithm
#
#     Let's put all this together into a 2-pass algorithm.
#
# Identify all indexes that should be removed.
#     Build a new string with removed indexes.
# As explained above, we should use a stack. If we put the indexes of the "(" on the stack, then we'll know that all the indexes on the stack at the end are the indexes of the unmatched "(". We should also use a set to keep track of the unmatched ")" we come across. Then, we can remove the character at each of those indexes and then return the edited string.
#
# We need to be really careful with that "removal" step though, as it can be done in O(n)O(n), but there are many ways of accidentally making it O(n^2)O(n
# 2
# ). Making these mistakes (and not fixing them) in an interview won't look good. Here's some operations that are O(n)O(n) that people sometimes assume are O(1)O(1).
#
# Adding or removing (or even changing) just one character anywhere in a string is O(n)O(n), because strings are immutable. The entire string is rebuilt for every change.
# Adding or removing not from the end of a list, vector, or array is O(n)O(n) because the other items are moved up to make a gap or down to fill in the gap.
# Checking if an item is in a list, because this requires a linear search. Even if you use binary search, it'll still be O(\log n)O(logn), which is not ideal for this problem.
# A safe strategy is to iterate over the string and insert each character we want to keep into a list (Python) or StringBuilder (Java). Then once we have all the characters, it is a single O(n)O(n) step to convert them into a string.
#
# Recall that checking if an item is in a set is O(1)O(1). If all the indexes we need to remove are in a set, then we can iterate through each index in the string, check if the current index is in the set, and if it is not, then add the character at that index to the string builder.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        extra_starting_paranthesis = []
        extra_ending_paranthesis = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                extra_starting_paranthesis.append(i)
            elif not extra_starting_paranthesis:
                extra_ending_paranthesis.append(i)
            else:
                extra_starting_paranthesis.pop()

        valid = []
        for i, c in enumerate(s):
            if i not in extra_starting_paranthesis and i not in extra_ending_paranthesis:
                valid.append(c)

        return "".join(valid)