"""
Just a simple graph structure that saves a name and 
the ID in Graph.nodes[i] that have a edge
"""

from __future__ import annotations

from networkx import DiGraph

import random

def create_random_graph(names: list[str]) -> Graph:
    """
    Create a random graph using a list of names
    """

    graph = DiGraph()

    max_friends = len(names)//4

    for name in names:

        num_friends: int = random.randint(0, max_friends)
        friends: list[int] = random.choices(names, k=num_friends)

        for friend in friends:
            graph.add_edge(name, friend)

    return graph
