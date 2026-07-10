input_data = open('/home/advent-of-code-2024/Day12/advent_of_code_12.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]
plant_dic = {}
plant_neighbour_dic = {}
cost = 0
for i in range(len(input_data_lst)):
    for j in range(len(input_data_lst[0])):
        plant = input_data_lst[i][j]
        if plant not in plant_dic:
            plant_dic[plant] = []
            plant_neighbour_dic[plant] = []
        plant_dic[plant].append([i,j])

for k,v in plant_dic.items():
    while v:
        pos = v[0]
        neighbours = []
        prev_neighbours = []
        if pos not in neighbours:
            neighbours.append(pos)
            prev_neighbours.append(pos)
        while True:
            for nb in range(len(prev_neighbours)):
                neighbour = prev_neighbours[nb]
                r,c = neighbour[0] , neighbour[1]
                left,right,up,down = [r,c-1],[r,c+1],[r-1,c],[r+1,c]
                if left in v: 
                    if left not in neighbours:
                        neighbours.append(left)
                if right in v: 
                    if right not in neighbours:
                        neighbours.append(right)
                if up in v: 
                    if up not in neighbours:
                        neighbours.append(up)
                if down in v: 
                    if down not in neighbours:
                        neighbours.append(down)
            if prev_neighbours == neighbours:
                break
            prev_neighbours = neighbours.copy()
        for nb_2 in range(len(neighbours)):
            if neighbours[nb_2] in v:
                v.pop(v.index(neighbours[nb_2]))
        plant_neighbour_dic[k].append(neighbours)

for k,v in plant_neighbour_dic.items():            
    for nbs in range(len(v)):
        side = 0 
        lst = v[nbs]          
        if len(lst) == 1:
            side = 4
            added_cost = len(lst)*side
            cost += added_cost
        elif len(lst) == 2:
            side = 4
            added_cost = len(lst)*side
            cost += added_cost
        else:
            boundaries = []
            for ind in range(len(lst)):
                pos = lst[ind]
                pos_r, pos_c = lst[ind][0], lst[ind][1]
                left,right,up,down = [pos_r,pos_c-1],[pos_r,pos_c+1],[pos_r-1,pos_c],[pos_r+1,pos_c]
                if left not in lst:
                    boundaries.append([left,'l'])
                if right not in lst:
                    boundaries.append([right,'r'])
                if up not in lst:
                    boundaries.append([up,'u'])
                if down not in lst:
                    boundaries.append([down,'d'])
            sides_lst = []
            while boundaries:
                side_lst = []
                start = boundaries[0]
                boundaries.pop(boundaries.index(start))
                side_lst.append(start)
                boundary_r,boundary_c, direction = start[0][0],start[0][1], start[1]
                increase = True
                decrease = True
                boundary_r_increase, boundary_c_increase = boundary_r, boundary_c
                while increase:
                    if direction == 'l' or direction == 'r':
                        boundary_r_increase += 1
                        increment = [[boundary_r_increase, boundary_c],direction]
                        if increment in boundaries:
                            side_lst.append(increment)
                            boundaries.pop(boundaries.index(increment))
                        else:
                            break
                    elif direction == 'u' or direction == 'd':
                        boundary_c_increase += 1
                        increment = [[boundary_r, boundary_c_increase],direction]
                        if increment in boundaries:
                           side_lst.append(increment)
                           boundaries.pop(boundaries.index(increment))
                        else:
                            break
                boundary_r_decrease, boundary_c_decrease = boundary_r, boundary_c
                while decrease:
                    if direction == 'l' or direction == 'r':
                        boundary_r_decrease -= 1
                        decrement = [[boundary_r_decrease, boundary_c],direction]
                        if decrement in boundaries:
                           side_lst.append(decrement)
                           boundaries.pop(boundaries.index(decrement))
                        else:
                            break
                    elif direction == 'u' or direction == 'd':
                        boundary_c_decrease -= 1
                        decrement = [[boundary_r, boundary_c_decrease],direction]
                        if decrement in boundaries:
                           side_lst.append(decrement)
                           boundaries.pop(boundaries.index(decrement))
                        else:
                            break
                sides_lst.append(side_lst)
            added_cost = len(lst)*len(sides_lst)
            cost += added_cost
print(cost)
input_data.close()