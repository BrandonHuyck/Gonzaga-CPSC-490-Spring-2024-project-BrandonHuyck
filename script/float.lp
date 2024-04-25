#script(python)
    
def add(x, y):
    return str(float(x.string) + float(y.string))

def mult(x, y):
    return str(float(x.string) * float(y.string))

def inv(x):
    return str(1 / float(x.string))

def eq(x, y):
    return str(float(x.string) == float(y.string))

def nq(x, y):
    return not eq(x, y)

def lt(x, y):
    return str(float(x.string) < float(y.string))

def lq(x, y):
    return lt(x, y) or eq(x, y)

def gt(x, y):
    return not lq(x, y)

def gq(x, y):
    return not lt(x, y)

def py_sum(x):
    return sum( map( int, x.string.split(';') ) )

def py_sort(x):
    return '; '.join( map( str, sorted( list( map( int, x.string.split(';') ) ) ) ) )

#end.

float("1.41"; "2.71"; "3.14").
result(@add("2.3", "3.1")).

list("3; 1; 2").
result( @py_sum(X) ) :- list(X).
result( @py_sort(X) ) :- list(X).

