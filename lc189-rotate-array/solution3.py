from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    # reverse all
    for i in range(0, n // 2):
        temp = nums[i]
        nums[i] = nums[n - 1 - i]
        nums[n - 1 - i] = temp
    # reverse part 1
    for i in range(0, k // 2):
        temp = nums[i]
        nums[i] = nums[k - 1 - i]
        nums[k - 1 - i] = temp
    # reverse part 2
    for i in range(k, (n + k) // 2):
        temp = nums[i]
        nums[i] = nums[n + k - 1 - i]
        nums[n + k - 1 - i] = temp


a = [1, 2, 3, 4, 5, 6, 7]
rotate(a, 3)
print(a)
