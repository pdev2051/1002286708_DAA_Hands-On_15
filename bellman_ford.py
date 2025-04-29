import math

def bellman_ford(graph, source):
    """
    Implements the Bellman-Ford algorithm to find the shortest paths from a single
    source vertex to all other vertices in a weighted directed graph.

    Args:
        graph: A dictionary representing the graph where keys are vertices and
               values are lists of tuples representing edges. Each tuple is of
               the form (neighbor, weight).
        source: The starting vertex.

    Returns:
        A tuple containing:
            - distances: A dictionary storing the shortest distance from the
                         source to each vertex.
            - predecessors: A dictionary storing the predecessor of each vertex
                            in the shortest path from the source.
            - has_negative_cycle: A boolean indicating whether the graph contains
                                  a negative cycle reachable from the source.
    """
    distances = {vertex: math.inf for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[source] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] != math.inf and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] != math.inf and distances[u] + weight < distances[v]:
                return distances, predecessors, True  # Negative cycle detected

    return distances, predecessors, False

if __name__ == '__main__':
    graph = {
        'A': [('B', -1), ('C', 4)],
        'B': [('C', 3), ('D', 2), ('E', 2)],
        'C': [],
        'D': [('B', 1), ('C', 5)],
        'E': [('D', -3)]
    }

    source_node = 'A'
    distances, predecessors, has_negative_cycle = bellman_ford(graph, source_node)

    print(f"Shortest distances from source '{source_node}':")
    for vertex, distance in distances.items():
        print(f"To {vertex}: {distance}")

    print("\nPredecessors in the shortest paths:")
    for vertex, predecessor in predecessors.items():
        print(f"Predecessor of {vertex}: {predecessor}")

    if has_negative_cycle:
        print("\nWarning: The graph contains a negative cycle reachable from the source.")
    else:
        print("\nNo negative cycles detected.")

    # Example with a negative cycle
    negative_cycle_graph = {
        'X': [('Y', 2)],
        'Y': [('Z', -4)],
        'Z': [('X', 1)]
    }

    source_negative = 'X'
    distances_neg, predecessors_neg, has_negative_cycle_neg = bellman_ford(negative_cycle_graph, source_negative)

    print(f"\nShortest distances from source '{source_negative}' in graph with negative cycle:")
    for vertex, distance in distances_neg.items():
        print(f"To {vertex}: {distance}")

    if has_negative_cycle_neg:
        print("\nWarning: The graph contains a negative cycle reachable from the source.")
    else:
        print("\nNo negative cycles detected.")