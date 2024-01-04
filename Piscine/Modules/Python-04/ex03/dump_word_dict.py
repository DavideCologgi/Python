# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dump_word_dict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 15:56:03 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 16:44:06 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pickle

dictionary = {}
with open("words.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word_len = len(word)
            if (word_len in dictionary):
                dictionary[word_len] += 1
            else:
                dictionary[word_len] = 1
with open("word_count.pickle", "wb") as pick:
    pickle.dump(dictionary, pick)