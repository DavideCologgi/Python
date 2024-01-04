# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 13:42:12 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/13 14:29:24 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def is_palindrome(check):
	p = len(check) / 2
	i = 0
	while (i < p):
		if (check[i] != check[-i - 1]):
			return (False)
		i += 1
	return (True)

if __name__ == "__main__":
	try:
		if (len(sys.argv) > 2):
			raise Exception("Error! Insert just 1 string!")
		elif (len(sys.argv) == 1):
			raise Exception("Error! Insert a string as parameter")
		str = sys.argv[1]
		form_str = str.replace(" ", "")
		if (is_palindrome(form_str)):
			print(f"The string {str} is palindrome")
		else:
			print(f"The string {str} is not palindrome")

	except Exception as err:
		print(err)