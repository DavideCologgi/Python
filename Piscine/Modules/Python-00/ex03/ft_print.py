# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_print.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 11:06:19 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 11:12:32 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    string = input("Insert a string: ")
    n = int(input("Insert an integer: "))
    l = len(string)
    if (n > l):
        raise Exception("Error: index out of range")
    print(string[n] + " " + string[-n])

except Exception as err:
    print(err)
