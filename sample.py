side = [
    [ "Y", "O", "W" ],
    [ "R", "G", "O" ],
    [ "O", "O", "B" ]
]
new_side = [ [ 'X' for i in range(3) ] for i in range(3) ]
for row_idx, row in enumerate(side):
	for unit_idx, unit in enumerate(row):
		new_side[2-unit_idx][row_idx] = unit

print(new_side)