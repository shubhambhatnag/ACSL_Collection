file = open("PracticeACSL.txt","r")
graph = []
for line in file.readlines():
    line = line.rstrip()
    line = line.split(",")
    if len(line) < 3:
        graph.append(line)
        continue
    else:
        line = [[line[0],line[1]],int(line[2])]
        graph.append(line)
start = graph[-1][0]
end = graph[-1][1]
graph.pop(-1)
weight = 0
currentNode = start
pathTotal = []
pathTotal.append(start)
used = []
while currentNode != end:
    shortestPath = None
    for path in graph:
        if currentNode in path[0] and path not in used:
            if shortestPath == None:
                if currentNode == path[0][0]:
                    shortestPath = [path[0][1],path[1],path]
                else:
                    shortestPath = [path[0][0],path[1],path]
                
            else:
                if path[1] < shortestPath[1]:
                    if currentNode == path[0][0]:
                        shortestPath = [path[0][1],path[1],path]
                    else:
                        shortestPath = [path[0][0],path[1],path]
            
    for path in graph:
        if currentNode in path[0] and shortestPath[0] in path[0]:
            weight += shortestPath[1]
            used.append(shortestPath[2])
            break
    
    currentNode = shortestPath[0]
    pathTotal.append(currentNode)
print("-".join(pathTotal))
