# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_matrix.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 14:31:14 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/13 15:19:29 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	if (len(sys.argv) != 3):
		raise Exception("Error! Usage: python3 ft_matrix.py <n> <m>")
	n = int(sys.argv[1])
	m = int(sys.argv[2])
	matrix = []
	
	# Filling matrix through input
	for i in range(n):
		row = []
		for j in range(m):
			value = float(input(f"Insert the element in position ({i}, {j}): "))
			row.append(value)
		matrix.append(row)
	
	# Print matrix
	print("The inserted matrix is:")
	for i in range(n):
		print(matrix[i])
	
	# Sum of rows
	sum = [0] * n
	for y in range(m):
		for x in range(n):
			sum[x] += matrix[x][y]
	print(f"The sum over rows is:\n{sum}")
	
	# Sum of columns
	sum = [0] * m
	for x in range(n):
		for y in range(m):
			sum[y] += matrix[x][y]
	print(f"The sum over columns is:\n{sum}")

except Exception as err:
	print(err)