#!/usr/bin/python

#!/media/sf_Ubuntu/python python

#!/usr/bin/env python

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print "hello, this is Gary\n"   #all the statements in a script/module will be excuted when import or execute

#for '>>> execfile('script.py', {'a':9}, {'b':20})'	#locals has prioriry than globals in reference
if __name__=='__builtin__':
    import sys
    print len(sys.argv)
    print 'a', sys.argv[0], 'b'
    print a
    fib(a)
    print
    print b
    fib(b)

#for 'gary@VirtualBox:/media/sf_Ubuntu/python$ python script.py 9'
#and for '>>> execfile('script.py')'
if __name__ == "__main__":  # when execute as a script, the condition is true
    print 'run script\n'
    try:
        import sys
        print len(sys.argv)
        if len(sys.argv) ==2:
            print 'argv[0]= ', sys.argv[0], 'argv[1]= ', sys.argv[1]
            fib(int(sys.argv[1]))
    except NameError:
        print 'NameError'
    except IndexError:
        print 'IndexError'
    else:
        print 'script finished.'

#for 'import script'
if __name__ == "script":  # when import, the __name__ == "fibo" is true   #script or fibo is the main file name
    print __name__, 'imported'
