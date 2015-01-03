from collections import namedtuple

class Edge(namedtuple('Edge', 'start end cost')):
    __slots__ = ()

    def __contains__(self, v):
        return v == self.start or v == self.end

    def other(self, v):
        if v == self.start:
            return self.end
        if v == self.end:
            return self.start
        raise ValueError


class Graph:
    def __init__(self, vertices, edges):
        self.edges = edges
        self.vertices = vertices

    def connections(self, v):
        yield from [e for e in self.edges if v in e]

    def check_in_graph(self, v):
        if v not in self.vertices:
            template = "'{v}' not in vertices: {vs}"
            raise ValueError(template.format(v=v, vs=self.vertices))


    def shortest_distance(self, source, destination=None):
        self.check_in_graph(source)
        if destination:
            self.check_in_graph(destination)

        if source == destination:
            return 0

        distances = {v: float('inf') for v in self.vertices}
        distances[source] = 0
        distances.update(**{e.other(source): e.cost
                            for e in self.connections(source)})

        unvisited = [v for v in self.vertices if v != source]

        while (destination is None and unvisited) or destination in unvisited:
            current = min(unvisited, key=distances.get)
            unvisited.remove(current)

            for e in self.connections(current):
                other = e.other(current)
                distances[other] = min(distances.get(other, float('inf')),
                                       distances[current] + e.cost)
        if destination:
            return distances[destination]
        return distances




if __name__ == '__main__':
    # test data from http://rosettacode.org/wiki/Dijkstra%27s_algorithm
    rosetta_vertices = ('a', 'b', 'c', 'd', 'e', 'f')
    rosetta_edges = (Edge(start='a', end='b', cost=7),
                     Edge(start='a', end='c', cost=9),
                     Edge(start='a', end='f', cost=14),
                     Edge(start='b', end='c', cost=10),
                     Edge(start='b', end='d', cost=15),
                     Edge(start='c', end='d', cost=11),
                     Edge(start='c', end='f', cost=2),
                     Edge(start='d', end='e', cost=6),
                     Edge(start='e', end='f', cost=9))

    g = Graph(rosetta_vertices, rosetta_edges)

    print(g.shortest_distance('a', 'e'))
    print(g.shortest_distance('a'))
