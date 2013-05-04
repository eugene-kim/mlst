import graph
import reader

f = open('kindahard.in')

infile = reader.InFileReader(f)

edgeSet = infile.read_input_file() # contains graph(s)

for i in edgeSet: # we work with one graph at a time
	inst = graph.make_graph(i) # instance of the graph

	inst.search() # sets graph properties by DFS search

	vertices = dict() # dict of directed edges
	doublevertex = dict() # dict of undirected edges

	for j in i: # intialize both dicts properly
		vertices[j.ends[0]] = [] 
		doublevertex[j.ends[0]] = [] 
		doublevertex[j.ends[1]] = [] 
 	for j in i: # add edges of graph 
		vertices[j.ends[0]].append(j.ends[1])
		doublevertex[j.ends[0]].append(j.ends[1])
		doublevertex[j.ends[1]].append(j.ends[0])

	maxNum = 0 # max num of edges going into any of the vertices in the graph
	maxVertexList = [] # list of max edge count vertices

	# set maxNum
	for a in doublevertex.keys():
		maxNum = max(maxNum,len(doublevertex[a]))
	# append max edge nodes to maxVertexList
	for i in doublevertex.keys():
		if len(doublevertex[i]) == maxNum:
			maxVertexList.append(i)
	print maxNum
	print maxVertexList

	# we look at the graph len(maxVertexList) times to find the MLST solution.
	# numLeafNodes holds possible solutions 
	numLeafNodes = []

	for j in maxVertexList:
		testGraph = graph.Graph(5) # blank graph we start off with; 5 doesn't mean anything
		seen = []
		copy = vertices.copy() 
		for b in copy[j]: 
			testGraph.add_edge_uv(j,b)
		del copy[j] 
		seen.append(j) # starting point 
		while copy: # loop until the copy dict is empty
			for x in copy.keys(): # loop through vertices
				if x not in seen: # if we haven't gone through the node already,
					for y in copy[x]: # loop through connected vertices from vertex x
						testGraph.add_edge_uv(x,y) # add the edge to our graph
						testGraph.search() 
						if testGraph.has_cycle: 
							testGraph.rem_edge_uv(x,y)
					seen.append(x) 
					del copy[x] # remove vertex from dict
		# print testGraph.num_leaves
		numLeafNodes.append(testGraph.num_leaves)

	print numLeafNodes

	maxLeafNodes = max(numLeafNodes)
	print maxLeafNodes