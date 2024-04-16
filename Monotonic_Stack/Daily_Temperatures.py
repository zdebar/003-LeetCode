# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[
# i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day
# for which this is possible, keep answer[i] == 0 instead.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []
        answer = [0] * n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer