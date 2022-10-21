graph = {}
fruit = "mango"
graph["you"] = ["alice", " ЬоЬ", "claire"]
print(graph)
for i in range(len(graph) - 1):

    if fruit in graph:
        print("Found!")
    else:
        print(graph.get())