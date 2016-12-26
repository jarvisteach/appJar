import heapq
# first build an adjacency list
graph = {}
graph['a'] = [('b', 0.95), ('d', 0.72), ('e', 1.75)]
graph['b'] = [('a', 0.95), ('c', 0.32), ('e', 0.82)]
graph['c'] = [('b', 0.32), ('e', 0.17), ('f', 0.91)]
graph['d'] = [('a', 0.72), ('e', 0.29), ('g', 0.17)]
graph['e'] = [('a', 1.75), ('b', 0.82), ('c', 0.17), ('d', 0.29), ('f', 0.33), ('g', 0.27), ('h', 0.18), ('i', 1.98)]
graph['f'] = [('c', 0.91), ('e', 0.33), ('i', 0.13)]
graph['g'] = [('d', 0.17), ('e', 0.27), ('h', 0.92)]
graph['h'] = [('e', 0.18), ('g', 0.92), ('i', 0.22)]
graph['i'] = [('e', 1.98), ('f', 0.13), ('h', 0.22)]

print(graph)

# function to list all neighbours of a node
def showNeighbours(node):
      print("The neighbors of '", node, "' are: ")
      for tup in graph[node]:
            print(tup[0], "distance", tup[1])


# function to show the weight of an edge
def showEdge(source, dest):
      for tup in graph[source]:
            neighbor = tup[0]
            weight = tup[1]
            if neighbor == dest:
                  print("The weight of the edge {'", source, "', '", dest, "'} is: ", weight)
                  break

# funciton to sum the weights of all nighbour-edges
def sumEdges(node):
      total = 0.0
      for tup in graph[node]:
            weight = tup[1]
            total += weight
      print("node", node, " -> sum of edge weights: ", total)


def dijkstra(adj, source, target):
      print(">>", source, "-->", target)
      INF = ((1<<63) - 1)//2
      pred = { x:x for x in adj }
      dist = { x:INF for x in adj }
      dist[ source ] = 0
      PQ = []
      heapq.heappush(PQ, [dist[ source ], source])

      while(PQ):
            u = heapq.heappop(PQ)  # u is a tuple [u_dist, u_id]
            u_dist = u[0]
            u_id = u[1]
            if u_dist == dist[u_id]:
                  if u_id == target:
                        break
                  for v in adj[u_id]:
                        v_id = v[0]
                        w_uv = v[1]
                        if dist[u_id] +  w_uv < dist[v_id]:
                              dist[v_id] = dist[u_id] + w_uv
                              heapq.heappush(PQ, [dist[v_id], v_id])
                              pred[v_id] = u_id
                                                                        
      if dist[target]==INF:
            print("There is no path between ", source, "and", target)
      else:
            st = []
            node = target
            while(True):
                  st.append(str(node))
                  if(node==pred[node]):
                        break
                  node = pred[node]
            path = st[::-1]
            print("The shortest path is: " + " ".join(path))
            print("The distance from '", source, "' to '", target, "' is: " + str(dist['i']))
            print("distance dictionary: " + str(dist))
            print("predecessor dictionary: " + str(pred))

#showNeighbours("a")
#showEdge("a", "e")
#sumEdges("a")
dijkstra(graph, "a", "a")
dijkstra(graph, "a", "b")
dijkstra(graph, "a", "c")
dijkstra(graph, "a", "d")
dijkstra(graph, "a", "e")
