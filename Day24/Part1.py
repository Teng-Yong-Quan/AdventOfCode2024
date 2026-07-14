input_data = open('/home/advent-of-code-2024/Day24/advent_of_code_24.txt','r')
all_info = [z for z in input_data]
wires_dict = {y[0] : int(y[1]) for y in [x.replace('\n','').split(':') for x in all_info if ':' in x]}
other_wires = [x.replace('\n','') for x in all_info if '->' in x]
while other_wires:
	wire = other_wires.pop(0)
	expr, new_wire = wire.split(" -> ")
	left_wire, op, right_wire = expr.split()
	if left_wire in wires_dict and right_wire in wires_dict:
		if 'AND' == op:
			wires_dict[new_wire] = wires_dict[left_wire] & wires_dict[right_wire]
		elif 'OR' == op:
			wires_dict[new_wire] = wires_dict[left_wire] | wires_dict[right_wire]
		else:
			wires_dict[new_wire] = wires_dict[left_wire] ^ wires_dict[right_wire]
	else:
		other_wires.append(wire)
wires_dict = dict(sorted(wires_dict.items(), reverse=True))
binary_output = ''.join([str(v) for k,v in wires_dict.items() if k.startswith('z')])
ans = int(binary_output,2)
print(ans)
input_data.close()