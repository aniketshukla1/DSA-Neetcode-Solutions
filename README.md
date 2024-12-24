# Neetcode.io Solutions in Python

This repository contains **Python solutions** for all problems covered on [Neetcode.io](https://neetcode.io), organized for easy reference and learning. Each solution is written with clarity and includes comments explaining the approach, time complexity, and space complexity.

**More language support (e.g., Java, C++, JavaScript, Golang) will be added soon**, making this repository a one-stop solution for Neetcode.io problems in multiple languages.

## 🌟 Features
- **Comprehensive Coverage**: Solutions for all Neetcode.io problem categories.
- **Well-Commented Code**: Every solution includes a detailed explanation of the approach.
- **Optimized Algorithms**: Focus on clean, efficient, and scalable solutions.
- **Future Expansion**: Planned support for solutions in other languages like Java, C++, and JavaScript.

## 📂 Directory Structure
The repository is organized into folders based on problem categories:

- 📦 **Neetcode.io Solutions**
  - **Arrays & Hashing**
  - **Two Pointers**
  - **Sliding Window**
  - **Stack**
  - **Binary Search**
  - **Linked List**
  - **Trees**
  - **Heap / Priority Queue**
  - **Backtracking**
  - **Tries**
  - **Graphs**
  - **Advanced Graphs**
  - **1-D Dynamic Programming**
  - **2-D Dynamic Programming**
  - **Greedy**
  - **Intervals**
  - **Math & Geometry**
  - **Bit Manipulation**


Each problem is organized into its own folder within the relevant category, making finding and reviewing solutions easy.

## 🛠 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/neetcode-python-solutions.git
   ```
2.	Navigate to the category and problem folder you’re interested in:
     ```bash
     cd Arrays/Contains Duplicate/
     ```
3.  Open the Solution.py file to view the solution:
     ```bash
     cat Solution.py
     ```

📖 Solution Format

Each solution file follows a consistent format:
	•	Problem Name: Title of the problem.
	•	Problem Description: A short summary of the problem.
	•	Approach: Explanation of the solution approach.
	•	Complexity: Analysis of time and space complexity.
	•	Code: Optimized Python solution.

🧩 Example

File: Solution.py

```python
# Problem: Contains Duplicate
# Description: Check if a list contains any duplicates.
# Approach:
# 1. Use a set to track unique elements (O(1) for lookup/insertion).
# 2. Iterate through the list:
#    - If an element exists in the set, return True (duplicate found).
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
```

🚀 Contributions

Contributions are welcome! If you’d like to add solutions in other languages or optimize existing ones:
	1.	Fork the repository.
	2.	Add your solutions.
	3.	Submit a pull request.

📚 References
	•	[Neetcode.io](https://neetcode.io)
	•	[LeetCode](https://leetcode.com)

📜 License

This repository is licensed under the MIT License. You may use the code for your personal learning and projects.
