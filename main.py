import copy
#Setup starting position
# 0 5 2
# 1 4 3
# 7 8 6
# This position is 10 moves away from the desired position
#Desired position
# 1 2 3
# 4 5 6
# 7 8 0
board = [['0','5','2'],['1','4','3'],['7','8','6']]
des_board = [['1','2','3'],['4','5','6'],['7','8','0']]
x = len(board[0])
y = len(board)
heurstic = False

def print_board(board_to_print):
	#Print board
	for row in board_to_print:
		row_string = ""
		for num in row:
			row_string += num + " "
		print(row_string)
	print("---")

print_board(board)

#This program is tested with the board above, but it should work on any N*N board
def program():
	print(move(board))

#Makes a choice for the best move
def move(board_state_current, visited=[]):
	#Append the current state to state's visited
	visited.append(parse_board(board_state_current))

	#Check if the desired board state is reached
	if parse_board(board_state_current) == parse_board(des_board):
		return [visited]

	paths = []

	#Start the recursive search
	for child in find_new_states(board_state_current):
		if child not in visited:
			new_paths = move(child, visited)
			for new_path in new_paths:
				paths.append(new_path)
	return paths

#Finds the possible new states of the board
def find_new_states(board_state_current,visited=[]):
	zero_pos = []
	#Find the position of 0
	for row in range(x):
		for col in range(y):
			if board_state_current[row][col] == "0":
				zero_pos = [row,col]
				break

	up,down,left,right = -1,-1,-1,-1
	#Look 4 ways, if a way goes beyond board limits it stays a -1
	if val_num(zero_pos[0]-1,x): #Because the board is always a square it doesn't matter wether x or y is the limit
		up = [zero_pos[0]-1,zero_pos[1]]

	if val_num(zero_pos[0]+1,x):
		down = [zero_pos[0]+1,zero_pos[1]]

	if val_num(zero_pos[1]-1,x):
		left = [zero_pos[0],zero_pos[1]-1]

	if val_num(zero_pos[1]+1,x):
		right = [zero_pos[0],zero_pos[1]+1]

	#For every way get the new board state if the number and 0 would be switched
	#If a way is invalid (-1) the state would be False
	print("Look around results:")
	print("Up:",up,"Right:",right,"Down:",down,"Left:",left)
	state1 = switch_num(zero_pos,up,board_state_current)
	state2 = switch_num(zero_pos,down,board_state_current)
	state3 = switch_num(zero_pos,right,board_state_current)
	state4 = switch_num(zero_pos,left,board_state_current)


	#If a state is not False, add it to new_states
	new_states = []
	print("posible new states:")
	if state1: 
		print_board(state1)
		new_states.append(state1)
	if state2: 
		print_board(state2)
		new_states.append(state2)
	if state3: 
		print_board(state3)
		new_states.append(state3)
	if state4: 
		print_board(state4)
		new_states.append(state4)
	return new_states

#Switches the 0 with an adjecent number on the board (sliding)
def switch_num(zero_pos,num_pos,old_board):
	if num_pos == -1: #This pos is not valid
		return False
	new_board = copy.deepcopy(old_board)
	temp = old_board[zero_pos[0]][zero_pos[1]]
	new_board[zero_pos[0]][zero_pos[1]] = old_board[num_pos[0]][num_pos[1]] #Put the number in the 0 position
	new_board[num_pos[0]][num_pos[1]] = temp #Put the 0 in the number position
	return new_board

#Validates wether a number is inside the board limits
def val_num(num, lim):
	if num < 0:
		return False
	elif num == lim:
		return False
	return True

#Parses the board to a string to be compared
def parse_board(board_state):
	board_str = ""
	for row in board_state:
		for num in row:
			board_str += num
	return board_str

#Checks the current state agains all the visited states to see if a dead-end is reached
def check_visited(new_state):
	for state in visited:
		if state == new_state:
			return False
	return True

#Uses heurstic values to find the best ways
def find_best_state():
	pass

program()