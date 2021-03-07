from src.graph import create_random_graph
from collections import defaultdict
import networkx as nx

import matplotlib.pyplot as plt

layout = nx.spring_layout

def inverse_networkx_graph(graph):

    r_graph = nx.DiGraph()

    inverse_edges = [(y, x) for x, y in graph.edges]

    r_graph.add_edges_from(inverse_edges)

    [r_graph.add_node(node) for node in graph.nodes]

    return r_graph


def dfs(graph):


    pre = defaultdict(int)
    pos = defaultdict(int)
    time = 1

    def dfs_visit(graph, node, visited, pre, pos, time):

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

# networkx lib don't detect components in a direct graph
def detected_components_in_digraph(graph, pos):

    pos = sorted(pos.items(), key=lambda x : x[1], reverse=True)

    components: list[list[str]] = []

    visited = defaultdict(bool)

    def mark_dfs(graph, node, visited):

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

if __name__ == '__main__':

    nodes = []
    for i in range(1,20):
        nodes.append(f'N{i}')

    G = create_random_graph(nodes)
    lay = layout(G)

    pre, pos = dfs(nx.to_dict_of_lists(G))

    inverse_graph = inverse_networkx_graph(G)

    components = detected_components_in_digraph(nx.to_dict_of_lists(inverse_graph), pos)

    import random

    for num, component in  enumerate(components):

        print(component)
        nx.draw_circular(
            G,
            width=0.5,
            nodelist=component,
            font_weight='bold',
            with_labels=True,
            node_color=(
                random.random(),
                random.random(),
                random.random()
            )
        )

    plt.savefig('graph.png')
