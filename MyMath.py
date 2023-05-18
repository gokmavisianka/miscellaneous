from itertools import combinations
from math import dist

def hypotenuse(a, b, c=None, case=0):
	if case == 0:
		return (a**2 + b**2 + (0 is c is None else c)**2)**(1/2)
	elif case == 1:
		points = [a, b] + [] if c is None else [c]
		x, y = list(p[0] for p in points), list(p[1] for p in points)
		z = list(p[2] for p in points) if (len(a) == len(b) == 3) else [0, 0]
		d_x, d_y, d_z = (max(x) - min(x)), (max(y) - min(y)), (max(z) - min(z))
		return (d_x**2 + d_y**2 + d_z**2)**(1/2)
	else:
		raise ValueError(f"Unexpected case: <{case}>")

def ceil(number):
    # Rounds up to the next full integer.
    return int(number) + 1 if number > int(number) else number

def floor(number):
    # Rounds down to the next full integer.
    return int(number) if int(number) < number else number

def multiply(list_of_elements):
    # Returns the product of all the elements. Inspired by the sum() function.
    product = 1
    for element in list_of_elements:
        product *= element
    return product

def factorial(number):
    if number >= 0:
        return multiply(range(1, number + 1))
    else:
        raise ValueError("The factorial of negative numbers cannot be calculated, {number} is given.")
	
def permutations_count(n, r):
	if n >= r:
		return int(factorial(n) / factorial(n - r))
	else:
		raise ValueError(f"n must be higher or equal to r,\nn: {n}, r: {r}.")

def combinations_count(n, r, with_replacement=False):
	if n >= r:
		if with_replacement:
			return int(factorial(n + r - 1) / (factorial(n - 1) * factorial(r)))
		else:
			return int(factorial(n) / (factorial(n - r) * factorial(r)))
	else:
		raise ValueError(f"n must be higher or equal to r,\nn: {n}, r: {r}.")

def is_odd(number):
    return True if number % 2 != 0 else False

def is_even(number):
    return True if number % 2 == 0 else False

def round_to_even(number, case="up"):
    number = int(number)
    if is_odd(number) == True:
        if case == "up":
            return number + 1
        elif case == "down":
            return number - 1
        else:
            raise ValueError(f"Unexpected case: <{case}>")
    else:
        return number

def round_to_odd(number, case="up"):
    number = int(number)
    if is_even(number) == True:
        if case == "up":
            return number + 1
        elif case == "down":
            return number - 1
        else:
            raise ValueError(f"Unexpected case: <{case}>")
    else:
        return number

class consecutive:
    def sum(start, end, case="normal", replace=False):
        if end >= start:
            if case == "normal":
                return int((end - start + 1) * (end + start) / 2)
            elif case == "odd":
                start, end = round_to_odd(start - 1, "down"), round_to_odd(end, "down")
                return int(((round_to_odd(end, "down") + 1) / 2) ** 2 - ((round_to_odd(start - 1, "down") + 1) / 2) ** 2)
            elif case == "even":
                start, end = round_to_even(start - 2, "up") / 2, round_to_even(end, "up") / 2
                return int(end * (end + 1) - start * (start + 1))
        else:
            if replace == True:
                return consecutive.sum(end, start, case=case)
            else:
                raise ValueError(f"start value must be smaller or equal to end value (start: {start}, end: {end}). Change replace value to True if needed.")
		
class matrices:
	def dot_product(self, A, B):
		A_rows, A_columns = len(A), len(A[0])
		B_rows, B_columns = len(B), len(B[0])
		matrix = []  
		for row in range(A_rows):
			matrix.append([])
			for column in range(B_columns):
				matrix[row].append(sum(A[row][i] * B[i][column] for i in range(B_columns)))
		
		return matrix
	
	def transpose(self, matrix):
		row_count, column_count = len(matrix), len(matrix[0])
		transpose_of_matrix = []
		for column in range(column_count):
			transpose_of_matrix.append([])
			for row in range(row_count):
				transpose_of_matrix[column].append(matrix[row][column])
				
		return transpose_of_matrix
	
	def addition(A, B):
		A_rows, A_columns = len(A), len(A[0])
		B_rows, B_columns = len(B), len(B[0])
		matrix = []
		for row in range(A_rows):
			matrix.append([])
			for column in range(B_column):
				matrix[row].append(A[row][column] + B[row][column])
		
		return matrix
            

def array_diff(A, B):
	if type(B) in (tuple, list, dict):
		for element in B:
			while A.count(element) != 0:
				A.remove(element)
	else:
		while A.count(B) != 0:
			A.remove(B)
		
    return A
		
def is_square(points: list):
    return (len(points) == len(set(points)) == 4) and (len(set(dist(*pair) for pair in combinations(points, 2))) == 2)

def decompose(n, a=None):
    if a == None: a = n*n
    if a == 0: return []
    for m in range(min(n-1, int(a ** .5)), 0, -1):
        sub = decompose(m, a - m*m)
        if sub != None: return sub + [m]

# ceil(0.0001) -> 1
# floor(0.999) -> 0, same as the int() function.
# multiply([2, 4, 5]) -> 40
# factorial(4) -> 24
# permutations_count(4, 2) -> 12
# combinations_count(4, 2, with_replacement=False) -> 6
# combinations_count(4, 2, with_replacement=True) -> 10
# is_odd(3) -> True, is_odd(4) -> False.
# is_even(3) -> False, is_even(4) -> True.
# round_to_even(3, case="up") -> 4,
# round_to_even(3, case="down") -> 2,
# round_to_even(10) -> 10.
# round_to_odd(4, case="up") -> 5,
# round_to_odd(4, case="down") -> 3,
# round_to_odd(9) -> 9.
# consecutive.sum(1, 9, case="normal") -> 45
# consecutive.sum(1, 9, case="odd") -> 25
# consecutive.sum(1, 9, case="even") -> 20
# consecutive.sum(9, 1, replace=False) -> will raise ValueError
# consecutive.sum(9, 1, replace=True) -> 45
# consecutive.sum(1, 9, replace=True) -> 45        
