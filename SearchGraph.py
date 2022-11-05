from matplotlib import image
from matplotlib import pyplot as plt
import math

path_img = "Images/IMG_6722.JPG"
#for simplicity we ll consider heuristic distances given
#and this function returns heuristic distance for all nodes
def heuristic(n, stop_node):
    H_dist = {
        'A': manhattan_distance('A', stop_node)/speed_nodes(stop_node),
        'B': manhattan_distance('B', stop_node)/speed_nodes(stop_node),
        'C': manhattan_distance('C', stop_node)/speed_nodes(stop_node),
        'D': manhattan_distance('D', stop_node)/speed_nodes(stop_node),
        'E': manhattan_distance('E', stop_node)/speed_nodes(stop_node),
        'F': manhattan_distance('F', stop_node)/speed_nodes(stop_node),
        'G': manhattan_distance('G', stop_node)/speed_nodes(stop_node),
        'H': manhattan_distance('H', stop_node)/speed_nodes(stop_node),
        'I': manhattan_distance('I', stop_node)/speed_nodes(stop_node),
        'J': manhattan_distance('J', stop_node)/speed_nodes(stop_node)
    }
    return H_dist[n]

def manhattan_distance(n, ng):
    x_n = coords_nodes(n)[0]
    y_n = coords_nodes(n)[1]
    x_g = coords_nodes(ng)[0]
    y_g = coords_nodes(ng)[1]
    return abs(x_n - x_g) + abs(y_n - y_g)


def speed_nodes(n):
    speed = {
        'A': 0,
        'B': 44,
        'C': 88,
        'D': 94,
        'E': 44,
        'F': 77,
        'G': 99,
        'H': 33,
        'I': 83,
        'J': 66,
    }
    return speed[n]

def coords_nodes(n):
    coords = {
        'A':(2, 9),
        'B':(1,5),
        'C':(2,3),
        'D':(4,5),
        'E':(4,1),
        'F':(7,8),
        'G':(5,6),
        'H':(9,5),
        'I':(7,4),
        'J':(6,1),
    }
    return coords[n]

def aStarAlgo(start_node, stop_node, Graph_nodes):
    open_set = set(start_node)
    closed_set = set()
    g = {}  # store distance from starting node
    parents = {}  # parents contains an adjacency map of all nodes
    # distance of starting node from itself is zero
    g[start_node] = 0
    # start_node is root node i.e it has no parent nodes
    # so start_node is set to its own parent node
    parents[start_node] = start_node
    while len(open_set) > 0:
        n = None
        # node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v, stop_node) < g[n] + heuristic(n, stop_node):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n, Graph_nodes):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # for each node m,compare its distance from start i.e g(m) to the
                # from start through n node
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n
                        # if m in closed set,remove and add to open
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Il percorso non esiste!')
            return None

        # if the current node is the stop_node
        # then we begin reconstructin the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Percorso migliore trovato: {}'.format(path))
            return path
        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)
    print('Il percorso non esiste!')
    return None

# define fuction to return neighbor and its distance
# from the passed node
def get_neighbors(v, Graph_nodes):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def createGraph():
    # Describe your graph here
    graph = {
        'A': [('B', 6), ('F', 3)],
        'B': [('A', 6), ('C', 3), ('D', 2)],
        'C': [('B', 3), ('D', 1), ('E', 5)],
        'D': [('B', 2), ('C', 1), ('E', 8)],
        'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
        'F': [('A', 3), ('G', 1), ('H', 7)],
        'G': [('F', 1), ('I', 3)],
        'H': [('F', 7), ('I', 2)],
        'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    }
    return graph

def showGraph():
    data = image.imread(path_img)
    plt.plot(100, 100, marker='v', color="white")
    plt.imshow(data, extent=([0, 10, 0, 10]))
    plt.show()
