input_data = open('/home/advent-of-code-2024/Day18/advent_of_code_18.txt','r')
input_data_lst = [x.replace('\n','').split(',') for x in input_data] 

original_walls = [[int(y[0]),int(y[1])]for y in input_data_lst]
start,end = [0,0],[70,70]
end_lst = []

walls = original_walls[:1024]
pq = [(start,0)]
shortest_visited = []
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
    current_score = current_tup[1]
    n,s,e,w = [r-1,c],[r+1,c],[r,c+1],[r,c-1]
    new_score_n = current_score
    if n not in walls and 0 <= n[0] <= 70 and 0 <= n[1] <= 70:
        new_score_n +=1
        new_tup_n = (n,new_score_n)
        new_lst.append(new_tup_n)
                 
    new_score_s = current_score        
    if s not in walls and 0 <= s[0] <= 70 and 0 <= s[1] <= 70:
        new_score_s +=1
        new_tup_s = (s,new_score_s)
        new_lst.append(new_tup_s)
    
    new_score_e = current_score  
    if e not in walls and 0 <= e[0] <= 70 and 0 <= e[1] <= 70:
        new_score_e +=1
        new_tup_e = (e,new_score_e)
        new_lst.append(new_tup_e)
    
    new_score_w =  current_score  
    if w not in walls and 0 <= w[0] <= 70 and 0 <= w[1] <= 70:
        new_score_w +=1
        new_tup_w = (w,new_score_w)
        new_lst.append(new_tup_w)
    
    if new_lst:
        for tup in range(len(new_lst)):
            selected_tup = new_lst[tup]
            for short_tup in range(len(shortest_visited)):
                selected_short_tup = shortest_visited[short_tup]
                if selected_short_tup[0] == selected_tup[0] and selected_short_tup[1] < selected_tup[1]:
                    new_lst[tup] = 0
                    selected_tup = 0
                    break
            for pq_tup in range(len(pq)):
                selected_pq_tup = pq[pq_tup]
                if selected_tup:
                    if selected_pq_tup[0] == selected_tup[0] and selected_pq_tup[1] >= selected_tup[1]:
                        pq[pq_tup] = selected_tup
                        new_lst[tup] = 0
                        break
        #print(new_lst)
        new_lst = [x for x in new_lst if x]    
        pq.extend(new_lst)
    pq = sorted(pq,key = lambda t:t[1])
print(end_lst)
input_data.close()