input_data = open('/home/advent-of-code-2024/Day15/advent_of_code_15.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]            

robot = None
walls = []
boxes = []
move = ''

map_ = []
movement = ''
for i in range(len(input_data_lst)):
    if input_data_lst[i]:
        if input_data_lst[i][0] == '#':
            map_.append(input_data_lst[i])
        elif input_data_lst[i][0] != '#':
            movement += input_data_lst[i]
    
for row in range(len(map_)):
    for col in range(len(map_[0])):
        if map_[row][col] =='#':
            walls.append([row,col])
        elif map_[row][col] == '@':
            robot = [row,col]
        elif map_[row][col] =='O':
            boxes.append([row,col])

for mv in range(len(movement)):
    move = movement[mv]
    stack = []
    if move == '<':
        old_robot_r,old_robot_c = robot[0],robot[1]
        stack.append(robot)
        old_robot_c -= 1
        while True:
            if [old_robot_r,old_robot_c] not in boxes:
                break
            else:
                stack.append(boxes.pop(boxes.index([old_robot_r,old_robot_c])))
            old_robot_c -= 1
        if len(stack) > 1:    
            front_c = stack[-1][1]
            move_c = front_c - 1
            if [old_robot_r,move_c] not in walls:
                robot = stack.pop(0)
                robot = [robot[0],robot[1]-1]
                remain_len = len(stack)
                stack.append(robot)
                for i in range(remain_len):
                    pop_box = stack.pop(0)
                    new_box = [pop_box[0],pop_box[1]-1]
                    stack.append(new_box)
        else:
            front_c = stack[-1][1]
            move_c = front_c - 1
            if [old_robot_r,move_c] not in walls:
                robot = stack.pop(0)
                robot = [old_robot_r,move_c]
                stack.append(robot)
            
    elif move == '>':
        old_robot_r,old_robot_c = robot[0],robot[1]
        stack.append(robot)
        old_robot_c += 1
        while True:
            if [old_robot_r,old_robot_c] not in boxes:
                break
            else:
                stack.append(boxes.pop(boxes.index([old_robot_r,old_robot_c])))
            old_robot_c += 1
        if len(stack) > 1:     
            front_c = stack[-1][1]
            move_c = front_c + 1
            if [old_robot_r,move_c] not in walls:
                robot = stack.pop(0)
                robot = [robot[0],robot[1]+1]
                remain_len = len(stack)
                stack.append(robot)
                for i in range(remain_len):
                    pop_box = stack.pop(0)
                    new_box = [pop_box[0],pop_box[1]+1]
                    stack.append(new_box)
        else:
            front_c = stack[-1][1]
            move_c = front_c + 1
            if [old_robot_r,move_c] not in walls:
                robot = stack.pop(0)
                robot = [old_robot_r,move_c]
                stack.append(robot)
                
    elif move == '^':
        old_robot_r,old_robot_c = robot[0],robot[1]
        stack.append(robot)
        old_robot_r -= 1
        while True:
            if [old_robot_r,old_robot_c] in boxes:
                stack.append(boxes.pop(boxes.index([old_robot_r,old_robot_c])))
            else:
                break
            old_robot_r -= 1
        if len(stack) > 1:    
            front_r = stack[-1][0]
            move_r = front_r - 1
            if [move_r,old_robot_c] not in walls:
                robot = stack.pop(0)
                robot = [robot[0]-1,robot[1]]
                remain_len = len(stack)
                stack.append(robot)
                for i in range(remain_len):
                    pop_box = stack.pop(0)
                    new_box = [pop_box[0]-1,pop_box[1]]
                    stack.append(new_box)
        else:
            front_r = stack[-1][0]
            move_r = front_r - 1
            if [move_r,old_robot_c] not in walls:
                robot = stack.pop(0)
                robot = [move_r,old_robot_c]
                stack.append(robot)
                
    elif move == 'v':
        old_robot_r,old_robot_c = robot[0],robot[1]
        stack.append(robot)
        old_robot_r += 1
        while True:
            if [old_robot_r,old_robot_c] in boxes:
                stack.append(boxes.pop(boxes.index([old_robot_r,old_robot_c])))
            else:
                break
            old_robot_r += 1
        if len(stack) > 1:    
            front_r = stack[-1][0]
            move_r = front_r + 1
            if [move_r,old_robot_c] not in walls:
                robot = stack.pop(0)
                robot = [robot[0]+1,robot[1]]
                remain_len = len(stack)
                stack.append(robot)
                for i in range(remain_len):
                    pop_box = stack.pop(0)
                    new_box = [pop_box[0]+1,pop_box[1]]
                    stack.append(new_box)
        else:
            front_r = stack[-1][0]
            move_r = front_r + 1
            if [move_r,old_robot_c] not in walls:
                robot = stack.pop(0)
                robot = [move_r,old_robot_c]
                stack.append(robot)
            
    robot = stack.pop(0)
    while stack:
        boxes.append(stack.pop(0))  
    
gps = 0    
for box in range(len(boxes)):
    box_r,box_c = boxes[box][0] , boxes[box][1]
    box_gps = box_r*100 + box_c
    gps += box_gps
print(gps)
input_data.close()