# 001. Two Sum

**Pattern:** Arrays & Hashing · **Difficulty:** Easy
· [LeetCode](https://leetcode.com/problems/two-sum/)

## Problem

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers such that they add up to `target`.

- Exactly one valid answer exists.
- The same element may not be used twice.
- The answer may be returned in any order.

**Example**

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]        # nums[0] + nums[1] == 9
```

## Approach

Brute force checks every pair in `O(n²)`. Instead, keep a hash map of the
values already seen mapped to their index. For each `num`, its partner is
`target - num`; if that complement is already in the map, we've found the pair
in a single pass.

## Complexity

| | |
| --- | --- |
| Time | `O(n)` |
| Space | `O(n)` |

## Run

```bash
python solution.py
```
