# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_trim.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 16:13:03 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/13 16:49:11 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def trim(lst = []):
	if (len(lst) > 0):
		lst.pop()
		lst.pop(0)
	return (None)

if __name__ == "__main__":
	try:
		if (len(sys.argv) < 3):
			raise Exception("Error! You must insert at least 2 values")
		lst = []
		for i in sys.argv[1:]:
			lst.append(i)
		trim(lst)
		print("The new list is:", lst)
			
	except Exception as err:
		print(err)