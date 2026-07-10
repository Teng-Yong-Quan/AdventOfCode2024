input_data = open('/home/advent-of-code-2024/Day16/advent_of_code_16.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data]  

route = []
start = None
end = None
for i in range(len(input_data_lst)):
    for j in range(len(input_data_lst[0])):
        string = input_data_lst[i][j]
        if string == '.':
            route.append((i,j))
        elif string == 'E':
            end = (i,j)
            route.append((i,j))
        elif string == 'S':
            start = (i,j)
        
shortest_visited = []
end_lst = []
pq = [(start,'e',0)]
prev_shortest_visited = []

while pq:
    new_lst = []
    current_tup = pq.pop(0)
    current_pos = current_tup[0]
    if current_pos == end:
        shortest_visited.append(current_tup)
        end_lst.append(current_tup)
        break
    if current_tup not in shortest_visited:
        shortest_visited.append(current_tup)
    r, c = current_pos[0],current_pos[1]
    current_direction = current_tup[1]
    current_score = current_tup[2]
    n,s,e,w = (r-1,c),(r+1,c),(r,c+1),(r,c-1)
    new_direction_n, new_score_n = current_direction, current_score
    if n in route:
        if new_direction_n != 's':
            if new_direction_n == 'e' or new_direction_n == 'w':
                new_score_n += 1000
            new_direction_n = 'n'
            new_score_n +=1
            new_tup_n = (n,new_direction_n,new_score_n)
            new_lst.append(new_tup_n)
                 
    new_direction_s, new_score_s = current_direction, current_score        
    if s in route:
        if new_direction_s != 'n':
            if new_direction_s == 'e' or new_direction_s == 'w':
                new_score_s += 1000
            new_direction_s = 's'
            new_score_s +=1
            new_tup_s = (s,new_direction_s,new_score_s)
            new_lst.append(new_tup_s)
    
    new_direction_e, new_score_e = current_direction, current_score  
    if e in route:
        if new_direction_e != 'w':
            if new_direction_e == 'n' or new_direction_e == 's':
                new_score_e += 1000
            new_direction_e = 'e'
            new_score_e +=1
            new_tup_e = (e,new_direction_e,new_score_e)
            new_lst.append(new_tup_e)
    
    new_direction_w, new_score_w = current_direction, current_score  
    if w in route:
        if new_direction_w != 'e':
            if new_direction_w == 'n' or new_direction_w == 's':
                new_score_w += 1000
            new_direction_w = 'w'
            new_score_w +=1
            new_tup_w = (w,new_direction_w,new_score_w)
            new_lst.append(new_tup_w)
    
    if new_lst:
        for tup in range(len(new_lst)):
            selected_tup = new_lst[tup]
            for short_tup in range(len(shortest_visited)):
                selected_short_tup = shortest_visited[short_tup]
                if selected_short_tup[0] == selected_tup[0] and selected_short_tup[1] == selected_tup[1] and selected_short_tup[2] < selected_tup[2]:
                    new_lst[tup] = 0
                    selected_tup = 0
                    break
            for pq_tup in range(len(pq)):
                selected_pq_tup = pq[pq_tup]
                if selected_tup:
                    if selected_pq_tup[0] == selected_tup[0] and selected_pq_tup[1] == selected_tup[1] and selected_pq_tup[2] >= selected_tup[2]:
                        pq[pq_tup] = selected_tup
                        new_lst[tup] = 0
                        break

        new_lst = [x for x in new_lst if x]    
        pq.extend(new_lst)
    pq = sorted(pq,key = lambda t:t[0][0])
    pq = sorted(pq, key = lambda t:t[2])
    #print(pq)
    #print()
  
optimum_paths = shortest_visited

stack = []
visited = []
dead_end = []
stack.append((start,'e',0))
score = 0
while stack:
    current = stack[-1]
    if current[0] == end:
        visited.append(stack.pop())
        continue
    r,c = current[0][0], current[0][1]
    n,s,e,w = (r-1,c), (r+1,c), (r,c+1), (r,c-1)
    current_direction = current[1]
    score = current[2]
    n_score, s_score, e_score, w_score = 0,0,0,0
    n_,s_,e_,w_ = (),(),(),()
    if current_direction == 'n':
        n_score = score + 1
        e_score = score + 1001
        w_score = score + 1001
        n_ = (n,current_direction,n_score)
        e_ = (e,'e',e_score)
        w_ = (w,'w',w_score)
    elif current_direction == 's':
        s_score = score + 1
        e_score = score + 1001
        w_score = score + 1001
        s_ = (s,current_direction,s_score)
        e_ = (e,'e',e_score)
        w_ = (w,'w',w_score)
    elif current_direction == 'e':
        e_score = score + 1
        n_score = score + 1001
        s_score = score + 1001
        e_ = (e,current_direction,e_score)
        n_ = (n,'n',n_score)
        s_ = (s,'s',s_score)
    elif current_direction == 'w':
        w_score = score + 1
        n_score = score + 1001
        s_score = score + 1001
        w_ = (w,current_direction,w_score)
        n_ = (n,'n',n_score)
        s_ = (s,'s',s_score)
    new_lst = []
    #print(n_,s_,e_,w_)
    for i in range(len(optimum_paths)):
        if n_ == optimum_paths[i] and n_ not in stack:
            new_lst.append(optimum_paths[i])
        if s_ == optimum_paths[i] and s_ not in stack:
            new_lst.append(optimum_paths[i])
        if e_ == optimum_paths[i] and e_ not in stack:
            new_lst.append(optimum_paths[i])
        if w_ == optimum_paths[i] and w_ not in stack:
            new_lst.append(optimum_paths[i])
    
    #print(new_lst)
    #print()
    if not new_lst and current[0] != end:
        dead_end.append(stack.pop())
        continue
    else:
        check_dead_end = [x for x in new_lst if x in dead_end]
        if check_dead_end == new_lst:
            dead_end.append(stack.pop())
            continue
        
    if new_lst:
        for new in range(len(new_lst)):
            if new_lst[new] in stack or new_lst[new] in visited or new_lst[new] in dead_end:
                new_lst[new] = 0
        new_lst = [x for x in new_lst if x]
    if new_lst:
        stack.append(new_lst[0])
    else:
        visited.append(stack.pop())
    
final_visited = set([x[0] for x in visited])
print(len(final_visited))
input_data.close()