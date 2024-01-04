# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    student.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dcologgi <dcologgi@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/14 12:29:06 by dcologgi          #+#    #+#              #
#    Updated: 2023/12/14 14:31:34 by dcologgi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	
	def __str__(self):
		return (f"{self.firstname} {self.lastname}")
		

class Student(Person):
	def __init__(self, fname, lname, course = None):
		Person.__init__(self, fname, lname)
		self.course = course

	def __str__(self):
		if (self.course == None):
			return (f"{self.firstname} {self.lastname} is not registered to any course")
		else:
			return (f"{self.firstname} {self.lastname} is registered to {self.course}")

if __name__ == "__main__":
	f_name = input("Insert first name: ")
	l_name = input("Insert last name: ")
	student = input("Are you a student? (y/n)")
	while (student != 'y' and student != 'n'):
		student = input('Please type "y" or "n": ')
	if (student == 'y'):
		course = input("Please insert your degree course: ")
		s = Student(f_name, l_name, course)
		print(f"{s.firstname} {s.lastname} is registered to {s.course}")
	else:
		p = Person(f_name, l_name)
		print(f"{p.firstname} {p.lastname}")