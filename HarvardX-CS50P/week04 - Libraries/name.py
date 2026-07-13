import sys
# https://docs.python.org/3/library/sys.html

try: 
    print('hello, my name is', sys.argv[1]) 
except IndexError:
    print('Too few arguments')


print('--- Another way ---')

if len(sys.argv) < 2:
    sys.exit('Too many arguments')

elif len(sys.argv) > 2:
    sys.exit('Too much arguments')

print('Hello, my name is', sys.argv[1])
