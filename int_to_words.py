# for https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Converts a non-negative integer num to its English word equivalent.

        Example: num = 123
        Output: 'One Hundred Twenty Three'

        Takes a single non-negative integer, num, and returns a string.
        """
        digits = [
            '',
            'One',
            'Two',
            'Three',
            'Four',
            'Five',
            'Six',
            'Seven',
            'Eight',
            'Nine',
            'Ten',
            'Eleven',
            'Twelve',
            'Thirteen',
            'Fourteen',
            'Fifteen',
            'Sixteen',
            'Seventeen',
            'Eighteen',
            'Nineteen'
        ]
        tens = [
            '',
            '',
            'Twenty',
            'Thirty',
            'Forty',
            'Fifty',
            'Sixty',
            'Seventy',
            'Eighty',
            'Ninety',
            'Hundred'
        ]
        places = [
            '',
            'Thousand',
            'Million',
            'Billion'
        ]
        place = 0
        results = []
        while num > 0:
            current_chunk = num % 1000
            hundreds_chunk = current_chunk // 100
            if hundreds_chunk > 0:
                results.append(digits[hundreds_chunk])
                results.append('Hundred')
            current_chunk = current_chunk % 100
            tens_chunk = current_chunk // 10
            if tens_chunk != 1:
                if tens_chunk:
                    results.append(tens[tens_chunk])
                ones_chunk = current_chunk % 10
                results.append(digits[ones_chunk])
            elif tens_chunk == 1:
                results.append(digits[current_chunk])
            if place:
                results.append(places[place])
            results.append(results)
            num = num // 1000
            place += 1
        if results:
            return results
        else:
            return "Zero"
