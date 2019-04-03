# AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
graph = {'A': [('B', 5), ('D', 5), ('E', 7)],
         'B': [('C', 4)],
         'C': [('D', 8), ('E', 2)],
         'D': [('C',8), ('E', 6)],
         'E': [('B', 3)]
          }

def find_dist_route(network, route):
    #edge = []
    edge = route.split('-')
    node_len = len(edge)
    print(node_len)
    total_dist = 0
    for i in range(0,len(edge)): 
        #print(i)
        if i < len(edge) - 1:
            counter = 0
            start = edge[i]
            end = edge[i+1]
            print("Start: ", start)
            print("End: ", end)
            if start in network.keys():
                for node, x in network.items():
                    if node == start:
                        print("x value:", x)
                        for a,b in x:
                            print("a value:",a)
                            print("b value:", b)
                            if a == end:
                                print("Edge value:",b)
                                total_dist = total_dist+b
                                counter = 1
                                break;
                            #else:
    if counter == 0:
        output = 'No Such Routes'
    else:
        output = str(total_dist)
    return output

print(find_dist_route(graph, input("Enter the route :")))	

