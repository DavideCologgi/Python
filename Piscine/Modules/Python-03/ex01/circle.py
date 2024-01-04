# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    circle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 10:49:02 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 12:03:48 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = Point(*center)
        self.radius = radius

    def __str__(self):
        return f"Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}"
    
if __name__ == "__main__":
    try:
        if (len(sys.argv) != 1):
            raise Exception("Error! Wrong number of parameters")
        circle = Circle((150, 100), 75)
        print(circle)

    except Exception as err:
        print(err)