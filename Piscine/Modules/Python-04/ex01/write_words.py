# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    write_words.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 15:34:01 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 15:45:26 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

word_len = int(input("Insert an integer: "))
file = open("words.txt", "r")
long_file = open("long_words.txt", "w")
print(f"The words longer than {word_len} have been written on 'long_words.txt")
for line in file:
    if (len(line) - 1) > word_len:
        long_file.write(line)