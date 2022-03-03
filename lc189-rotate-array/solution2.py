from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    nums[:] = nums[n - k::] + nums[0: n - k]


a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)

