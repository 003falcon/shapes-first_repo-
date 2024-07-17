def heuristic_val(n):
    dist = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 2,
        "e": 4,
        "f": 4
    }
    return dist[n]

Graph_nodes = {                                            #Graph somewhat looks like this
     "a":[("b",6),("c",14)],                                #         a
     "b":[("a",6),("c",7),('f',5),("d",1)],                #       /
     "c":[("a",14),("d",8),("b",7),("e",4),("f",4)],        #      b ----- d
     "d":[("c",8),("b",1),("e",5)],                         #      | \  / |
     "e":[("d",5),("c",4),("f",1)],                         #     |   c   |
     "f":[("c",4),("b",5),("e",1)]                          #     | /   \ |
}                                                           #     f -----e

obstacles = {"c"}  # Define the obstacle nodes

def get_nebor(x):#nebor short for neighbour
    if x in Graph_nodes:
        neighbors = []
        for neighbor, weight in Graph_nodes[x]:
            if neighbor not in obstacles:  # Checking for obstacles
                neighbors.append((neighbor, weight))
        return neighbors
    else:
        return None

def Astar(begin_node, end_node):
    open_set = set(begin_node) #this set refers to the nodes which is going to be traversed
    closed_set = set()         #whereas this set refers to the nodes already traversed
    start_dist = {}            #initializing a dictionary to keep count of node and its distance
    source = {}                 #initializing a dictionary to keep
                                # track of the current node and its previous node
    start_dist[begin_node] = 0
    source[begin_node] = begin_node #putting the current and prev node as the start node initially

    while len(open_set) > 0:
        n = None
        for x in open_set:
            if n is None or start_dist[x] + heuristic_val(x) < start_dist[n] + heuristic_val(n):
                n = x#initializing the node to the begin node

        if n != end_node or Graph_nodes[n] !=None:#here  we're checking for neighbours
                                                  # only if the current node is not the destination node

            for m, wt in get_nebor(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    source[m] = n
                    start_dist[m] = start_dist[n] + wt
                else:
                    if start_dist[m] > start_dist[n] + wt:
                        start_dist[m] = start_dist[n] + wt
                        source[m] = n
                        if m in closed_set:
                           closed_set.remove(m)
                           open_set.add(m)

        if n == end_node:
            path = []
            while source[n] != n:
                path.append(n)
                n = source[n]#node traversing back to source node to obtain path in reverse
            path.append(begin_node)
            path.reverse()
            print("Path found: {}".format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)


    print("Path doesn't exist")
    return None

Astar( 'a',"e")#start node-a,end node-d here
