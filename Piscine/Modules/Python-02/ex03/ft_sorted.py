# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sorted.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 15:20:09 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/13 16:12:08 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	if (len(sys.argv) < 3):
		raise Exception("Error! You must insert at least 2 numbers")
	stack = []
	for i in sys.argv[1:]:
		stack.append(int(i))
	n = stack[0]
	flag = 0
	for j in stack:
		if (j > n):
			flag = 1
		n = j
	if (flag == 0):
		raise Exception("The inserted sequence is sorted!")
	else:
		stack.sort(reverse = True)
		print(f"The inserted sequence is not sorted!\nThe correct order is {stack}")

except Exception as err:
	print(err)