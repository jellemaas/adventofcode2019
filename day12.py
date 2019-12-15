def day_twelve_one():
	array = [[-14, -4, -11, 0, 0, 0], [-9, 6, -7, 0, 0, 0], [4, 1, 4, 0, 0, 0], [2, -14, -9, 0, 0, 0]]
	# array = [[-8, -10, 0,0,0,0],[5,5,10,0,0,0],[2,-7,3,0,0,0], [9,-8,-3,0,0,0]]
	# array = [[-1, 0, 2,0,0,0],[2,-10,-7,0,0,0],[4,-8,8,0,0,0], [3,5,-1,0,0,0]]

	i = 0
	while i < 1000:
		if array[0][0] > array[1][0]:
			array[0][3] += -1
			array[1][3] += 1
		if array[0][0] > array[2][0]:
			array[0][3] += -1
			array[2][3] += 1
		if array[0][0] > array[3][0]:
			array[0][3] += -1
			array[3][3] += 1

		if array[0][0] < array[1][0]:
			array[0][3] += 1
			array[1][3] += -1
		if array[0][0] < array[2][0]:
			array[0][3] += 1
			array[2][3] += -1
		if array[0][0] < array[3][0]:
			array[0][3] += 1
			array[3][3] += -1

		if array[1][0] > array[2][0]:
			array[1][3] += -1
			array[2][3] += 1
		if array[1][0] > array[3][0]:
			array[1][3] += -1
			array[3][3] += 1

		if array[2][0] > array[3][0]:
			array[2][3] += -1
			array[3][3] += 1

		if array[1][0] < array[2][0]:
			array[1][3] += 1
			array[2][3] += -1
		if array[1][0] < array[3][0]:
			array[1][3] += 1
			array[3][3] += -1

		if array[2][0] < array[3][0]:
			array[2][3] += 1
			array[3][3] += -1

		if array[0][1] > array[1][1]:
			array[0][4] += -1
			array[1][4] += 1
		if array[0][1] > array[2][1]:
			array[0][4] += -1
			array[2][4] += 1
		if array[0][1] > array[3][1]:
			array[0][4] += -1
			array[3][4] += 1

		if array[1][1] > array[2][1]:
			array[1][4] += -1
			array[2][4] += 1
		if array[1][1] > array[3][1]:
			array[1][4] += -1
			array[3][4] += 1

		if array[2][1] > array[3][1]:
			array[2][4] += -1
			array[3][4] += 1

		if array[0][1] < array[1][1]:
			array[0][4] += 1
			array[1][4] += -1
		if array[0][1] < array[2][1]:
			array[0][4] += 1
			array[2][4] += -1
		if array[0][1] < array[3][1]:
			array[0][4] += 1
			array[3][4] += -1

		if array[1][1] < array[2][1]:
			array[1][4] += 1
			array[2][4] += -1
		if array[1][1] < array[3][1]:
			array[1][4] += 1
			array[3][4] += -1

		if array[2][1] < array[3][1]:
			array[2][4] += 1
			array[3][4] += -1

		if array[0][2] > array[1][2]:
			array[0][5] += -1
			array[1][5] += 1
		if array[0][2] > array[2][2]:
			array[0][5] += -1
			array[2][5] += 1
		if array[0][2] > array[3][2]:
			array[0][5] += -1
			array[3][5] += 1

		if array[1][2] > array[2][2]:
			array[1][5] += -1
			array[2][5] += 1
		if array[1][2] > array[3][2]:
			array[1][5] += -1
			array[3][5] += 1

		if array[2][2] > array[3][2]:
			array[2][5] += -1
			array[3][5] += 1

		if array[0][2] < array[1][2]:
			array[0][5] += 1
			array[1][5] += -1
		if array[0][2] < array[2][2]:
			array[0][5] += 1
			array[2][5] += -1
		if array[0][2] < array[3][2]:
			array[0][5] += 1
			array[3][5] += -1

		if array[1][2] < array[2][2]:
			array[1][5] += 1
			array[2][5] += -1
		if array[1][2] < array[3][2]:
			array[1][5] += 1
			array[3][5] += -1

		if array[2][2] < array[3][2]:
			array[2][5] += 1
			array[3][5] += -1

		for number in array:
			number[0] = number[0] + number[3]
			number[1] = number[1] + number[4]
			number[2] = number[2] + number[5]

		print(array)
		i += 1

	answer = 0
	for number in array:
		answer = answer + (abs(number[0]) + abs(number[1]) + abs(number[2])) * (
					abs(number[3]) + abs(number[4]) + abs(number[5]))

	print(answer)
	return


# day_twelve_one()
