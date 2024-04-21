class Graph:
    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Adds an undirected edge between two vertices.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            # Adding vertex2 to the adjacency list of vertex1
            self.graph[vertex1].append(vertex2)
            # Adding vertex1 to the adjacency list of vertex2
            self.graph[vertex2].append(vertex1)
        else:
            print("One or both vertices not found in the graph.")

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph.
        """
        if vertex in self.graph:
            # Remove the vertex from the graph
            del self.graph[vertex]
            # Remove any edges containing the vertex
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
        else:
            print("Vertex not found in the graph.")

    def remove_edge(self, vertex1, vertex2):
        """
        Removes an edge between two vertices.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            # Remove vertex2 from the adjacency list of vertex1
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            # Remove vertex1 from the adjacency list of vertex2
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)
        else:
            print("One or both vertices not found in the graph.")

    def print_graph(self):
        """
        Prints the adjacency list representation of the graph.
        """
        for vertex in self.graph:
            # Printing the vertex and its adjacent vertices
            print(vertex, "->", " -> ".join(map(str, self.graph[vertex])))


def main():
    """
    Main entry point.
    """
    graph = Graph()

    # Adding vertices
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)

    # Adding edges
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    # Printing the graph
    print("Graph after adding vertices and edges:")
    graph.print_graph()

    # Removing a vertex
    graph.remove_vertex(2)

    # Removing an edge
    graph.remove_edge(1, 3)

    # Printing the graph after removals
    print("\nGraph after removing vertex and edge:")
    graph.print_graph()


if __name__ == "__main__":
    main()
