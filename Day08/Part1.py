input_data = open('/home/advent-of-code-2024/Day08/advent_of_code_8.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
dic = {}
antinode = []
for i in range(len(input_data_lst)):  
    for j in range(len(input_data_lst[0])):
        if input_data_lst[i][j] != '.':
            key = input_data_lst[i][j]
            if input_data_lst[i][j] not in dic:
                dic[key] = [[i,j]]
            else:
                dic[key].append([i,j])

for k,v in dic.items():
    if len(v) == 1:
        continue
    else:
        for h in range(len(v)-1):
            end = h + 1
            while end < len(v):
                row_diff = v[h][0] - v[end][0] 
                col_diff = v[h][1] - v[end][1]
                anti_row_h , anti_col_h, anti_row_end, anti_col_end = v[h][0],v[h][1],v[end][0], v[end][1]
            
                anti_row_h  += row_diff
                anti_col_h += col_diff
                antinode_h = [anti_row_h,anti_col_h]
                if antinode_h not in antinode:
                    antinode.append(antinode_h)
                    
                anti_row_end -= row_diff
                anti_col_end -= col_diff
                antinode_end = [anti_row_end,anti_col_end]
                if antinode_end not in antinode:
                    antinode.append(antinode_end)
                    
                end+=1

for anti in range(len(antinode)):
    if antinode[anti][0] < 0 or antinode[anti][0] >= len(input_data_lst) or antinode[anti][1] < 0 or antinode[anti][1] >= len(input_data_lst[0]):
        antinode[anti] = 0

valid_antinode = sorted([x for x in antinode if x])
print(len(valid_antinode))
input_data.close()