#!usr/bin/env python

from optparse import OptionParser
from math import log

def findAB(g,n,X):
    x = 0
    for a in range(n):
        x = g**a % n
        if x == X:
            return a

def findK(n,X,S):
    return (X**S)%n


def main():
    
    parser = OptionParser()
    parser.add_option('-g', type="int")
    parser.add_option('-n', type="int")
    parser.add_option('--alice',type="int")
    parser.add_option('--bob',type="int")
    options, args = parser.parse_args()

    # print options

    g = options.g
    n = options.n
    alice = options.alice
    bob = options.bob

    a = findAB(g,n,alice)
    b = findAB(g,n,bob)

    kp = findK(n,alice,b)
    kn = findK(n,bob,a)

    print 
    print "Secret Key of Alice: " + str(a)
    print "Secret Key of Bob: " + str(b)
    print "Shared Secret of Alice: " + str(kp)
    print "Shared Secret of Bob: " + str(kn)

main()

