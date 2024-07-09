def longest_path(graph: list) -> int:
    # Perform topological sort on the graph
    topo_order = topological_sort(graph)
    # Calculate the longest path using the topological order
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    from collections import deque
    
    # Calculate in-degrees of all nodes
    indegree = [0] * len(graph)
    for u in range(len(graph)):
        for v, _ in graph[u]:
            indegree[v] += 1
    
    # Initialize the queue with nodes having in-degree of 0
    queue = deque([i for i in range(len(graph)) if indegree[i] == 0])
    topo_order = []
    
    # Process nodes in the queue
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return topo_order

def calculate_longest_path(graph, topo_order):
    # Initialize distances with negative infinity
    dist = [-float('inf')] * len(graph)
    
    # Set the distance to 0 for all nodes in the topological order
    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0
    
    # Update distances based on the topological order
    for node in topo_order:
        for neighbor, weight in graph[node]:
            if dist[neighbor] < dist[node] + weight:
                dist[neighbor] = dist[node] + weight
    
    # The longest path length is the maximum value in the distance array
    return max(dist)

# Example usage
#     graph = [
#         [(1, 3), (2, 2)],
#         [(3, 4)],
#         [(3, 1)],
#         []
#     ]
#     print(longest_path(graph))  # Output: 7