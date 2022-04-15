a = 5
b = 15
c = 20
d = 100
e = 123456
f = 999999
g = -6543

variables = globals().copy()
to_be_ignored = ["__annotations__", "__builtins__", "__name__", "__doc__", "__package__", "__loader__", "__spec__", "__file__"]

for variable in variables:
    if variable not in to_be_ignored:
        print(f"{variable} = {variables[variable]}")
        
"""
Output:
a = 5
b = 15
c = 20
d = 100
e = 123456
f = 999999
g = -6543
"""
