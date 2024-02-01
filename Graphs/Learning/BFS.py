from collections import deque

def bfsOfGraph(V, adj):
    # Initialize visited array
    vis = [0] * V
    vis[0] = 1  # Mark the first node as visited
    q = deque([0])  # Use deque as the queue for BFS
    bfs = []  # List to store BFS traversal result

    while q:
        node = q.popleft()
        bfs.append(node)  # Add the current node to BFS result

        # Traverse neighbors of the current node
        for neighbor in adj[node]:
            if not vis[neighbor]:
                vis[neighbor] = 1  # Mark neighbor as visited
                q.append(neighbor)  # Add neighbor to the queue for further exploration

    return bfs

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def printAns(ans):
    print(" ".join(map(str, ans)))  # Print the BFS result with spaces

if __name__ == "__main__":
    # Create an adjacency list for the graph
    adj = [[] for _ in range(6)]

    # Add edges to the graph
    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

    # Perform BFS and print the result
    ans = bfsOfGraph(5, adj)
    printAns(ans)