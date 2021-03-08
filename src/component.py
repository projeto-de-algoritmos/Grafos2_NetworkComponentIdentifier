from collections import defaultdict
from typing import Tuple, List, Dict

def detected_components_in_digraph(graph: dict, pos: List[Tuple[str, int]]) -> List[List[str]]:
    """
    Receive a graph and the time that each node
    finish to visit your edges
    """

    # visited the nodes that pos[i] is greater
    pos = sorted(pos.items(), key=lambda x : x[1], reverse=True)

    components: List[List[str]] = []

    visited: Dict[str, bool] = defaultdict(bool)

    def mark_dfs(graph, node, visited):
        """
        Return a component
        """

        component = []

        if visited[node]:
            return component

        visited[node] = True

        component.append(node)

        for edge in graph[node]:
            if not visited[edge]:
                component += mark_dfs(graph, edge, visited)

        return component

    for key, _ in pos:

        component = mark_dfs(graph, key, visited)

        if len(component):
            components.append(component)

    return components

