input_data = open('/home/advent-of-code-2024/Day13/advent_of_code_13.txt','r')
input_data_lst = [x.replace('\n','').replace(':','').replace(',','').split() for x in input_data]            
A = []
B = []
prize = []
for index in range(len(input_data_lst)):
    if 'A' in input_data_lst[index]:
        button_A = []
        for string_A in range(len(input_data_lst[index])):
            if input_data_lst[index][string_A].startswith('X'):
                button_A.append(int(input_data_lst[index][string_A][2:]))
            elif input_data_lst[index][string_A].startswith('Y'):
                button_A.append(int(input_data_lst[index][string_A][2:]))
        A.append(button_A)
    elif 'B' in input_data_lst[index]:
        button_B = []
        for string_B in range(len(input_data_lst[index])):
            if input_data_lst[index][string_B].startswith('X'):
                button_B.append(int(input_data_lst[index][string_B][2:]))
            elif input_data_lst[index][string_B].startswith('Y'):
                button_B.append(int(input_data_lst[index][string_B][2:]))
        B.append(button_B)
    elif 'Prize' in input_data_lst[index]:
        prize_P = []
        for string_P in range(len(input_data_lst[index])):
            if input_data_lst[index][string_P].startswith('X'):
                prize_P.append(int(input_data_lst[index][string_P][2:]))
            elif input_data_lst[index][string_P].startswith('Y'):
                prize_P.append(int(input_data_lst[index][string_P][2:]))
        prize.append(prize_P)
# 10000000000000        

prizes_won = []
for i in range(len(A)):
    win_prize = []
    unknown_a,unknown_b = 0,0
    x_a, y_a, x_b, y_b, prize_x, prize_y = A[i][0], A[i][1], B[i][0], B[i][1], prize[i][0], prize[i][1]
    mul_x_b,mul_y_b = x_b, y_b
    x_a *= mul_y_b
    x_b *= mul_y_b
    prize_x *= mul_y_b
    y_a *= mul_x_b
    y_b *= mul_x_b
    prize_y *= mul_x_b
    unknown_a = (prize_x - prize_y)//(x_a-y_a)
    unknown_b = (prize_y - unknown_a*y_a)/y_b
    remainder_a, remainder_b = (prize_x - prize_y)%(x_a-y_a), (prize_y - unknown_a*y_a)%y_b
    if not remainder_a and not remainder_b:
        win_prize.append([int(unknown_a),int(unknown_b)])
    prizes_won.append(win_prize)        
tokens = 0
for p_won in range(len(prizes_won)):
    tokens_lst = []    
    if prizes_won[p_won]:
        for combo in range(len(prizes_won[p_won])):
            button_combo = prizes_won[p_won][combo]
            tokens_spent = button_combo[0]*3 + button_combo[1]
            tokens_lst.append(tokens_spent)
        tokens += min(tokens_lst)
print(tokens)
input_data.close()