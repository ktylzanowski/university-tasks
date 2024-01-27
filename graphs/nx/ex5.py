import networkx as nx


def find_leaves_and_supports(graph):
    G = nx.from_dict_of_lists(graph)

    leaves = [node for node in G.nodes() if G.degree(node) == 1]
    supports = set()

    for leaf in leaves:
        support = list(G.neighbors(leaf))[0]
        supports.add(support)

    return leaves, supports


def main():
    input_str = input()
    input_graph = eval(input_str)

    leaves, supports = find_leaves_and_supports(input_graph)
    sorted_supports = sorted(supports)
    if leaves:
        print("Liście:", " ".join(map(str, leaves)))
    else:
        print("Liście:")
    print("Supporty:", " ".join(map(str, sorted_supports)))


main()



