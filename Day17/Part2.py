def dec_to_bin(num):
    return bin(num)[2:]

def bin_to_dec(num_str):
    string = str(num_str)
    num = 0
    while string:
        add_num = 0
        if int(string[0]):
            add_num = pow(2,len(string)-1)
        num += add_num
        string = string[1:]
    return num

def xor(a,b):
    bi_a = dec_to_bin(a)
    bi_b = dec_to_bin(b)
    if len(bi_a) > len(bi_b):
        bi_b = '0'*(len(bi_a)-len(bi_b)) + bi_b
    elif len(bi_a) < len(bi_b):
        bi_a = '0'*(len(bi_b)-len(bi_a)) + bi_a
    string = ''
    for i in range(len(bi_a)):
        if bi_a[i] == bi_b[i]:
            string += '0'
        elif bi_a[i] != bi_b[i]:
            string += '1'
    return bin_to_dec(string)

input_data = open('/home/advent-of-code-2024/Day17/advent_of_code_17.txt','r')
input_data_lst = [x.replace('\n','') for x in input_data] 

reg_A = int(''.join([x for x in input_data_lst[0] if x.isdigit()]))
reg_B = int(''.join([x for x in input_data_lst[1] if x.isdigit()]))
reg_C = int(''.join([x for x in input_data_lst[2] if x.isdigit()]))
program_lst = [int(x) for x in input_data_lst[4] if x.isdigit()]

stack = []
dead_end = []
reg_A = 0
stack.append(reg_A)
reg_A = stack[-1]

while len(stack) < len(program_lst) + 1:
    reg_A = stack[-1]
    reg_A*= 8
    lst = []
    output = []
    org_reg_A = reg_A
    for i in range(reg_A, reg_A+8):
        lst.append(i)
    #print(lst)
    for num in lst:
        reg_A = num
        combo_operand = {'0':0,'1':1,'2':2,'3':3,'4':reg_A,'5':reg_B,'6':reg_C}
        index = 0
        while index < len(program_lst):
            opcode = program_lst[index]
            if opcode == 0:
                combo_index = index + 1
                selected_combo_operand = str(program_lst[combo_index])
                val = combo_operand[selected_combo_operand]
                reg_A = int(reg_A/(2**val))
                combo_operand['4'] = reg_A
            elif opcode == 1:
                reg_B = xor(reg_B,program_lst[index+1])
                combo_operand['5'] = reg_B
            elif opcode == 2:
                combo_index = index + 1
                selected_combo_operand = str(program_lst[combo_index])
                val = combo_operand[selected_combo_operand]
                reg_B = val%8
                combo_operand['5'] = reg_B
            elif opcode == 3:
                break
            elif opcode == 4:
                reg_B = xor(reg_B,reg_C)
                combo_operand['5'] = reg_B
            elif opcode == 5:
                combo_index = index + 1
                selected_combo_operand = str(program_lst[combo_index])
                val = combo_operand[selected_combo_operand]
                output.append(val%8)
            elif opcode == 6:
                combo_index = index + 1
                selected_combo_operand = str(program_lst[combo_index])
                val = combo_operand[selected_combo_operand]
                reg_B = int(reg_A/(2**val))
                combo_operand['5'] = reg_B
            elif opcode == 7:
                combo_index = index + 1
                selected_combo_operand = str(program_lst[combo_index])
                val = combo_operand[selected_combo_operand]
                reg_C = int(reg_A/(2**val))
                combo_operand['6'] = reg_C
            index +=2
    correct = program_lst[len(program_lst)-len(stack)]
    check_av_correct = []
    #print(output)
    if correct in output:
        for i in range(len(output)):
            if output[i] == correct:
                if org_reg_A + i not in stack and org_reg_A + i not in dead_end:
                    check_av_correct.append(org_reg_A+i)
    if not check_av_correct:
        dead_end.append(stack.pop())
    else:
        reg_A = check_av_correct[0]
        stack.append(reg_A)
print(stack[-1])
input_data.close()
