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
                if v[h] not in antinode:
                    antinode.append(v[h])
                if v[end] not in antinode:
                    antinode.append(v[end])
                row_diff = v[h][0] - v[end][0] 
                col_diff = v[h][1] - v[end][1]
                anti_row_h , anti_col_h, anti_row_end, anti_col_end = v[h][0],v[h][1],v[end][0], v[end][1]
                anti_h_exceed, anti_end_exceed = False, False
            
                while True:
                    if anti_row_h < 0 or anti_row_h >= len(input_data_lst) or  0 > anti_col_h or anti_col_h >= len(input_data_lst[0]):
                        anti_h_exceed = True
                    else:
                        anti_row_h  += row_diff
                        anti_col_h += col_diff
                        antinode_h = [anti_row_h,anti_col_h]
                        if antinode_h not in antinode:
                            antinode.append(antinode_h)
                    if 0 > anti_row_end or anti_row_end >= len(input_data_lst) or  0 > anti_col_end or anti_col_end >= len(input_data_lst[0]):   
                        anti_end_exceed = True
                    else:
                        anti_row_end -= row_diff
                        anti_col_end -= col_diff
                        antinode_end = [anti_row_end,anti_col_end]
                        if antinode_end not in antinode:
                            antinode.append(antinode_end)
                    if anti_h_exceed and anti_end_exceed:
                        break
                end+=1

for anti in range(len(antinode)):
    if antinode[anti][0] < 0 or antinode[anti][0] >= len(input_data_lst) or antinode[anti][1] < 0 or antinode[anti][1] >= len(input_data_lst[0]):
        antinode[anti] = 0

valid_antinode = sorted([x for x in antinode if x])
print(len(valid_antinode))
input_data.close()