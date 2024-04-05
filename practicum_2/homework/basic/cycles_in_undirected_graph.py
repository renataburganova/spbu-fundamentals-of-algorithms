import networkx as nx
import matplotlib.pyplot as plt

TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_w_cycles.edgelist",
]


def plot_graph(G):
    options = dict(
        font_size=12,
        node_size=500,
        node_color="white",
        edgecolors="black",
    )
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, **options)
    if nx.is_weighted(G):
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def has_cycles_dfs_algorithm(G):
    colour = {}
    parent = {}

    def dfs_visit(node):
        colour[node] = 1
        for neighbor in G.neighbors(node):
            if colour.get(neighbor, 0) == 0:
                parent[neighbor] = node
                for j in G.neighbors(neighbor):
                    if (colour.get(j, 0) == 1 or colour.get(j, 0) == 2) and j != parent[neighbor]:
                        return False
                if not dfs_visit(neighbor):
                    return False
        colour[node] = 2
        return True

    for node in G:
        if node not in colour:
            if not dfs_visit(node):
                return False
    return True


if __name__ == "__main__":
    for filename in TEST_GRAPH_FILES:
        G = nx.read_edgelist("C:/IT/algorithms/spbu-fundamentals-of-algorithms/practicum_2/homework/basic/" + filename,
                             create_using=nx.Graph)
        plot_graph(G)
        if has_cycles_dfs_algorithm(G):
            print(f"Graph {filename} has cycles: NO")
        else:
            print(f"Graph {filename} has cycles: YES")
