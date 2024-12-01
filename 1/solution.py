from heapq import *
import fileinput
from collections import Counter

class Day1():
    def __init__(self):
        self.l1 = []
        self.l2 = []
        with fileinput.input(files=('input.txt')) as f:
            for line in f:
                num1, num2 = [int(num) for num in line.split('   ')]
                self.l1.append(num1)
                self.l2.append(num2)

    def solution1(self):
        l1Sorted = sorted(self.l1)
        l2Sorted = sorted(self.l2)
        ans = 0
        for i in range(len(l1Sorted)):
            ans += abs(l1Sorted[i] - l2Sorted[i])
        return ans

    def solution2(self):
        l2Counter = Counter(self.l2)
        ans = 0
        for num1 in self.l1:
            ans += num1 * l2Counter[num1]
        return ans

d1 = Day1()
print(d1.solution1())
print(d1.solution2())