# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sum_list.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 16:46:03 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 17:24:01 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sum_list(sequence=[]):
	sum_value = 0
	for n in sequence:
		sum_value += int(n)
	return (sum_value)

if __name__ == "__main__":
	sequence = []
	n = int(input("Insert integer: "))
	while (n != 0):
		sequence.append(n)
		n = int(input("Insert integer: "))
	result = sum_list(sequence)
	print("The sum is:", result)