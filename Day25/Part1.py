input_data = open('/home/advent-of-code-2024/Day25/advent_of_code_25.txt','r')
input_data_lst = [x.replace("\n", "") for x in input_data]
keys_and_locks = []
current_item = []
for i in input_data_lst:
	if i == '':
		keys_and_locks.append(current_item)
		current_item = []
	else:
		current_item.append(i)
keys_and_locks.append(current_item)
all_keys = [x for x in keys_and_locks if all(c == '.' for c in x[0])]
all_locks = [x for x in keys_and_locks if all(c == '#' for c in x[0])]
all_keys_height = []
for each_key in all_keys:
	height = [0,0,0,0,0]
	for i in range(len(each_key)-1):
		for j in range(len(each_key[i])):
			if each_key[i][j] == '#':
				height[j] += 1
	all_keys_height.append(height)
all_locks_height = []
for each_lock in all_locks:
	height = [0,0,0,0,0]
	for i in range(1, len(each_lock)):
		for j in range(len(each_lock[i])):
			if each_lock[i][j] == '#':
				height[j] += 1
	all_locks_height.append(height)
ans = 0
for every_key in all_keys_height:
	for every_lock in all_locks_height:
		if all(x+y <= 5 for x,y in zip(every_key, every_lock)):
			ans += 1
print(ans)
input_data.close()
