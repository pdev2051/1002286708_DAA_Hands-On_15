import heapq
from typing import Dict, List, Tuple, Any

def dijkstra(
    graph: Dict[Any, List[Tuple[Any, float]]],
    source: Any
) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
    """
    Compute shortest paths from `source` to all other nodes in `graph`.

    Parameters
    ----------
    graph : dict
        Adjacency list representation of the graph where
        graph[u] = [(v, w_uv), ...] indicates an edge u->v of weight w_uv.
    source : hashable
        The starting node.

    Returns
    -------
    dist : dict
        dist[v] is the length of the shortest path from source to v.
    prev : dict
        prev[v] is the predecessor of v along the shortest path from source.
    """
    # Initialize distances and predecessor map
    dist: Dict[Any, float] = {node: float('inf') for node in graph}
    prev: Dict[Any, Any] = {node: None for node in graph}
    dist[source] = 0

    # Min-heap of (distance_so_far, node)
    heap: List[Tuple[float, Any]] = [(0, source)]

    while heap:
        d_u, u = heapq.heappop(heap)
        # If we pop a stale entry, skip it
        if d_u > dist[u]:
            continue

        # Relax all outgoing edges (u → v)
        for v, weight in graph[u]:
            alt = d_u + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    return dist, prev

def reconstruct_path(
    prev: Dict[Any, Any],
    source: Any,
    target: Any
) -> List[Any]:
    """
    Reconstruct the shortest path from source to target
    using the predecessor map returned by dijkstra().

    Returns a list of nodes [source, ..., target].
    If target is unreachable, returns an empty list.
    """
    path: List[Any] = []
    at = target
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()
    if path[0] == source:
        return path
    else:
        return []  # target not reachable

# Example usage
if __name__ == "__main__":
    # Define a sample graph
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
        'E': [('C', 8), ('D', 3)],
        'F': [('D', 6)]
    }

    source = 'A'
    dist, prev = dijkstra(graph, source)

    print("Shortest distances from", source)
    for node in sorted(dist):
        print(f"  {source} → {node}: {dist[node]}")

    # Reconstruct path from A to F
    path_A_to_F = reconstruct_path(prev, source, 'F')
    print("\nShortest path A → F:", " → ".join(path_A_to_F))
