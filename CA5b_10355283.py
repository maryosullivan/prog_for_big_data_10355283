# CA_5b_Calculator   
# Mary O'Sullivan, Staff Id: 10355283   

# Max function
def max(values):
    return reduce(lambda a,b: a if (a>b) else b, values)
    
print max([47, 11, 42, 13])
    
# Min function
def min(values):
    return reduce(lambda a,b: a if (a<b) else b, values)
    
print min([47, 11, 42, 13])

# Add function
def add(values):
    return reduce(lambda a,b: a+b, values)
    
print add([47, 11, 42, 13])

# Subtract function
def subtract(values):
    return reduce (lambda a,b: a-b, values)
    
print subtract([47, 11, 42, 13])

# Is Even Function
def is_even(values):
    return filter(lambda x: x % 2 == 0, values)

print is_even([47, 11, 42, 13])

# Is Odd Function
def is_odd(values):
    return filter(lambda x: x % 2 == 0, values)
    
print is_odd([47, 11, 42, 13])

# Divide Function
def divide(values):
    return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan', values)
    
print divide([47, 11, 42, 13])

# Multiply Function 
def multiply(values):
    return reduce (lambda a,b: a*b, values)

print multiply([47, 11, 42, 13])



def fahrenheit(t):
    return ((float(9)/5)*t + 32)

def celsius(t):
    return (float(5)/9*(t - 32))

# def celcius to fahrenheit
def to_fahrenheit(values):
    return map(fahrenheit, values)
    
print to_fahrenheit([0, 37, 40])

# def fahrenheit to celcius
def to_celsius(values):
    return map(celsius, values)
    
print to_celsius([0, 32, 100, 212])


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]

my_list = [fahrenheit(x) for x in Celsius]

n = 30

print [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x**2 + y**2 == z**2]

pyt_triples = []
for x in range(1,n):
    for y in range(x,n):
        for z in range (y,n):
            if x**2 + y**2 == z**2:
                pyt_triples.append((x,y,z))
print pyt_triples


colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]

print coloured_things

def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
    
x = city_generator()
print x.next()
print x.next()
print x.next()
print x.next()

cities = city_generator()
for city in cities:
    print city

    
    
def get_triplets(n):
    for x in range(1,n):
        for y in range(x,n):
            for z in range (y,n):
                if x**2 + y**2 == z**2:
                    yield (x,y,z)
                    
triplets = get_triplets(100)
for triplet in triplets:
    print triplet,
print
    
# Fibonacci numbers generator, first n
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter >= n): return
        yield a
        a, b = b, a + b
        counter += 1
        
f = fibonacci(500)
for x in f:
    print x,
print