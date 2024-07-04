import random
import networkx as nx


def remove_random_nodes_attack(G, f):
    num_nodes_to_remove = int(f * len(G.nodes()))
    nodes_to_remove = random.sample(list(G.nodes()), num_nodes_to_remove)

    for node in nodes_to_remove:
        G.remove_node(node)

    return G


def remove_highest_degree_nodes_attack(G, f):
    num_nodes_to_remove = int(f * len(G.nodes()))
    nodes_to_remove = sorted(G.degree, key=lambda x: x[1], reverse=True)[:num_nodes_to_remove]

    for node in nodes_to_remove:
        G.remove_node(node[0])

    return G


def remove_highest_page_rank_nodes_attack(G, f):
    pr = nx.pagerank(G)
    num_nodes_to_remove = int(f * len(G.nodes()))
    nodes_to_remove = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:num_nodes_to_remove]

    for node in nodes_to_remove:
        G.remove_node(node[0])

    return G


def remove_highest_betweenness_nodes_attack(G, f):
    betweenness = nx.betweenness_centrality(G)
    num_nodes_to_remove = int(f * len(G.nodes()))
    nodes_to_remove = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:num_nodes_to_remove]

    for node in nodes_to_remove:
        G.remove_node(node[0])

    return G




