# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_summorial.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 16:38:00 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 16:45:12 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
    if (len(sys.argv) != 2):
        raise Exception("Error! Usage: python3 ft_summorial.py <n>")
    n = int(sys.argv[1])
    if (n < 0):
        raise  Exception("Error! n must be >=0")
    summorial = 0
    while (n > 0):
        summorial = summorial + n
        n -= 1
    print(f"The sum is: {summorial}")

except Exception as err:
    print(err)