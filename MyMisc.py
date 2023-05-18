def format_words(words):
    if type(words) == list:
        _f_ = lambda element: element != ''
        words = list(filter(_f_, words))
        length = len(words)
        if length == 0:
            return ''
        elif length == 1:
            return words[0]
        else:
            return ", ".join(words[:length-1]) + " and " + words[-1]
    else:
        return ''
	
# A = ["one", "two", "three"]
# B = ["Me", "you"]
# C = list("abcdef")
# format_words(A) -> "one, two and three"
# format_words(B) -> "Me and you"
# format_words(C) -> "a, b, c, d, e and f"

def pyramid_array(n):
    return [[0] * row for row in range(1, n+1)]

# pyramid_array(3) -> [[0], [0, 0], [0, 0, 0]]

def split_number(n, case=0):
    if case == 0:
        return list(int(digit) for digit in str(n))
    elif case == 1:
        n = str(n)
        length = len(n)
        return list(int(n[i])*(10**(length - i - 1)) for i in range(length))
    elif case == 2:
        n = str(n)
        length = len(n)
        return list(10**(length - i - 1) for i in range(length))
    else:
        raise ValueError(f"Unexpected case: <{case}>")
		
# split_number(123) -> [1, 2, 3]
# split_number(123, case=1) -> [100, 20, 3]
# split_number(123, case=2) -> [100, 10, 1]

class roman:
	def encode(number):
		dictionary = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
					  100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
					  9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
		roman = ""
		for key in dictionary:
			x = number // key
			if x != 0:
				roman += dictionary[key] * (x)
				number %= key
				if number == 0:
					break
		
		return roman
	
	def decode(roman):
		dictionary = {'CM': 900, 'M': 1000, 'CD': 400, 'D': 500,
					  'XC': 90, 'C': 100, 'XL': 40, 'L': 50,
					  'IX': 9, 'X': 10, 'IV': 4, 'V': 5, 'I': 1}
		number = 0
		for key in dictionary:
			if key in roman:
				number += dictionary[key] * roman.count(key)
				roman = roman.replace(key, '')
				
		return number
	
# roman.encode(123) -> "CXXIII"
# roman.decode("CXXIII") -> 123

def has_duplicate(array):
    for element in set(array):
        if array.count(element) > 1:
            return True
    return False

# has_duplicate([1, 2, 3, 1]) -> True
# has_duplicate([1, 2, 3]) -> False
