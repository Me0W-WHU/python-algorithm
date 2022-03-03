from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    ext = nums + nums
    nums[:] = ext[n - k: 2 * n - k]


a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)
