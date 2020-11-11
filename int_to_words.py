# for https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Converts a non-negative integer num to its English word equivalent.

        Example: num = 123
        Output: 'One Hundred Twenty Three'

        Takes a single non-negative integer, num, and returns a string.
        """
        if num == 0:
            return 'Zero'
        digits = [
            '',  # blank string in 0 index to improve readability
            'One',  # since now digits[1] == 'One'
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
        # Next two could be part of big list technically but I don't think
        # it makes sense to do so.
        tens = [
            '',  # blank strings in 0 and 1 index for the same reason
            '',
            'Twenty',
            'Thirty',
            'Forty',
            'Fifty',
            'Sixty',
            'Seventy',
            'Eighty',
            'Ninety',
        ]
        scales = [
            '',  # Not for readability per se but so scale can start at 0
            'Thousand',
            'Million',
            'Billion'
        ]
        scale = 0  # increments upward
        results = []  # container for results
        while num > 0:
            current_chunk_words = []   # container for current chunk's words
            # Process the chunk by hundreds, then tens, then ones
            # adding the relevant words to current container
            # First hundreds, using modulo and floor division
            current_chunk = num % 1000  # lop off a three digit chunk
            hundreds_chunk = current_chunk // 100
            if hundreds_chunk > 0:
                current_chunk_words.append(digits[hundreds_chunk])
                current_chunk_words.append('Hundred')  # not worth a list entry
            # Then tens, again using modulo and floor division to separate
            current_chunk = current_chunk % 100
            tens_chunk = current_chunk // 10
            if tens_chunk != 1:  # Everything but the teens
                if tens_chunk:
                    current_chunk_words.append(tens[tens_chunk])
                # Processing ones like hundreds and tens, note that
                # this doesn't happen in the teens case
                ones_chunk = current_chunk % 10
                if ones_chunk:
                    current_chunk_words.append(digits[ones_chunk])
            elif tens_chunk == 1:  # 11-19 are a special case
                current_chunk_words.append(digits[current_chunk])
            # Now add the large_number/million/billion if applicable,
            # turn it into a string, and add it to results
            if current_chunk_words:
                if scale:
                    current_chunk_words.append(scales[scale])
                current_chunk_words = ' '.join(current_chunk_words)
                results.append(current_chunk_words)
            # Now we cut the number down by 1000, up the scale
            # marker and execute again, repeating until empty
            num = num // 1000
            scale += 1
        # This leaves results a list of correct strings for the three-digit
        # chunks of the int, but in reverse order. So assuming the int wasn't 0
        # we reverse results, and return a joined string of it. If the original
        # int was 0 then whoops. That check was originally down here but
        # sanitizing the input earlier was more performant.
        return ' '.join(reversed(results))
