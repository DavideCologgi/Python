# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_min.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 15:21:54 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 16:36:57 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def my_min(x=0, y=0, z=0):
    min_val = x
    if (y < min_val):
        min_val = y
    if (z < min_val):
        min_val = z
    return (min_val)

if __name__ == "__main__":
    try:
        if (len(sys.argv) != 4):
            raise Exception("Error! Usage: python3 ft_min.py <x> <y> <z>")
        n1 = float(sys.argv[1])
        n2 = float(sys.argv[2])
        n3 = float(sys.argv[3])
        min_val = my_min(n1, n2, n3)
        print(f"The min is: {min_val}")

    except Exception as err:
        print(err)

