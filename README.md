#UChicago Coding Challenge

### Problem

"There are a surprising number of Chicago neighborhoods that don't have any informal K-12 computer science programs. Given a particular neighborhood, it costs a certain amount of dollars to set up a CS program at a local school, and has a potential to impact students.

Given D amount of dollars in funding, write a function to determine how many students you could impact by setting up CS programs in certain neighborhoods.


Input:
int D : Number of dollars in available in funding
arr[] : an array of tuples (cost, impact) where the first value is the cost and the second value is the impact of setting up a CS program in that neighborhood.
Output: The maximal number of students impacted by setting up programs without exceeding our funding amount of D dollars
Bounds: 0 <= len(arr) ; 0 <= cost ; 0 <= impact"

### Solution

To solve the problem, it at first appears that a recursive solution would be the most natural. For each option *Op* and given cost *C*, one would return the *max*(*max arr* from 0 to *Op* given *C*, *max arr* from 0 to *Op* given *C - cost(Op)* plus *impact(Op)*). The main issue with this algorithm is that it checks both the inclusion and exclusion of an option for every path. Therefore, it checks every possible combination resulting in a time complexity of *O(2^len(arr))*

Using memoization, we can prevent double checking certain states. We use the same logic as above, but instead of recursively checking every possible option, we check the previously stored maximal states in a double array where each row represents an option and each column represents a cost. The zeroth row is set to zero because the impact of no options is zero. Since each cell requires a constant calculation, there is a time complexity of *O(len(arr)\*(D + 1))*  and a space complexity of *O((len(arr) + 1)\*(D + 1))*. Asymptotically, this approaches *O(len(arr)\* D)* for both time and space complexity.
