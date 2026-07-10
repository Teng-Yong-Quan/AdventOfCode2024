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
            walls.append([row,col*2])
            walls.append([row,col*2 + 1])
        elif map_[row][col] == '@':
            robot = [row,col*2]
        elif map_[row][col] =='O':
            boxes.append([[row,col*2],[row,col*2 +1]])

for mv in range(len(movement)):
    move = movement[mv]
    stack = []
    if move == '<':
        old_robot_r,old_robot_c = robot[0],robot[1]
        stack.append(robot)
        old_robot_c -= 1
        while True:
            if [[old_robot_r,old_robot_c-1],[old_robot_r,old_robot_c]] not in boxes:
                break
            else:
                stack.append(boxes.pop(boxes.index([[old_robot_r,old_robot_c-1],[old_robot_r,old_robot_c]])))
            old_robot_c -= 2
        if len(stack) > 1:    
            front_c = stack[-1][0][1]
            move_c = front_c - 1
            if [old_robot_r,move_c] not in walls:
                robot = stack.pop(0)
                robot = [robot[0],robot[1]-1]
                remain_len = len(stack)
                stack.append(robot)
                for i in range(remain_len):
                    pop_box = stack.pop(0)
                    left_left, left_right, right_left, right_right = pop_box[0][0], pop_box[0][1],pop_box[1][0],pop_box[1][1]
                    new_box = [[left_left,left_right-1],[right_left,right_right-1]]
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
            if [[old_robot_r,old_robot_c],[old_robot_r,old_robot_c+1]] not in boxes:
                break
            else:
                stack.append(boxes.pop(boxes.index([[old_robot_r,old_robot_c],[old_robot_r,old_robot_c+1]])))
            old_robot_c += 2
        if len(stack) > 1:     
            front_c = stack[-1][1][1]
            move_c = front_c + 1
            if [old_robot_r,move_c] not in walls:
                robot = stack.pop(0)
                robot = [robot[0],robot[1]+1]
                remain_len = len(stack)
                stack.append(robot)
                for i in range(remain_len):
                    pop_box = stack.pop(0)
                    left_left, left_right, right_left, right_right = pop_box[0][0], pop_box[0][1],pop_box[1][0],pop_box[1][1]
                    new_box = [[left_left,left_right+1],[right_left,right_right+1]]
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
        for box in range(len(boxes)):
            if [old_robot_r,old_robot_c] in boxes[box]:
                stack.append(boxes.pop(boxes.index(boxes[box])))
                break
        if len(stack) > 1:
            lower_c, upper_c = stack[-1][0][1], stack[-1][1][1] + 1
            processing = True
            while processing:
                old_robot_r -=1
                next_layer = []
                moving_right_c = lower_c
                while moving_right_c <= upper_c:
                    if [[old_robot_r,moving_right_c-1],[old_robot_r,moving_right_c]] in boxes:
                        next_layer.append(boxes.pop(boxes.index([[old_robot_r,moving_right_c-1],[old_robot_r,moving_right_c]])))
                    moving_right_c += 1
                if next_layer:
                   lower_c, upper_c = next_layer[0][0][1], next_layer[-1][1][1] + 1
                   while next_layer:
                      stack.append(next_layer.pop(0))
                else:
                    processing = False
                
        if len(stack) > 1:        
            got_wall = False
            counter = 1
            while counter < len(stack):
                left, right = stack[counter][0], stack[counter][1]
                check_left = [left[0]-1,left[1]]
                check_right = [right[0]-1,right[1]]
                if check_left in walls or check_right in walls:
                    got_wall = True
                    break
                counter += 1
            if not got_wall:
                robot = stack[0]
                robot = [robot[0]-1,robot[1]]
                stack[0] = robot
                for items in range(1,len(stack)):
                    item = stack[items]
                    stack[items] = [[item[0][0]-1,item[0][1]],[item[1][0]-1,item[1][1]]]
        else:
            robot = stack[0]
            if [robot[0]-1,robot[1]] not in walls:
                robot = [robot[0]-1,robot[1]]
                stack[0] = robot
                
    elif move == 'v':
        old_robot_r,old_robot_c = robot[0],robot[1]
        stack.append(robot)
        old_robot_r += 1
        for box in range(len(boxes)):
            if [old_robot_r,old_robot_c] in boxes[box]:
                stack.append(boxes.pop(boxes.index(boxes[box])))
                break
        if len(stack) > 1:
            lower_c, upper_c = stack[-1][0][1], stack[-1][1][1] + 1
            processing = True
            while processing:
                old_robot_r +=1
                next_layer = []
                moving_right_c = lower_c
                while moving_right_c <= upper_c:
                    if [[old_robot_r,moving_right_c-1],[old_robot_r,moving_right_c]] in boxes:
                        next_layer.append(boxes.pop(boxes.index([[old_robot_r,moving_right_c-1],[old_robot_r,moving_right_c]])))
                    moving_right_c += 1
                if next_layer:
                   lower_c, upper_c = next_layer[0][0][1], next_layer[-1][1][1] + 1
                   while next_layer:
                       stack.append(next_layer.pop(0))
                else:
                    processing = False
                
        if len(stack) > 1:        
            got_wall = False
            counter = 1
            while counter < len(stack):
                left, right = stack[counter][0], stack[counter][1]
                check_left = [left[0]+1,left[1]]
                check_right = [right[0]+1,right[1]]
                if check_left in walls or check_right in walls:
                    got_wall = True
                    break
                counter += 1
            if not got_wall:
                robot = stack[0]
                robot = [robot[0]+1,robot[1]]
                stack[0] = robot
                for items in range(1,len(stack)):
                    item = stack[items]
                    stack[items] = [[item[0][0]+1,item[0][1]],[item[1][0]+1,item[1][1]]]
        else:
            robot = stack[0]
            if [robot[0]+1,robot[1]] not in walls:
                robot = [robot[0]+1,robot[1]]
                stack[0] = robot
            
    robot = stack.pop(0)
    while stack:
        boxes.append(stack.pop(0))  
    

gps = 0    
for box in range(len(boxes)):
    box_r,box_c = boxes[box][0][0] , boxes[box][0][1]
    box_gps = box_r*100 + box_c
    gps += box_gps
print(gps)
input_data.close()