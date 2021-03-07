from src.graph import create_random_graph

import networkx as nx

import matplotlib.pyplot as plt

if __name__ == '__main__':


    G = create_random_graph(['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8'])


    plt.subplot(111)

    nx.draw(G, with_labels=True, font_weight='bold')

    plt.savefig('graph.png')
