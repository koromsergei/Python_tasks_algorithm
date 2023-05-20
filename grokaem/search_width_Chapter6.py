graph = {}
fruit = "mango"
graph["you"] = ["alice", " ЬоЬ", "claire"]
graph['bob'] = ['alice', 'tom', 'ben']
graph['claire'] = ['bob', 'kate']
checked = []
for i in graph:
    for j in graph[i]:
        if j in checked:
            continue
        if 'm' in j:
            print(f"{j} is mango seller!")
            break
        else:
            checked.append(j)

else:
    print('Not found')