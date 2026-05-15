# Development Log – The Torchbearer

**Student Name:** Nicholas Porter
**Student ID:** 121284225

---

## Entry 1 – 5/9: Initial Plan

The first thing I plan to implement is the run_dijkstra() function, since everything will build on top of this.  I think the most difficult parts are going to be the backtracking and pruning portions, making sure every possible order of relics are checked and the undoing changes to the path.  I plan on testing using the provided tests as well as creating unit tests for each function and any other edge cases I can think of along the way.

---

## Entry 2 – 5/13: Completed Parts 1-4

I completed parts 1 through 4, the README as well as their respective functions in torchbearer.py. I also wrote a few simple unit tests so that I could make sure these functions work before proceeding with the next parts.  I ran into a bug because I tried to use the distance dictionary before initializing it.  This was easy to resolve by initializing it first and then filling in the distances for each node.

---

## Entry 3 – 5/14: Completed Parts 5 and 6

I completed parts 5 and 6, the README as well as their respective functions in torchbearer.py.  All tests passed.  A bug I ran into was setting the best order to the current relics visited order which was being modified.  This was fixed by setting the best order to a copy of relics visited order when a better path was found.

---

## Entry 4 – 5/14: Post-Implementation Reflection

After I completed implementation, I ran all of the provided tests, but if given more time I would add more test cases and spend more time thinking of edge cases.  In terms of things that could have been improved, there may be a better method of pruning that would allow the algorithm to skip more branches.

---

## Final Entry – 5/14: Time Estimate

| Part                           | Estimated Hours |
| ------------------------------ | --------------- |
| Part 1: Problem Analysis       | 0.5             |
| Part 2: Precomputation Design  | 0.5             |
| Part 3: Algorithm Correctness  | 1               |
| Part 4: Search Design          | 1               |
| Part 5: State and Search Space | 1               |
| Part 6: Pruning                | 1               |
| Part 7: Implementation         | 3               |
| README and DEVLOG writing      | 2               |
| **Total**                      | 10              |
