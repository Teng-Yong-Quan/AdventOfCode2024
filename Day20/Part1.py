input_data = open('/home/advent-of-code-2024/Day20/advent_of_code_20.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
walls = [(i, j) for i in range(len(input_data_lst)) for j in range(len(input_data_lst[i])) if input_data_lst[i][j] == '#']
tracks = [(i, j) for i in range(len(input_data_lst)) for j in range(len(input_data_lst[i])) if input_data_lst[i][j] == '.']
start = [(i, j) for i in range(len(input_data_lst)) for j in range(len(input_data_lst[i])) if input_data_lst[i][j] == 'S'][0]
end = [(i, j) for i in range(len(input_data_lst)) for j in range(len(input_data_lst[i])) if input_data_lst[i][j] == 'E'][0]
time_passes = 0

original_track = [start]
while original_track[-1] != end:
	current = original_track[-1]
	current_x, current_y = current
	next_positions = [(current_x + 1, current_y), (current_x - 1, current_y), (current_x, current_y + 1), (current_x, current_y - 1)]
	for next_pos in next_positions:
		if (next_pos in tracks or next_pos == end) and next_pos not in original_track:
			original_track.append(next_pos)
			#print(next_pos)
			break

for wall in walls:
	valid = False
	if ((wall[0], wall[1] + 1) in original_track) and ((wall[0], wall[1] - 1) in original_track):
		if abs(original_track.index((wall[0], wall[1] + 1)) - original_track.index((wall[0], wall[1] - 1))) - 2 >= 100:
			valid = True
	if ((wall[0] + 1, wall[1]) in original_track) and ((wall[0] - 1, wall[1]) in original_track):
		if abs(original_track.index((wall[0] + 1, wall[1])) - original_track.index((wall[0] - 1, wall[1]))) - 2 >= 100:
			valid = True
	if valid:
		time_passes += 1
print(time_passes)
input_data.close()