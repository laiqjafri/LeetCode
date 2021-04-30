# Matching Pairs Given two strings s and t of length N, find the maximum number of possible matching pairs in strings
# s and t after swapping exactly two characters within s. A swap is switching s[i] and s[j], where s[i] and s[j]
# denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two
# strings are defined as the number of indices for which s[i] and t[i] are equal. Note: This means you must swap two
# characters at different indices. Signature int matchingPairs(String s, String t) Input s and t are strings of
# length N N is between 2 and 1,000,000 Output Return an integer denoting the maximum number of matching pairs
# Example 1 s = "abcd" t = "adcb" output = 4 Explanation: Using 0-based indexing, and with i = 1 and j = 3,
# s[1] and s[3] can be swapped, making it  "adcb". Therefore, the number of matching pairs of s and t will be 4.
# Example 2 s = "mno" t = "mno" output = 1 Explanation: Two indices have to be swapped, regardless of which two it
# is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo",
# which shares only "o" with t.

def matching_pairs(s, t):
    un_matched = set()
    matched = set()

    count = 0
    duplicate = False

    for index in range(len(s)):
        if s[index] == t[index]:
            count += 1
            if s[index] in matched:
                duplicate = True
            matched.add(s[index])
        else:
            un_matched.add((s[index], t[index]))

    if count == len(s):
        return count if duplicate else count - 2

    # abdc ==== abdd
    if count == len(s) - 1:
        if duplicate or list(un_matched)[0][0] in matched or list(un_matched)[0][1] in matched:
            return count
        else:
            return count - 1

    for (sc, tc) in un_matched:
        if (tc, sc) in un_matched:
            return count + 2

    unmatched_s = [sc for (sc, _) in un_matched]
    unmatched_t = [tc for (_, tc) in un_matched]

    for (sc, tc) in un_matched:
        if sc in unmatched_t or tc in unmatched_s:
            return count + 1

    return count


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
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
