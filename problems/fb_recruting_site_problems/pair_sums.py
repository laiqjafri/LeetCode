# Pair Sums Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it
# which sum to k. If an integer appears in the list multiple times, each copy is considered to be different; that is,
# two pairs are considered different if one pair includes at least one array index which the other doesn't,
# even if they include the same values. Signature int numberOfWays(int[] arr, int k) Input n is in the range [1, 100,
# 000]. Each value arr[i] is in the range [1, 1,000,000,000]. k is in the range [1, 1,000,000,000]. Output Return the
# number of different pairs of elements which sum to k. Example 1 n = 5 k = 6 arr = [1, 2, 3, 4, 3] output = 2 The
# valid pairs are 2+4 and 3+3. Example 2 n = 5 k = 6 arr = [1, 5, 3, 3, 3] output = 4 There's one valid pair 1+5,
# and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).

# Add any extra import statements you may need here

# Add any helper functions you may need here


def number_of_ways(arr, k):
    # Write your code here
    count_map = {}
    count = 0
    for v in arr:
        if count_map.get(v) is not None:
            count_map[v] = count_map[v] + 1
        else:
            count_map[v] = 1

    for v in count_map:
        diff = k - v
        if count_map.get(diff) is not None:
            if v == diff:
                if count_map[v] > 1:
                    count += (count_map[v] * (count_map[v] - 1))
            else:
                count += count_map[diff]

    return count // 2


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def print_integer(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    right_tick = '\u2713'
    wrong_tick = '\u2717'
    if result:
        print(right_tick, 'Test #', test_case_number, sep='')
    else:
        print(wrong_tick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        print_integer(expected)
        print(' Your output: ', end='')
        print_integer(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = number_of_ways(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = number_of_ways(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
