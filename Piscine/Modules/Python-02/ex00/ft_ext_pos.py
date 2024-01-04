# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ext_pos.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 10:44:06 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/13 12:40:46 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def my_min(lst = []):
	mn = lst[0]
	for n in lst:
		if (n < mn):
			mn = n
		print(mn)
	return (mn)
	
def my_max(lst = []):
	mx = lst[0]
	for n in lst:
		if (n > mx):
			mx = n
	return (mx)

def get_index(num, lst):
	i = -1
	for n in lst:
		i += 1
		if (num == n):
			return (i)

try:
	if (len(sys.argv) < 2):
		raise Exception("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
	lst = []
	for arg in sys.argv[1:]:
		lst.append(arg)
	mn = (my_min(lst), get_index(my_min(lst), lst))
	mx = (my_max(lst), get_index(my_max(lst), lst))
	print(f"The min is {mn[0]} and its position is {mn[1]}")
	print(f"The max is {mx[0]} and its position is {mx[1]}")
	
except Exception as err:
	print(err)