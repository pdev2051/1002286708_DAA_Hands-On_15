def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find shortest paths between all pairs of vertices
    
    Parameters:
    graph (list of lists): Adjacency matrix representation of the graph
                          graph[i][j] is the weight of the edge from vertex i to vertex j
                          Use float('inf') for non-existent edges
    
    Returns:
    distances (list of lists): distances[i][j] is the shortest path distance from vertex i to vertex j
    next_vertex (list of lists): next_vertex[i][j] is the next vertex on the shortest path from i to j
                                Used for path reconstruction
    """
    n = len(graph)  # Number of vertices
    
    # Initialize distances and next_vertex matrices
    distances = [row[:] for row in graph]  # Create a copy of the graph
    next_vertex = [[j if graph[i][j] != float('inf') else None for j in range(n)] for i in range(n)]
    
    # Set diagonal elements to 0
    for i in range(n):
        distances[i][i] = 0
        next_vertex[i][i] = i
    
    # Floyd-Warshall algorithm
    for k in range(n):  # Intermediate vertex
        for i in range(n):  # Source vertex
            for j in range(n):  # Destination vertex
                # If vertex k offers a shorter path from i to j, update the distance and next vertex
                if distances[i][k] != float('inf') and distances[k][j] != float('inf'):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        next_vertex[i][j] = next_vertex[i][k]
    
    # Check for negative cycles
    for i in range(n):
        if distances[i][i] < 0:
            raise ValueError("Graph contains a negative cycle")
    
    return distances, next_vertex

def reconstruct_path(next_vertex, start, end):
    """
    Reconstructs the shortest path from start to end using the next_vertex matrix
    
    Parameters:
    next_vertex (list of lists): The next_vertex matrix from floyd_warshall
    start (int): The starting vertex
    end (int): The ending vertex
    
    Returns:
    path (list): A list of vertices representing the shortest path from start to end
    """
    if next_vertex[start][end] is None:
        return []  # No path exists
    
    path = [start]
    while start != end:
        start = next_vertex[start][end]
        path.append(start)
    
    return path

# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    # inf means there's no direct edge between vertices
    inf = float('inf')
    example_graph = [
        [0, 3, inf, 7],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0]
    ]
    
    print("Original Graph (Adjacency Matrix):")
    for row in example_graph:
        print([x if x != inf else "∞" for x in row])
    
    # Run Floyd-Warshall algorithm
    distances, next_vertex = floyd_warshall(example_graph)
    
    print("\nShortest Distances Matrix:")
    for row in distances:
        print([x if x != inf else "∞" for x in row])
    
    # Reconstruct a specific path
    start_vertex = 0
    end_vertex = 2
    path = reconstruct_path(next_vertex, start_vertex, end_vertex)
    
    print(f"\nShortest path from {start_vertex} to {end_vertex}: {path}")
    print(f"Path distance: {distances[start_vertex][end_vertex]}")