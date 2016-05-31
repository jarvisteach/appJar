# empty dictionary
adjLists_dict = {}

# insert (vertex, list) pairs into dictionary
adjLists_dict[0] = [1,2]
adjLists_dict[1] = [2,3]
adjLists_dict[2] = [4]
adjLists_dict[3] = [4,5]
adjLists_dict[4] = [5]
adjLists_dict[5] = []

# testing
print("Neighbors of vertex 0: ", adjLists_dict[0])
print("Neighbors of vertex 3: ", adjLists_dict[3])

print("\nPrint all adjacency lists with corresponding vertex")
n = len(adjLists_dict)
for v in range(0,n):
      print(v, ":", adjLists_dict[v])
