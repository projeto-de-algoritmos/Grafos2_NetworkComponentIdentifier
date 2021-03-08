"""
Util function to create grpahs
"""

from __future__ import annotations

import random

import networkx as nx
from networkx import DiGraph
from collections import defaultdict

def create_random_graph(names: list[str]) -> DiGraph:
    """
    Create a random graph using a list of names
    """

    graph = DiGraph()

    """
    Each node can create a edge with 25% of the other 
    nodes, this line is just for create a graph with 
    more components
    """
    max_friends = len(names)//4

    for name in names:

        graph.add_node(name)

        num_friends: int = random.randint(0, max_friends)
        friends: list[int] = random.choices(names, k=num_friends)

        for friend in friends:
            graph.add_edge(name, friend)

    return graph

def inverse_networkx_graph(graph: dict) -> DiGraph:
    """
    Create a graph with all edges inversed
    """

    r_graph = nx.DiGraph()

    inverse_edges = [(y, x) for x, y in graph.edges]

    r_graph.add_edges_from(inverse_edges)

    # add nodes that don't have edges
    [r_graph.add_node(node) for node in graph.nodes]

    return r_graph

def dfsNumbering(graph):
    """
    Compute the time that each node
    is visited and the time of each edge of a node
    finish to be visited
    """

    pre = defaultdict(int)
    pos = defaultdict(int)
    time = 1

    def dfs_visit(graph, node, visited, pre, pos, time):
        """
        Visit a node and every other node that we 
        can reach
        """

        if not (visited[node] == 0):
            return time

        pre[node] = time
        time+=1
        visited[node] = True

        for edge in graph[node]:
            if not visited[edge]:
                time = dfs_visit(graph, edge, visited, pre, pos, time)

        pos[node] = time
        time+=1

        return time

    visited = defaultdict(bool)

    for node in graph.keys():
        time = dfs_visit(graph, node, visited, pre, pos, time)

    return pre, pos

