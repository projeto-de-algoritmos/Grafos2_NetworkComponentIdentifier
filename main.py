"""
Receive commands and draw a random graph with N nodes
"""

import logging
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

from random import random
from src.component import detected_components_in_digraph
from src.graph import create_random_graph, inverse_networkx_graph, dfsNumbering
from constants import *

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

IMG_FILE: str = 'graph.png'

if __name__ == '__main__':

    try:
        N = int(sys.argv[1])
    except IndexError:
        N = 20
    except ValueError: 
        logger.error('Send argument N as a number')
    except:
        logger.error('Usage python main.py N')
        raise

    logger.info(f'Creating random graph with {N} nodes')

    nodes = []

    for i in range(1, N+1):
        nodes.append(f'N{i}')

    G = create_random_graph(nodes)

    logger.info('Creating numbering')
    pre, pos = dfsNumbering(nx.to_dict_of_lists(G))

    if DEBUG:
        plt.subplot(131)
        nx.draw_circular(G, with_labels=True, font_weight='bold')


    logger.info('Creating inverse graph')
    inverse_graph = inverse_networkx_graph(G)

    if DEBUG:
        plt.subplot(132)
        nx.draw_circular(inverse_graph, with_labels=True, font_weight='bold')


    logger.info('Generating components')
    components = detected_components_in_digraph(
        nx.to_dict_of_lists(inverse_graph),
        pos
    )

    logger.info(f'We finded {len(components)} components')
    for pos, component in enumerate(components):
        logger.info(f'Component {pos+1}: {component}')


    if GENERATE_IMG:

        if DEBUG:
            plt.subplot(133)

        logger.info('Drawing image')
        for num, component in  enumerate(components):

            nx.draw_circular(
                G,
                nodelist=component,
                font_weight='bold',
                with_labels=True,
                node_color=np.array(
                    [
                        random(),
                        random(),
                        random()
                    ]
                ).reshape(1, -1)
            )

        logger.info(f'Saving image into {IMG_FILE}')

        plt.savefig(IMG_FILE)
