import itertools

def get_shortest_moves(start, dest, pad, dict):
	if start == dest:
		if (start, dest) not in dict:
			dict[(start, dest)] = ['A']
		return dict
	coord_to_key = {coord: key for key, coord in pad.items()}
	dx, dy = pad[dest][0] - pad[start][0], pad[dest][1] - pad[start][1]
	route = ''
	if dx < 0:
		route += abs(dx) * '^'
	elif dx > 0:
		route += dx * 'v'
	if dy < 0:
		route += abs(dy) * '<'
	elif dy > 0:
		route += dy * '>'
	new_permutations = []
	for perm in set(itertools.permutations(route)):
		next = start
		prev = start
		isvalid = True
		for move in perm:
			prev_coord = pad[prev]
			next_coord = pad[prev]
			if move == '<':
				next_coord = (prev_coord[0], prev_coord[1] - 1)
			elif move == '>':
				next_coord = (prev_coord[0], prev_coord[1] + 1)
			elif move == '^':
				next_coord = (prev_coord[0] - 1, prev_coord[1])
			elif move == 'v':
				next_coord = (prev_coord[0] + 1, prev_coord[1])
			if next_coord not in pad.values():
				isvalid = False
				break
			next = coord_to_key[next_coord]
			prev = next
		if isvalid and  next == dest:
			new_permutations.append(''.join(perm) + 'A')
	new_permutations = [x for x in new_permutations if len(x) == min(map(len, new_permutations))]	
	if (start, dest) not in dict:
		dict[(start,dest)] = []
	for new_perm in new_permutations:
		if new_perm not in dict[(start,dest)]:
			dict[(start,dest)].append(new_perm)
	return dict

def get_all_shortest_moves(pad):
	dict = {}
	for i in range(len(list(pad.keys()))):
		for j in range(len(list(pad.keys()))):
			dict = get_shortest_moves(list(pad.keys())[i], list(pad.keys())[j], pad, dict)
	return dict

def cost(start, end, depth):
	dict = None
	if max_depth == depth:
		dict = shortest_moves_num_dict
	else:
		dict = shortest_moves_dir_dict
	if (start, end, depth) in memo:
		return memo[(start, end, depth)]
	if depth == 0:
		return min(map(len,dict[(start,end)]))
	cost_lst = []
	for transition in dict[(start,end)]:
		current = 'A'
		total_cost = 0
		for next in transition:
			total_cost += cost(current, next, depth - 1)
			current = next
		cost_lst.append(total_cost)
	answer = min(cost_lst)
	memo[(start,end,depth)] = answer
	return answer
	
input_data = open('/home/advent-of-code-2024/Day21/advent_of_code_21.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
num_pad = {'A' : (3,2), '0' : (3,1), '1' : (2,0), '2' : (2, 1), '3' : (2,2), '4': (1,0), '5' : (1,1), '6' : (1,2), '7' : (0,0), '8' : (0,1), '9' : (0,2)}
dir_pad = {'<': (1,0), '>': (1,2), '^': (0,1), 'v': (1,1), 'A': (0,2)}
shortest_moves_num_dict = get_all_shortest_moves(num_pad)
shortest_moves_dir_dict = get_all_shortest_moves(dir_pad)
result = []
max_depth = 26 - 1
memo = {}
for input in input_data_lst:
	start = 'A'
	total_cost = 0
	for num in input:
		next = num
		total_cost += cost(start, next, max_depth)
		start = next
	result.append(total_cost)
result = sum([x*int(y[:-1]) for x,y in zip(result, input_data_lst)])
print(result)
input_data.close()