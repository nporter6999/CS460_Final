# The Torchbearer

**Student Name:** Nicholas Porter
**Student ID:** 121284225
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
 If you run Dijkstra's from the start node, it will find the shortest path to every other node, but that does not guarantee you will go through every relic along that path.

- **What decision remains after all inter-location costs are known:**
  The decision that remains is in which order to visit each of the relics.

- **Why this requires a search over orders (one sentence):**
  Search over orders is required, because you have to go through all of the possible combinations to find the optimal path.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| S                | S is the start point for every path                                                               |
| Relic            | All relics must be visited and after visiting a relic you have to go to either another relic or T |

### Part 2b: Distance Storage

| Property                    | Your answer                                                                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Data structure name         | Nested dictionary                                                                                                                              |
| What the keys represent     | Source nodes and destination nodes                                                                                                             |
| What the values represent   | Minimum fuel cost from the source to destination nodes                                                                                         |
| Lookup time complexity      | O(1)                                                                                                                                           |
| Why O(1) lookup is possible | With a dictionary, lookup is constant because instead of having to traverse the data structure, you can go directly to the value using the key |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** k+1
- **Cost per run:** O(mlogn)
- **Total complexity:** O(kmlogn)
- **Justification (one line):** Djikstra is ran once for each relic plus the start, and each run costs O(mlogn) 

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  There are no shorter paths possible from the source to that node 

- **For nodes not yet finalized (not in S):**
  The distance stored is the shortest path currently found from the source to that node

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  Source starts with a distance of 0, and all other nodes start with a distance of inf
- The path from the source to itself will always be 0, and no paths to other nodes have been discovered yet

- **Maintenance : why finalizing the min-dist node is always correct:**
  Since all edge weights are nonnegative every path to the min-dist node would have to add more fuel cost so there will never be a shorter path discovered 

- **Termination : what the invariant guarantees when the algorithm ends:**
  Once Dijkstra finishes every distance stored is the shortest path from the start to its respective node

### Part 3c: Why This Matters for the Route Planner

The route planner needs the shortest path to each relic so that it can compare the different orders of relics to find the minimum fuel cost.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy fails because it always chooses the next relic with the lowest cost, but that choice can lead to a worse complete path
- **Counter-example setup:** 

| From \ To | A   | B   | C   | T   |
| --------- | --- | --- | --- | --- |
| S         | 1   | 100 | 2   | --  |
| A         | --  | 100 | 100 | 1   |
| B         | 10  | --  | 5   | 1   |
| C         | 1   | 3   | --  | 100 |

- **What greedy picks:** S -> A -> B -> C -> T
- **What optimal picks:** S -> C -> B -> A -> T
- **Why greedy loses:** 
	- At the first step greedy chooses to go to A, because it is the lowest fuel cost from S
	- From A, B and C still need to be visited, but both have a very high cost from A
	- It would be optimal to go from S to C instead even though S to C is higher than S to A, because the costs from C to B and B to A are much lower

### What the Algorithm Must Explore
- The algorithm needs to explore every order to visit each relic in order to find the optimal route

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- https://pythonguides.com/priority-queue-in-python/
- https://www.geeksforgeeks.org/python/python-infinity/
