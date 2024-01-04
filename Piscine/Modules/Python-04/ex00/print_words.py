# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_words.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 15:14:05 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 15:32:55 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

word_len = int(input("Insert an integer: "))
file = open("words.txt", "r")
print(f"The words longer than {word_len} are the following:")
for line in file:
    cleaned_line = line.strip()
    if len(cleaned_line) > word_len:
        print(cleaned_line)

        