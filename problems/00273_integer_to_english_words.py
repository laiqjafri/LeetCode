# 273. Integer to English Words
# Hard
#
# 1477
#
# 3681
#
# Add to List
#
# Share
# Convert a non-negative integer num to its English words representation.
#
#
#
# Example 1:
#
# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:
#
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:
#
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:
#
# Input: num = 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'

        def units(num):
            return {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }.get(num)

        def tens(num):
            return {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }.get(num)

        def less_than_twenty(num):
            return {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen',
            }.get(num)

        def two(num):
            if num < 10:
                return units(num)
            elif 10 <= num < 20:
                return less_than_twenty(num)
            else:
                ten = num // 10
                rest = num - (ten * 10)
                return tens(ten) + ' ' + units(rest) if rest else tens(ten)

        def three(num):
            hundred = num // 100
            rest = num - (hundred * 100)
            if not hundred:
                return two(num)
            else:
                return units(hundred) + ' Hundred ' + two(rest) if rest else units(hundred) + ' Hundred'

        result = ''
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        if billion:
            result += three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)

        return result
