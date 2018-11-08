def thing():
    print ('Hello')
    print('Fun')

thing()
print('Zip')
thing()

# Max Function
big = max('Hello world')
print(big)

# type conversion
print(float(99)/100)
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))
print(1+2*float(3)/4-5)

# string conversions
sval = '123'
print(type(sval))
# print(sval+1) ## TypeError: can only concatenate str (not "int") to str
ival = int(sval)
print(type(ival))
print(ival + 1)
nsv = 'hello bob'
# niv = int(nsv) #ValueError: invalid literal for int() with base 10: 'hello bob'

# Building own functions
x = 5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyrics()
x=x+2
print(x)

# Parameters
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

# Parameters/Arguments
def addtwo(a,b):
    added = a+b
    return added

x = addtwo(3,5)
print(x)

# Exercise
def computepay(hours, rate):
    return 40 * rate + ((hours - 40) * rate * 1.5)

print(computepay(45,10))
