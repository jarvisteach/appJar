# list of lists
adjLists = [ [1,2], [2,3], [4], [4,5], [5], [] ]

# testing
print("Neighbors of vertex 0: ", adjLists[0])
print("Neighbors of vertex 3: ", adjLists[3])
 
print("\nPrint all adjacency lists with corresponding vertex")
n = len(adjLists)
for v in range(0,n):
      print(v, ":", adjLists[v])
