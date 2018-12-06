#Day 15 Homework 1
#Central difference approximations

import numpy as np

x=3
h1=.01
h2=.001

def function(X):
    return np.cos(X)*np.tanh(X)
    
def analytic(x):
    return (-np.sin(x)*np.tanh(x))+((1/((np.cosh(x))**2))*np.cos(x))
    
def centraldiff(x,h):
    fprime=(function(x+h)-function(x-h))/(2*h)
    return fprime

A=analytic(x)
print "Analytic",A

B=centraldiff(x,h1)
print "Derivative at h=.01",B

C=centraldiff(x,h2)
print "Derivative at h=.001",C

def Error(x,h): #From Symbolab
    return (h**2)*(1./6.)*((4.*np.cos(x)*((np.tanh(x))**2)*(1./((np.cosh(x))**2)))+(((6./((np.cosh(x))**2))+1)*(np.sin(x)*np.tanh(x)))-((2.*np.cos(x)*(1./((np.cosh(x))**4)))-(3.*np.cos(x)*(1./(np.cosh(x)**2)))))

E1=Error(x,h1)
E2=Error(x,h2)
print "When h is",h1," The error is", E1
print "When h is",h2," The error is", E2

E_ratio=E2/E1
H_ratio=(h2/h1)**2

print "The ratio of E2/E1 is",E_ratio
print "The ratio of (h2/h1)^2 is",H_ratio
print "Which tells us that the error is proportional to h^2"
