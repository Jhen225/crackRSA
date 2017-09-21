#!usr/bin/env python
from optparse import OptionParser


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
def findPQ(array):
    for i in range(len(array)/2):
        p = array[i]
        q = array[(len(array)-1) - i]

    return (p, q)

def gcd(a, b):
    	while b:
 		a, b = b, a%b
	return a
        
def main():
    
    #Adding options for terminal inputs
    parser = OptionParser()
    parser.add_option('-e', type="int")
    parser.add_option('-n', type="int")
    parser.add_option('--ciphertext',type="int")
    options, args = parser.parse_args()

    #Getting terminal inputs and storing them
    e = options.e
    n = options.n
    c = options.ciphertext

    #Factoring n to get (p,q)
    p, q = findPQ(sorted(factors(n)))

    #Computing phi
    phi = (p-1)*(q-1)

    #Computing d
    d = 0
    while (((e*d)-1)%phi) != 0:
        d+=1

    #Finding the message
    m = ((c**d)% n)

    print 
    print "p: " + str(p)
    print "q: " + str(q)
    print "phi: " + str(phi)
    print "d: " + str(d)
    print "m: " + str(m)

main()