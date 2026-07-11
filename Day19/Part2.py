input_data = open('/home/advent-of-code-2024/Day19/advent_of_code_19.txt','r')
input_data_lst = [x.replace('\n','').split(',') for x in input_data]
towel_pattern = [x.strip() for x in input_data_lst[0]]
towel_design = [''.join(x) for x in input_data_lst[1:] if x != ['']]
valid_design_ways = 0
for i in range(len(towel_design)):
	current_design = towel_design[i]
	queue = {}
	for j in range(len(towel_pattern)):
		current_pattern = towel_pattern[j]
		if current_design.startswith(current_pattern):
			queue[current_pattern] = 1
	
	while queue:
		new_queue = {}
		for j in range(len(queue)):
			current_pattern = list(queue.keys())[j]
			if current_pattern == current_design:
				valid_design_ways += queue[current_pattern]
			for k in range(len(towel_pattern)):
				next_pattern = towel_pattern[k]
				if current_design.startswith(current_pattern + next_pattern):
					if current_pattern + next_pattern not in new_queue:
						new_queue[current_pattern + next_pattern] = 0
					new_queue[current_pattern + next_pattern] += queue[current_pattern]
		queue = new_queue
print(valid_design_ways)
input_data.close()