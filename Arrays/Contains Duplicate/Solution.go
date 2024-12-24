package main

// Approach:
// 1. Use a set to track unique elements (O(1) for lookup/insertion).
// 2. Iterate through the list:
//    - If element exists in the set, return True (duplicate found).
//   - Otherwise, add the element to the set.
// 3. If no duplicates are found after iteration, return False.

// Time Complexity: O(n), Space Complexity: O(n).

func containsDuplicate(nums []int) bool {
    unique_nums := make(map[int]int)

    for _, num := range nums {
        if _, exists := unique_nums[num]; exists {
            return true;
        }
        unique_nums[num] = 1
    }

    return false;
}