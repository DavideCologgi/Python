# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    circle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 11:25:47 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 12:25:23 by dcologgi         ###   ########.fr        #
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

    def contains(self, point):
        distance = ((point.x)**2 + (point.y)**2)**0.5
        if (distance <= self.radius):
            return (True)
        else:
            return (False)
        
    def __str__(self):
        return f"Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}"
    
if __name__ == "__main__":
    try:
        if (len(sys.argv) != 3):
            raise Exception("Error! Wrong number of parameters")
        p_x = float(sys.argv[1])
        p_y = float(sys.argv[2])
        point = Point(p_x, p_y)
        circle = Circle((0, 0), 1)
        if (circle.contains(point)):
            print(f"The point ({p_x}, {p_y}) lies in the Circle of center (0, 0) and radius 1")
        else:
            print(f"The point ({p_x}, {p_y}) lies out the Circle of center (0, 0) and radius 1")

    except Exception as err:
        print(err)