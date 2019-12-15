def split_to_array(string1):
	return string1.split(",")


def split_to_letters_and_numbers(array):
	wiredletter = []
	wirednumber = []

	for i in array:
		lijstje = list(i)
		if lijstje[0] == "R":
			splittedR = i.split("R")
			splittedU = []
			splittedL = []
			splittedD = []
		elif lijstje[0] == "D":
			splittedD = i.split("D")
			splittedU = []
			splittedL = []
			splittedR = []
		elif lijstje[0] == "L":
			splittedL = i.split("L")
			splittedU = []
			splittedR = []
			splittedD = []
		elif lijstje[0] == "U":
			splittedU = i.split("U")
			splittedR = []
			splittedL = []
			splittedD = []
		for j in splittedR:
			wiredletter.append("R")
			wirednumber.append(splittedR[1])
			splittedR.remove(splittedR[1])
			splittedR.remove("")
		for u in splittedD:
			wiredletter.append("D")
			wirednumber.append(splittedD[1])
			splittedD.remove(splittedD[1])
			splittedD.remove("")
		for v in splittedL:
			wiredletter.append("L")
			wirednumber.append(splittedL[1])
			splittedL.remove(splittedL[1])
			splittedL.remove("")
		for w in splittedU:
			wiredletter.append("U")
			wirednumber.append(splittedU[1])
			splittedU.remove(splittedU[1])
			splittedU.remove("")

	return wiredletter, wirednumber


def get_all_coordinates(wiredletter, wirednumber):
	j = 0
	k = 0
	l = 0
	coordinates = [[0, 0]]

	# print(len(wiredletter))
	for i in wiredletter:
		if i == "R":
			while l < int(wirednumber[j]):
				lijstje = [int(coordinates[k][0]) + 1, int(coordinates[k][1])]
				coordinates.append(lijstje)

				k += 1
				l += 1
		elif i == "L":
			while l < int(wirednumber[j]):
				lijstje = [int(coordinates[k][0]) - 1, int(coordinates[k][1])]
				coordinates.append(lijstje)
				k += 1
				l += 1
		elif i == "U":
			while l < int(wirednumber[j]):
				lijstje = [int(coordinates[k][0]), int(coordinates[k][1] + 1)]
				coordinates.append(lijstje)
				k += 1
				l += 1
		elif i == "D":
			while l < int(wirednumber[j]):
				lijstje = [int(coordinates[k][0]), int(coordinates[k][1]) - 1]
				coordinates.append(lijstje)
				k += 1
				l += 1
		l = 0
		j += 1
	return coordinates


def get_crossing(coordinates1, coordinates2):
	j = 0
	crossing = []
	# do not sort if you want the distance
	# coordinates2.sort()
	# coordinates1.sort()
	for coordinate1 in coordinates1:
		for coordinate2 in coordinates2:
			j += 1
			# print(j)
			# if j % 1000000000 == 0:
			#   print("miljard verder")
			# print(j + "out of the "  + int(len(coordinates1)*len(coordinates2)))
			if coordinate2 == coordinate1:
				crossing.append(coordinate1)
				# print(coordinate2)
	# print(crossing)
	crossing.remove(crossing[0])
	# print(crossing)
	return crossing


def get_distance(crossing, coordinates):
	distancearray = []
	for crossingdistance in crossing:
		distance = 0
		for amount in coordinates:
			distance += 1
			if amount == crossingdistance:
				distancearray.append(distance)
	return distancearray


def get_minimum_crossing_distance(crossing):
	closest = []
	for numbers in crossing:
		summation = abs(numbers[0]) + abs(numbers[1])
		closest.append(summation)

	minimum = closest[0]
	for manhattan in closest:
		if manhattan < minimum:
			minimum = manhattan

	return minimum


def get_min_to_crossing(array, array2):
	i = 0
	minimum = array[0] + array2[0]
	while i < len(array) - 1:
		if (array[i] + array2[i]) < minimum:
			minimum = (array[i] + array2[i])
		i += 1
	return (minimum - 2)


def day_three_one(string1, string2):
	wire1 = split_to_array(string1)
	wire2 = split_to_array(string2)

	wiredletter1, wirednumber1 = split_to_letters_and_numbers(wire1)
	wiredletter2, wirednumber2 = split_to_letters_and_numbers(wire2)

	coordinates1 = get_all_coordinates(wiredletter1, wirednumber1)
	coordinates2 = get_all_coordinates(wiredletter2, wirednumber2)

	crossing = get_crossing(coordinates1, coordinates2)

	answer = get_minimum_crossing_distance(crossing)

	print(answer)


def day_three_two(string1, string2):
	wire1 = split_to_array(string1)
	wire2 = split_to_array(string2)

	wiredletter1, wirednumber1 = split_to_letters_and_numbers(wire1)
	wiredletter2, wirednumber2 = split_to_letters_and_numbers(wire2)

	coordinates1 = get_all_coordinates(wiredletter1, wirednumber1)
	coordinates2 = get_all_coordinates(wiredletter2, wirednumber2)

	crossing = get_crossing(coordinates1, coordinates2)

	distance1 = get_distance(crossing, coordinates1)
	distance2 = get_distance(crossing, coordinates2)

	answer = get_min_to_crossing(distance1, distance2)

	print(answer)


# day_three_one("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
# day_three_two("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
