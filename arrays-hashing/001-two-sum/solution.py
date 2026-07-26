"""001. Two Sum

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Exactly one valid answer exists and
the same element may not be used twice.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of the two numbers adding up to `target`.

    Single pass with a hash map from value -> index. For each number we check
    whether its complement (target - num) has already been seen.

    Time:  O(n) - one pass over nums.
    Space: O(n) - the seen map.
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # unreachable given the problem's guarantee


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    print("all tests passed")
