# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_max_val.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 15:10:02 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 15:19:40 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
    if (len(sys.argv) != 4):
        raise Exception("Error! Usage: python3 ft_max.py <x> <y> <z>")
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
    n3 = float(sys.argv[3])
    max_val = n1
    if (n2 > max_val):
        max_val = n2
    if (n3 > max_val):
        max_val = n3
    print(f"The max is: {max_val}")

except Exception as err:
    print(err)