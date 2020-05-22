# for https://leetcode.com/problems/fizz-buzz/
# I don't know if this is cheating? It seems super easy idk

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuzzList = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                fizzBuzzList.append('FizzBuzz')
            elif num % 3 == 0:
                fizzBuzzList.append('Fizz')
            elif num % 5 == 0:
                fizzBuzzList.append('Buzz')
            else:
                fizzBuzzList.append(str(num))
        return fizzBuzzList
