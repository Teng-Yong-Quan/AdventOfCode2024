def bron_kerbosch(current_clique, candidates, processed_vertices, graph):
	if not candidates and not processed_vertices:
		if len(current_clique) > 2:
			cliques.append(list(current_clique))
		return
	union_set = candidates.union(processed_vertices)
	pivot = max(union_set, key=lambda v: len(graph[v]))
	possibles = candidates.difference(graph[pivot])
	for vertex in possibles:
		new_clique = current_clique.union({vertex})
		new_candidates = candidates.intersection(graph[vertex])
		new_processed_vertices = processed_vertices.intersection(graph[vertex])
		bron_kerbosch(new_clique, new_candidates, new_processed_vertices, graph)
		candidates.remove(vertex)
		processed_vertices.add(vertex)
	
input_data = open('/home/advent-of-code-2024/Day23/advent_of_code_23.txt','r')
input_data_lst = [x.replace('\n','').split('-') for x in input_data]
graph = {}
for pair in input_data_lst:
	left, right = pair[0], pair[1]
	if left not in graph:
		graph[left] = []
	graph[left].append(right)
	if right not in graph:
		graph[right] = []
	graph[right].append(left)
cliques = []
current_clique = set()
candidates = set(graph.keys())
processed_vertices = set()
bron_kerbosch(current_clique, candidates, processed_vertices, graph)
ans = ','.join(sorted(max(cliques, key=len)))
print(ans)
input_data.close()