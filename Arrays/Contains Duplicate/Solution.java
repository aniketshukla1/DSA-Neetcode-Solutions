// Approach:
// 1. Use a set to track unique elements (O(1) for lookup/insertion).
// 2. Iterate through the list:
//    - If element exists in the set, return True (duplicate found).
//   - Otherwise, add the element to the set.
// 3. If no duplicates are found after iteration, return False.

// Time Complexity: O(n), Space Complexity: O(n).

import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> unique_nums = new HashSet<>();
        for(Integer num:nums) {
            if(unique_nums.contains(num)) {
                return true;
            }
            unique_nums.add(num);
        }

        return false;
    }
}