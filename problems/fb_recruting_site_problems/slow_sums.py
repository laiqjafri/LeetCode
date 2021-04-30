# Slow Sums Suppose we have a list of N numbers, and repeat the following operation until we're left with only a
# single number: Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each
# operation equal to the value of the new number, and call the penalty for the entire list as the sum of the
# penalties of each operation. For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first
# operation, which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is
# to find the worst possible penalty for a given input. Signature: int getTotalTime(int[] arr) Input: An array arr
# containing N integers, denoting the numbers in the list. Output format: An int representing the worst possible
# total penalty. Constraints: 1 ≤ N ≤ 10^6 1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array. The
# sum of values of N over all test cases will not exceed 5 * 10^6. Example arr = [4, 2, 1, 3] output = 26 First,
# add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1] Add 7 + 2 for a penalty of 9. Now the array is [9,
# 1] Add 9 + 1 for a penalty of 10. The penalties sum to 26.

def _recurse(arr, penalty=0):
    if len(arr) <= 1:
        return penalty

    new_penalty = arr[0] + arr[1]
    return _recurse([new_penalty] + arr[2:], penalty + new_penalty)


def get_total_time(arr):
    arr.sort(reverse=True)
    return _recurse(arr)


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
    arr_1 = [4, 2, 1, 3]
    expected_1 = 26
    output_1 = get_total_time(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 3, 9, 8, 4]
    expected_2 = 88
    output_2 = get_total_time(arr_2)
    check(expected_2, output_2)
