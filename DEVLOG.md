# Development Log – The Torchbearer

**Student Name:** Nicholas Porter
**Student ID:** 121284225

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/9]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

The first thing I plan to implement is the run_dijkstra() function, since everything will build on top of this.  I think the most difficult parts are going to be the backtracking and pruning portions, making sure every possible order of relics are checked and the undoing changes to the path.  I plan on testing using the provided tests as well as creating unit tests for each function and any other edge cases I can think of along the way.

---

## Entry 2 – 5/13: Completed Parts 1-4

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

I completed parts 1 through 4, the README as well as their respective functions in torchbearer.py. I also wrote a few simple unit tests so that I could make sure these functions work before proceeding with the next parts.  I ran into a bug because I tried to use the distance dictionary before initializing it.  This was easy to resolve by initializing it first and then filling in the distances for each node.

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
