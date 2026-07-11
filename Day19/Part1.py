input_data = open('/home/advent-of-code-2024/Day19/advent_of_code_19.txt','r')
input_data_lst = [x.replace('\n','').split(',') for x in input_data]
towel_pattern = [x.strip() for x in input_data_lst[0]]
towel_design = [''.join(x) for x in input_data_lst[1:] if x != ['']]
valid_design = 0
for i in range(len(towel_design)):
	current_design = towel_design[i]
	queue = []
	for j in range(len(towel_pattern)):
		current_pattern = towel_pattern[j]
		if current_design.startswith(current_pattern):
			queue.append(current_pattern)
	isFound = False
	while queue:
		new_queue = []
		for j in range(len(queue)):
			current_pattern = queue[j]
			if current_pattern == current_design:
				isFound = True
				break
			for k in range(len(towel_pattern)):
				next_pattern = towel_pattern[k]
				if current_design.startswith(current_pattern + next_pattern) and current_pattern + next_pattern not in new_queue:
					new_queue.append(current_pattern + next_pattern)
		queue = new_queue
	if isFound:
		valid_design += 1
print(valid_design)
input_data.close()
