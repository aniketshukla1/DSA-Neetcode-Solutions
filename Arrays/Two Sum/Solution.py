from collections import defaultdict
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(int)
        for idx in range(len(nums)):
            if target - nums[idx] in nums_dict:
                return [idx, nums_dict[target - nums[idx]]]
            nums_dict[nums[idx]] = idx
        return []