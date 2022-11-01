print("X Y Z F")
for x in range(0, 2):
	for y in range(0, 2):
		for z in range(0, 2):
			if (not(x or y or z)) == ((not x) and (not y) and (not z)):
				f = 1
			else:
				f = 0
			print(x, y, z, f)
