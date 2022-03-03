from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    a = [i * i for i in nums]
    a.sort()
    return a


print(sortedSquares([-4, -1, 0, 3, 10]))
