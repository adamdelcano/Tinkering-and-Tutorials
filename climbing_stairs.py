# for https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # this part might be a bit cheaty but oh well
        if n < 4:
            return n
        last_sum = 2
        current_sum = 3
        # actual loop, fibonacci's not just pasta no more ayyy
        for num in range(4, n + 1):
            last_sum, current_sum = current_sum, (current_sum + last_sum)
        return current_sum
