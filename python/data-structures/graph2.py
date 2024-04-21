from collections import defaultdict, deque

class Graph:
    def __init__(self):
        """
        Initializes the graph.
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Adds an edge to the graph.
        """
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        """
        Utility function for DFS traversal.
        """
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, v):
        """
        Performs Depth-First Search (DFS) traversal starting from vertex v.
        """
        visited = [False] * len(self.graph)
        self.dfs_util(v, visited)
        print()

    def bfs(self, v):
        """
        Performs Breadth-First Search (BFS) traversal starting from vertex v.
        """
        visited = [False] * len(self.graph)
        queue = deque()
        queue.append(v)
        visited[v] = True

        while queue:
            v = queue.popleft()
            print(v, end=' ')

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()

def main():
    """
    Main entry point.
    """
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print("Depth-First Traversal (DFS) starting from vertex 2:")
    graph.dfs(2)

    print("Breadth-First Traversal (BFS) starting from vertex 2:")
    graph.bfs(2)

if __name__ == "__main__":
    main()
