# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_compare.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 12:18:43 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 14:30:49 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
    if (len(sys.argv) != 3):
        raise Exception("Wrong number of parameters!")
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    if (num1 > num2):
        print(f"{num1} is greater than {num2}")
    elif (num1 == num2):
        print(f"{num1} is equal to {num2}")
    else:
        print(f"{num1} is less than {num2}")

except Exception as err:
    print(err)