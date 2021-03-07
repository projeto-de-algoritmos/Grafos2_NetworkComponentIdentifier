from src.graph import create_random_graph

import networkx as nx

import matplotlib.pyplot as plt

def inverse_networkx_graph(graph):

    r_graph = nx.DiGraph()

    inverse_edges = [(y, x) for x, y in graph.edges]

    r_graph.add_edges_from(inverse_edges)

    return r_graph

if __name__ == '__main__':


    G = create_random_graph(['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8'])

    plt.subplot(131)

    nx.draw(G, with_labels=True, font_weight='bold')

    inverse_graph = inverse_networkx_graph(G)

    plt.subplot(132)

    print(inverse_graph)

    nx.draw(inverse_graph, with_labels=True, font_weight='bold')

    plt.savefig('graph.png')
