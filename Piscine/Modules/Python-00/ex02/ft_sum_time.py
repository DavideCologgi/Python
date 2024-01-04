# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sum_time.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 10:51:56 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/12 11:05:07 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    hours = int(input("Insert hours: "))
    minutes = int(input("Insert minutes: "))
    seconds = int(input("Insert seconds: "))

    total = (hours * 3600) + (minutes * 60) + seconds
    print(f"Total seconds: {total}")

except Exception as err:
    print(err)