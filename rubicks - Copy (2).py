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
	    	side = data[0]
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

	LEFT = 'L'
	RIGHT = 'R'
	UP = 'U'
	DOWN = 'D'
	FRONT = 'F'
	BACK = 'B'

	def __init__(self, cube):
		self.cube = cube
		self.moves = []

	def get_moves():
		return self.moves

	def solve():
		pass

	def override_face_pattern(face, new_partial_face):
		size = len(face)
		new_face = [ [ 'X' for i in range(size) ] for i in range(size) ]
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

	def rotate(self, adjacent_side_update_schema):
		signature = sys._getframe(1).f_code.co_name.title()
		side = signature[0]
		face = self.cube[side]
		size = len(face)
		is_clockwise = len(signature)==1
		new_face = [ [ 'X' for i in range(size) ] for i in range(size) ]
		for row_idx, row in enumerate(face):
			for unit_idx, unit in enumerate(row):
				if is_clockwise:
					new_face[unit_idx][size-1-row_idx] = unit
				else:
					new_face[size-1-unit_idx][row_idx] = unit
		self.cube[side] = new_face
		self.update_adjacent_faces(adjacent_side_update_schema)
		self.moves.append(signature)

	def r(self):
		self.rotate(
			(
				( (FRONT, DOWN, BACK, UP),
				  (
						( (0, 2), (0, 2), (2, 0), (0, 2)),
						( (1, 2), (1, 2), (1, 0), (1, 2)),
						( (2, 2) : (2, 2), (0, 0), (2, 2))
					)
				),
				# ( DOWN, BACK, {
				# 		(0, 2) : (2, 0),
				# 		(1, 2) : (1, 0),
				# 		(2, 2) : (0, 0)
				# 	}
				# ),
				# ( BACK, UP, {
				# 		(2, 0) : (0, 2),
				# 		(1, 0) : (1, 2),
				# 		(0, 0) : (2, 2)
				# 	}
				# ),
				# ( UP, FRONT, {
				# 		(0, 2) : (0, 2),
				# 		(1, 2) : (1, 2),
				# 		(2, 2) : (2, 2)
				# 	}
				# )
			)
		)
	def ri(self):
		self.rotate(
			(
				( FRONT, UP,  {
						(0, 2) : (0, 2),
						(1, 2) : (1, 2),
						(2, 2) : (2, 2)
					}
				),
				( UP, BACK, {
						(0, 2) : (2, 0),
						(1, 2) : (1, 0),
						(2, 2) : (0, 0)
					}
				),
				( BACK, DOWN, {
						(0, 0) : (2, 2),
						(1, 0) : (1, 2),
						(2, 0) : (0, 2)
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
		self.rotate(
			(
				( FRONT, UP,  {
						(0, 0) : (0, 0),
						(1, 0) : (1, 0),
						(2, 0) : (2, 0)
					}
				),
				( UP, BACK, {
						(0, 0) : (2, 2),
						(1, 0) : (1, 2),
						(2, 0) : (0, 2)
					}
				),
				( BACK, DOWN, {
						(0, 2) : (2, 0),
						(1, 2) : (1, 0),
						(2, 2) : (0, 0)
					}
				),
				( DOWN, FRONT, {
						(0, 0) : (0, 0),
						(1, 0) : (1, 0),
						(2, 0) : (2, 0)
					}
				)
			)
		)

	def li(self):
		self.rotate(
			(
				( FRONT, DOWN,  {
						(0, 0) : (0, 0),
						(1, 0) : (1, 0),
						(2, 0) : (2, 0)
					}
				),
				( UP, FRONT, {
						(0, 0) : (0, 0),
						(1, 0) : (1, 0),
						(2, 0) : (2, 0)
					}
				),
				( BACK, UP, {
						(0, 2) : (2, 0),
						(1, 2) : (1, 0),
						(2, 2) : (0, 0)
					}
				),
				( DOWN, BACK, {
						(0, 0) : (2, 2),
						(1, 0) : (1, 2),
						(2, 0) : (0, 2)
					}
				)
			)
		)

	def b(self):
		self.rotate(
			(
				( LEFT, UP,  {
						(0, 0) : (0, 0),
						(1, 0) : (0, 1),
						(2, 0) : (0, 2)
					}
				),
				( DOWN, LEFT, {
						(0, 0) : (0, 0),
						(1, 0) : (1, 0),
						(2, 0) : (2, 0)
					}
				),
				( RIGHT, DOWN, {
						(0, 2) : (2, 0),
						(1, 2) : (1, 0),
						(2, 2) : (0, 0)
					}
				),
				( UP, RIGHT, {
						(0, 0) : (2, 2),
						(1, 0) : (1, 2),
						(2, 0) : (0, 2)
					}
				)
			)
		)

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