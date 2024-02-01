# Time Complexity: For an undirected graph, O(N) + O(2E), For a directed graph, O(N) + O(E), Because for every node we are calling the recursive function once, the time taken is O(N) and 2E is for total degrees as we traverse for all adjacent nodes.

# Space Complexity: O(3N) ~ O(N), Space for dfs stack space, visited array and an adjacency list.
def dfsOfGraph(V, adj):
    def dfs(node, vis, ls):
        vis[node] = 1
        ls.append(node)
        for neighbor in adj[node]:
            if not vis[neighbor]:
                dfs(neighbor, vis, ls)

    vis = [0] * V  # Initialize visited array
    start = 0  # Starting node for DFS
    ls = []  # List to store DFS traversal result
    dfs(start, vis, ls)  # Call DFS function
    return ls  # Return DFS traversal result

def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def printAns(ans):
    print(" ".join(map(str, ans)))  # Print the DFS result with spaces

if __name__ == "__main__":
    adj = [[] for _ in range(5)]

    # Add edges to the graph
    addEdge(adj, 0, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 3)

    ans = dfsOfGraph(5, adj)
    printAns(ans)
