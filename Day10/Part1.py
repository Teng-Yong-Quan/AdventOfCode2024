input_data = open('/home/advent-of-code-2024/Day10/advent_of_code_10.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
score = 0
zeroes = []
for i in range(len(input_data_lst)):
    for j in range(len(input_data_lst[0])):
        if input_data_lst[i][j] == '0':
            zeroes.append([i,j])

for zero in range(len(zeroes)):
    routes = []
    num = 0
    start = zeroes[zero]
    routes.append([start])
    while num < 9:
        neighbours = []
        num+=1
        num_str = str(num)
        for index in range(len(routes[-1])):
            pos = routes[-1][index]
            row,column = pos[0], pos[1]
            left = [row,column-1]
            right = [row,column+1]
            up = [row-1,column]
            down = [row+1,column]
            if 0 <= left[0] < len(input_data_lst) and 0 <= left[1] < len(input_data_lst[0]) and input_data_lst[left[0]][left[1]] == num_str:
                neighbours.append(left)
            if 0 <= right[0] < len(input_data_lst) and 0 <= right[1] < len(input_data_lst[0]) and input_data_lst[right[0]][right[1]] == num_str:
                neighbours.append(right)
            if 0 <= up[0] < len(input_data_lst) and 0 <= up[1] < len(input_data_lst[0]) and input_data_lst[up[0]][up[1]] == num_str:
                neighbours.append(up)
            if 0 <= down[0] < len(input_data_lst) and 0 <= down[1] < len(input_data_lst[0]) and input_data_lst[down[0]][down[1]] == num_str:
                neighbours.append(down)
        routes.append(neighbours)
    unique_nines = []       
    for nine in range(len(routes[-1])):
        if routes[-1][nine] not in unique_nines:
            unique_nines.append(routes[-1][nine])
    score += len(unique_nines)
print(score)
input_data.close()