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
combo = []
for k,v in graph.items():
	if k.startswith('t'):
		for i in range(len(v)):
			for j in range(i+1, len(v)):
				neighbour_a, neighbour_b = v[i], v[j]
				if neighbour_b in graph[neighbour_a]:
					current = sorted([k, neighbour_a, neighbour_b])
					if current not in combo:
						combo.append(current)
ans = len(combo)
print(ans)
input_data.close()