input_data = open('/home/advent-of-code-2024/Day14/advent_of_code_14.txt','r')
input_data_lst = [x.replace('\n','').split(' ') for x in input_data]            
pos_lst = []
velo_lst = []

for i in range(len(input_data_lst)):
    for j in range(len(input_data_lst[0])):
        string = input_data_lst[i][j]
        lst = []
        if string.startswith('p'):
            count = 0
            substring = ''
            while count < len(string):
                char = string[count]
                if char == ',':
                    lst.append(int(substring))
                    substring = ''
                if char.isdigit():
                    substring += char                
                count += 1
            lst.append(int(substring))
            pos_lst.append(lst)
        elif string.startswith('v'):
            count = 0
            substring = ''
            while count < len(string):
                char = string[count]
                if char == ',':
                    lst.append(int(substring))
                    substring = ''
                if char.isdigit():
                    substring += char                
                if char == '-':
                    substring += char
                count += 1
            lst.append(int(substring))
            velo_lst.append(lst)

#101 wide and 103 tall map
# test case is 11 wide and 7 tall map
    
wide_limit = 101
tall_limit = 103
counter = 0
while counter < 100:
    for robot in range(len(pos_lst)):
        velo = velo_lst[robot]
        old_pos = pos_lst[robot]
        new_pos = []
        old_pos_c, old_pos_r, velo_c,velo_r = old_pos[0], old_pos[1], velo[0], velo[1]
        new_pos_r = old_pos_r + velo_r
        new_pos_c = old_pos_c + velo_c
        if new_pos_c >= wide_limit:
            new_pos_c -= wide_limit
        elif new_pos_c < 0:
            new_pos_c += wide_limit
        if new_pos_r >= tall_limit:
            new_pos_r -= tall_limit
        elif new_pos_r < 0:
            new_pos_r += tall_limit
        new_pos.append(new_pos_c)
        new_pos.append(new_pos_r)
        old_pos = new_pos
        pos_lst[robot] = old_pos
    check_pos_lst = []
    for bot in pos_lst:
        if bot not in check_pos_lst:
            check_pos_lst.append(bot)
    counter+=1
    if check_pos_lst == pos_lst:
        break
    
quadrants = [[],[],[],[]]
middle_column, middle_row = (wide_limit-1)//2, (tall_limit-1)//2
for pos_ind in range(len(pos_lst)):
    pos_c, pos_r = pos_lst[pos_ind][0], pos_lst[pos_ind][1]
    if pos_c < middle_column and pos_r < middle_row:
        quadrants[0].append(pos_lst[pos_ind])
    if pos_c > middle_column and pos_r < middle_row:
        quadrants[1].append(pos_lst[pos_ind])
    if pos_c < middle_column and pos_r > middle_row:
        quadrants[2].append(pos_lst[pos_ind])
    if pos_c > middle_column and pos_r > middle_row:
        quadrants[3].append(pos_lst[pos_ind])

safety = 1
for quad in range(len(quadrants)):
    safety*=len(quadrants[quad])
print(safety)
input_data.close()