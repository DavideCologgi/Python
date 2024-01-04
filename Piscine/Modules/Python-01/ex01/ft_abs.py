# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_abs.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 14:32:10 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 15:08:42 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

expression = input("Insert an expression: ")
abs_result = eval(expression)
if (abs_result < 0):
    abs_result = -abs_result
print(f"The result is: {abs_result}")