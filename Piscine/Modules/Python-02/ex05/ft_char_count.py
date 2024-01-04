# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_char_count.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 16:50:45 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 16:16:16 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	if (len(sys.argv) < 2):
		raise Exception("Error! No string given")
	elif (len(sys.argv) > 2):
		raise Exception("Error! Insert only 1 string")
	phrase = sys.argv[1]
	dictionary = dict()
	for c in phrase:
		if c in dictionary:
			dictionary[c] += 1
		else:
			dictionary[c] = 1
	print("Char count:")
	ord_dictionary = dict(sorted(dictionary.items()))
	for key, value in ord_dictionary.items():
		print(f"{key} = {value}")

except Exception as err:
	print(err)