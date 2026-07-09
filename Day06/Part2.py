def left(current_position,new_map,wall):
    row,column = current_position[0], current_position[1]
    prev_col = 0
    while next_pos(row,column,'l',new_map,wall):
        if isOut(row,column,new_map):
            return []
        if [row,column] not in visited:
            visited.append([row,column])
        prev_col = column
        column -=1
    return [row,prev_col]
        
def right(current_position,new_map,wall):
    row,column = current_position[0], current_position[1]
    prev_col = 0
    while next_pos(row,column,'r',new_map,wall):
        if isOut(row,column,new_map):
            return []
        if [row,column] not in visited:
            visited.append([row,column])
        prev_col = column
        column +=1
    return [row,prev_col]

def up(current_position,new_map,wall):
    row,column = current_position[0], current_position[1]
    prev_row = 0
    while next_pos(row,column,'u',new_map,wall):
        if isOut(row,column,new_map):
            return []
        if [row,column] not in visited:
            visited.append([row,column])
        prev_row = row
        row -=1
    return [prev_row, column]

def down(current_position,new_map,wall):
    row,column = current_position[0], current_position[1]
    prev_row = 0
    while next_pos(row,column,'d',new_map,wall):
        if isOut(row,column,new_map):
            return []
        if [row,column] not in visited:
            visited.append([row,column])
        prev_row = row
        row +=1
    return [prev_row, column]

def next_pos(r,c,direction,new_map,wall):
    if not isOut(r,c,new_map):
        if new_map[r][c] == '#':
            if [r,c,direction] not in wall:
                wall.append([r,c,direction])
            return False
    return True

def isOut(r,c,new_map):
    if r == -1 or r == len(new_map) or c == -1 or c == len(new_map[0]):
        return True
    return False

def switch(new_map,wall,prev_wall):
    l,r,u,d = False,False,True,False
    curr_pos = start_position
    while True:
        prev_wall = wall.copy()
        if l:
            curr_pos = left(curr_pos,new_map,wall)
            if curr_pos:
                l = False
                u = True
            else:
                break
        elif r:
            curr_pos = right(curr_pos,new_map,wall)
            if curr_pos:
                r = False
                d = True
            else:
                break
        elif u:
            curr_pos = up(curr_pos,new_map,wall)
            if curr_pos:
                u = False
                r = True
            else:
                break
        elif d:
            curr_pos = down(curr_pos,new_map,wall)
            if curr_pos:
                d = False
                l = True
            else:
                break
        if len(wall) == len(prev_wall):
            return False
    return True

input_data = open('/home/advent-of-code-2024/Day06/advent_of_code_6.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
visited = []
start_position = []
for i in range(len(input_data_lst)):
    for j in range(len(input_data_lst[0])):
        if input_data_lst[i][j] == '^':
            start_position.append(i)
            start_position.append(j)
            break
switch(input_data_lst,[],[])
actual_visited = visited.copy()

#Slow and inefficient solution
ans = 0
counter = 0
for visit in actual_visited:
    print("counter: ",counter)
    counter+=1
    if visit == start_position:
        continue
    else:
        map_copy = input_data_lst.copy()
        visited = []
        row,column = visit[0],visit[1]
        map_copy[row] = map_copy[row][:column] + "#" + map_copy[row][column+1:]
        if not switch(map_copy,[],[]):
            ans +=1
print(ans)
input_data.close()