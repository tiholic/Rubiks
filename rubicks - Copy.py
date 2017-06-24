import sys

def convertInputsToArray(input):
	arr = []
	sub_arr = []
	for i, color in enumerate(input):
		if i % 3 is 0:
			sub_arr = [ color ]
		else:
			sub_arr.append(color)
		if i % 3 is 2:
			arr.append(sub_arr)
	return arr


def getInputs():
	map = { };
	side = None
	for x in range(12):
	    data = input()
	    if x % 2 is 0:
	    	side = data
	    else:
	    	map[side] = convertInputsToArray(data)
	return map
	
def solve_rubicks(cube):
	rubicks_cube = RubicksCube(cube)
	rubicks_cube.solve()
	moves = rubicks_cube.get_moves()
	print(len(moves))
	print(', '.join(moves))


class RubicksCube:

	LEFT = 'LEFT'
	RIGHT = 'RIGHT'
	UP = 'UP'
	DOWN = 'DOWN'
	FRONT = 'FRONT'
	BACK = 'BACK'

	def __init__(self, cube):
		self.cube = cube
		self.cube_size = len(cube['LEFT'])
		self.moves = []

	def get_moves():
		return self.moves

	def solve():
		pass

	# @staticmethod
	# def get_adjacennt_sides(side):
	# 	if side == FRONT:
	# 		return [ LEFT, UP, RIGHT, DOWN ]
	# 	elif side == BACK:
	# 		return [ LEFT, DOWN, RIGHT, UP ]
	# 	elif side == UP:
	# 		return [ LEFT, BACK, RIGHT, FRONT ]
	# 	elif side == DOWN:
	# 		return [ LEFT, FRONT, RIGHT, BACK ]
	# 	elif side == RIGHT:
	# 		return [ FRONT, UP, BACK, DOWN ]
	# 	elif side == LEFT:
	# 		return [ FRONT, DOWN, BACK, UP ]

	# def get_adjacent_faces(side):
	# 	adjacent_faces = {}
	# 	for adjacent_side in RubicksCube.get_adjacennt_sides(side):
	# 		adjacent_faces[adjacent_side] = self.cube[adjacent_side]
	# 	return adjacent_faces

	def rotate(self, side, signature, adjacent_side_update_schema):

		signature = sys._getframe(1).f_code.co_name.title()

		size = self.cube_size
		face = self.cube[side]
		is_clockwise = len(signature)==1
		new_face = [ [ 'X' for i in range(self.cube_size) ] for i in range(self.cube_size) ]
		for row_idx, row in enumerate(face):
			for unit_idx, unit in enumerate(row):
				if is_clockwise:
					new_face[unit_idx][self.cube_size-1-row_idx] = unit
				else:
					new_face[self.cube_size-1-unit_idx][row_idx] = unit
		self.cube[side] = new_face
		self.update_adjacent_faces(adjacent_side_update_schema)
		self.moves.append(signature)

	# def rotate_clokwise(self, side, adjacent_side_update_schema):
	# 	self.rotate(side, True, adjacent_side_update_schema)

	# def rotate_anti_clockwise(self, side, adjacent_side_update_schema):
	# 	self.rotate(side, False, adjacent_side_update_schema)

	def shift_left_lane(self, side, moment):
		pass

	def override_face_pattern(face, new_partial_face):
		new_face = [ [ 'X' for i in range(self.cube_size) ] for i in range(self.cube_size) ]
		for row_idx, row in enumerate(face):
			for unit_idx, unit in enumerate(row):
				new_face[row_idx][unit_idx] = unit

		for position, new_unit in new_partial_face.items():
			new_face[position[0], position[1]] = unit

		return new_face

	def update_adjacent_face(self, updating_side, update_by_side, schema):
		updating_face = self.cube[updating_side]
		update_by_face = self.cube[update_by_side]
		partial_face_schema = {}
		for destination, source in schema.items():
			partial_face_schema[destination] = update_by_face[source[0]][source[1]]
		new_face = override_face_pattern(updating_face, partial_face_schema)
		self.cube[updating_side] = new_face

	def update_adjacent_faces(self, master_schema):
		for conf in master_schema:
			update_adjacent_face(conf[0], conf[1], conf[2])

	def r(self):
		self.rotate(RIGHT, 'R', 
			(
				( FRONT, DOWN,  {
						(0, 2) : (0, 2),
						(1, 2) : (1, 2),
						(2, 2) : (2, 2)
					}
				),
				( UP, FRONT, {
						(0, 2) : (0, 2),
						(1, 2) : (1, 2),
						(2, 2) : (2, 2)
					}
				),
				( BACK, UP, {
						(0, 2) : (2, 2),
						(1, 2) : (1, 2),
						(2, 2) : (0, 2)
					}
				),
				( DOWN, BACK, {
						(0, 2) : (2, 2),
						(1, 2) : (1, 2),
						(2, 2) : (0, 2)
					}
				)
			)
		)
	def ri(self):
		self.rotate(RIGHT, False, 'Ri', 
			(
				( FRONT, UP,  {
						(0, 2) : (0, 2),
						(1, 2) : (1, 2),
						(2, 2) : (2, 2)
					}
				),
				( UP, BACK, {
						(0, 2) : (2, 2),
						(1, 2) : (1, 2),
						(2, 2) : (0, 2)
					}
				),
				( BACK, DOWN, {
						(0, 2) : (2, 2),
						(1, 2) : (1, 2),
						(2, 2) : (0, 2)
					}
				),
				( DOWN, FRONT, {
						(0, 2) : (0, 2),
						(1, 2) : (1, 2),
						(2, 2) : (2, 2)
					}
				)
			)
		)

	def l(self):
		self.rotate(LEFT, True, 'L'
			(
			)
		)

	def li(self):
		self.rotate_anti_clockwise(LEFT)
		moves.append('Li')
		self.rotate(LEFT, False, 'Li'
			(
			)
		)

	def b(self):
		self.rotate_clokwise(BACK)
		moves.append('B')

	def bi(self):
		self.rotate_anti_clockwise(BACK)
		moves.append('Bi')

	def d(self):
		self.rotate_clokwise(DOWN)
		moves.append('D')

	def di(self):
		self.rotate_anti_clockwise(DOWN)
		moves.append('Di')

	def f(self):
		self.rotate_clokwise(FRONT)
		moves.append('F')

	def fi(self):
		self.rotate_anti_clockwise(FRONT)
		moves.append('Fi')

	def u(self):
		self.rotate_clokwise(UP)
		moves.append('U')

	def ui(self):
		self.rotate_anti_clockwise(UP)
		moves.append('Ui')


cube = getInputs()
solve_rubicks(cube)