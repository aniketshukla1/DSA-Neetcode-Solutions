# Approach:
# 1. Use a set to track unique elements (O(1) for lookup/insertion).
# 2. Iterate through the list:
#    - If element exists in the set, return True (duplicate found).
#    - Otherwise, add the element to the set.
# 3. If no duplicates are found after iteration, return False.

# Time Complexity: O(n), Space Complexity: O(n).

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False