"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Nicholas Porter
Student ID: 121284225

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return """
- Why a single shortest-path run from S is not enough:
  If you run Dijkstra's from the start node, it will find the shortest path to every other node, but that does not guarantee you will go through every relic along that path.

- What decision remains after all inter-location costs are known:
  The decision that remains is in which order to visit each of the relics.

- Why this requires a search over orders:
  Search over orders is required, because you have to go through all of the possible combinations to find the optimal path."""


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = []
    sources.append(spawn)
    for relic in relics:
        if relic not in sources:
            sources.append(relic)
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    dist = {}
    for node in graph:
        dist[node] = float('inf')
    
    dist[source] = 0


    priority_queue = []
    heapq.heappush(priority_queue, (0, source))

    while priority_queue:
        curr_dist, u = heapq.heappop(priority_queue)

        if curr_dist > dist[u]:
            continue
        
        for v, cost in graph[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(priority_queue, (dist[u] + cost, v))

    return dist

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    dist_table = {}
    
    sources = select_sources(spawn, relics, exit_node)
    for source in sources:
        dist = run_dijkstra(graph, source)
        dist_table[source] = dist

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """
- For nodes already finalized (in S):
  There are no shorter paths possible from S to that node 

- For nodes not yet finalized (not in S):
  The distance stored is the shortest path currently found from the S to that node

- Initialization : why the invariant holds before iteration 1:
  S starts with a distance of 0, and all other nodes start with a distance of inf
  The path from the source to itself will always be 0, and no paths to other nodes have been discovered yet

- Maintenance : why finalizing the min-dist node is always correct:
  Since all edge weights are nonnegative every path to the min-dist node would have to add more fuel cost so there will never be a shorter path discovered 

- Termination : what the invariant guarantees when the algorithm ends:
  Once Dijkstra finishes every distance stored is the shortest path from the start to its respective node


The route planner needs the shortest path to each relic so that it can compare the different orders of relics to find the minimum fuel cost."""


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """
Why Greedy Fails
- The failure mode: Greedy fails because it always chooses the next relic with the lowest cost, but that choice can lead to a worse complete path
- Counter-example setup: 

| From \ To | A   | B   | C   | T   |
| --------- | --- | --- | --- | --- |
| S         | 1   | 100 | 2   | --  |
| A         | --  | 100 | 100 | 1   |
| B         | 10  | --  | 5   | 1   |
| C         | 1   | 3   | --  | 100 |

- What greedy picks: S -> A -> B -> C -> T
- What optimal picks: S -> C -> B -> A -> T
- Why greedy loses: 
	- At the first step greedy chooses to go to A, because it is the lowest fuel cost from S
	- From A, B and C still need to be visited, but both have a very high cost from A
	- It would be optimal to go from S to C instead even though S to C is higher than S to A, because the costs from C to B and B to A are much lower

What the Algorithm Must Explore
- The algorithm needs to explore every order to visit each relic in order to find the optimal route."""


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


def _run_unit_tests():
    print("Running Unit tests...")

    # Test 1: select_sources should include S and relics, but not T.
    sources = select_sources('S', ['A', 'B'], 'T')

    if 'S' in sources and 'A' in sources and 'B' in sources and 'T' not in sources:
        print("Test 1 passed")
    else:
        print("Test 1 failed")
        print("sources =", sources)

    # Test 2: select_sources should not add duplicates.
    sources = select_sources('S', ['A', 'S', 'A'], 'T')

    if len(sources) == 2:
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        print("sources =", sources)

    # Test 3: Dijkstra should find the cheaper path through A.
    graph = {
        'S': [('A', 1), ('B', 5)],
        'A': [('B', 2)],
        'B': []
    }

    dist = run_dijkstra(graph, 'S')

    if dist['S'] == 0 and dist['A'] == 1 and dist['B'] == 3:
        print("Test 3 passed")
    else:
        print("Test 3 failed")
        print("dist =", dist)

    # Test 4: unreachable nodes should stay infinity.
    graph = {
        'S': [('A', 2)],
        'A': [],
        'B': []
    }

    dist = run_dijkstra(graph, 'S')

    if dist['B'] == float('inf'):
        print("Test 4 passed")
    else:
        print("Test 4 failed")
        print("dist =", dist)

    # Test 5: precompute_distances should make a table for S and each relic.
    graph = {
        'S': [('A', 1)],
        'A': [('B', 2)],
        'B': [('T', 3)],
        'T': []
    }

    dist_table = precompute_distances(graph, 'S', ['A', 'B'], 'T')

    if 'S' in dist_table and 'A' in dist_table and 'B' in dist_table and 'T' not in dist_table:
        print("Test 5 passed")
    else:
        print("Test 5 failed")
        print("dist_table =", dist_table)

    # Test 6: precompute_distances should store correct shortest path values.
    if dist_table['S']['T'] == 6 and dist_table['A']['T'] == 5 and dist_table['B']['T'] == 3:
        print("Test 6 passed")
    else:
        print("Test 6 failed")
        print("dist_table =", dist_table)

if __name__ == "__main__":
    #_run_tests()
    _run_unit_tests()
    print(explain_problem())
    print(dijkstra_invariant_check())
    print(explain_search())
