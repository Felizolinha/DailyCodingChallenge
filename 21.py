x = [(30, 75), (0, 50), (60, 150)]

def is_a_contained_in_b(a, b):
    #Input tuples must be ordered: (x,y) x<=y
    return a[0] >= b[0] and a[1] <= b[1]

rooms = 0

for i, val in enumerate(x):
    if val