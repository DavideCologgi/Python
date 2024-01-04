# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    point.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 09:43:58 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 12:14:28 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

if __name__ == "__main__":
	try:
		if(len(sys.argv) != 1):
			raise Exception("Error! Too many parameters")
		# Crea il primo Point
		point = (input("Insert the coordinates of the first point: "))
		x_str, y_str = point.split(',')
		x = float(x_str)
		y = float(y_str)
		p1 = Point(x, y)
		# Crea il secondo Point
		point = ((input("Insert the coordinates of the second point: ")))
		x_str, y_str = point.split(',')
		x = float(x_str)
		y = float(y_str)
		p2 = Point(x, y)
		# Calcolo la distanza tra p1 e p2
		distance = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5
		print("Their distance is:",distance)

	except Exception as err:
		print(err)
	