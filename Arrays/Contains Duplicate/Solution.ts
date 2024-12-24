// Approach:
// 1. Use a set to track unique elements (O(1) for lookup/insertion).
// 2. Iterate through the list:
//    - If element exists in the set, return True (duplicate found).
//   - Otherwise, add the element to the set.
// 3. If no duplicates are found after iteration, return False.

// Time Complexity: O(n), Space Complexity: O(n).

function containsDuplicate(nums: number[]): boolean {
   const unique_nums: Set<number> = new Set<number>();

   for(const num of nums) {
        if (unique_nums.has(num)) {
            return true;
        }
        unique_nums.add(num)
   }

   return false;

};