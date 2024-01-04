# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_words.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 15:46:15 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 15:55:07 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    filename = input("Insert file name: ")
    file = open(filename, "r")
    word_len = int(input("Insert an integer: "))
    print(f"The words longer than {word_len} are the following:")
    for line in file:
        cleaned_line = line.strip()
        if len(cleaned_line) > word_len:
            print(cleaned_line)

except FileNotFoundError:
    print("Error! The specified file does not exist!")