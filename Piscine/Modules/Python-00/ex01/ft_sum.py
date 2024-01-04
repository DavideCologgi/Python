# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sum.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 10:46:29 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 10:59:12 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    num1 = int(input("Insert your first integer: "))
    num2 = int(input("Insert your second integer: "))
    result = num1 + num2
    print(f"Result: {result}")

except Exception as e:
    print(e)