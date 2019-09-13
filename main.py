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
x = len(board[0])
y = len(board)
heurstic = False

#Print board
for row in board:
	row_string = ""
	for num in row:
		row_string += num + " "
	print(row_string)

#This program is tested with the board above, but it should work on any N*N board
def program():
	pass

#Makes a choice for the best move
def move():
	pass

#Finds the possible new states of the board
def find_new_states():
	pass

#Parses the board to a string to be compared
def parse_board():
	pass

#Checks the current state agains all the visited states to see if a dead-end is reached
def check_visited():
	pass

#Uses heurstic values to find the best ways
def find_best_state():
	pass

