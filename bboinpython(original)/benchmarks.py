# -*- coding: utf-8 -*-
"""

This is the code for Biogeography-Based Optimization (BBO)
@author: Dan Simon
Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)

-- Benchmark Function File: Defining the benchmark function along its range lower bound, upper bound and dimensions

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math

# define the function blocks

#Sphere function
def F1(x):
    s=numpy.sum(x**2);
    return s


#Ackley Function
def F2(x):
    term1 = 0
    term2 = 0
    for i in range(10):
        #associated with ft1
        term1 = term1 + x[i]*x[i]
        #associated with ft2
        term2 = term2 + math.cos(2*3.14*x[i])


    ft1 = 20 * math.exp(-0.02 * math.sqrt(term1/10))
    ft2 = math.exp(term2/10)

    result = 20 + math.exp(1) - ft1 - ft2

    return round(result,2)


#Alpine Function
def F3(x):
    result=0
    # limit on x in not applied here
    for i in range(10):
        result = result + abs(x[i]*math.sin(x[i])+0.1*x[i])

    return round(result,2)


#Bartels Conn Function
def F4(x):
    result = 0
    # limit on x in not applied here
    result = result + abs((x[0]*x[0])+(x[1]*x[1])+(x[0]*x[1]))+abs(math.sin(x[0]))+abs(math.cos(x[1]))

    return result


#Beale Function
def F5(x):
	result = 0
	result = result + (1.5-x[0]+x[0]*x[1])**2 + (2.25 -x[0]+x[0]*x[1]*x[1])**2 + (2.625 - x[0] +x[0]*(x[1]**3))**2

	return result


#Bird Function
def F6(x):
	result = 0
	# limit on x in not applied here
	result = result + (math.sin(x[0])*math.exp((1-math.cos(x[1]))**2)) + (math.cos(x[1])*math.exp((1-math.sin(x[0]))**2)) + ((x[0]-x[1])**2)

	return result

#Bohachevsky Function
def F7(x):
	result = 0
	# limit on x'i' value not defined here
	result = result + x[0]*x[0]+2*x[1]*x[1]+0.7 - 0.3*math.cos(3*math.pi*x[0])+0.4*math.cos(4*math.pi*x[1])

	return result


#Booth Function
def F8(x):
	result = 0
	result = result + (x[0]+2*x[1]-7)**2 + (2*x[0]+x[1]-5)**2

	return result


#Box-Betts Quadratic Sum Function
def F9(x):
	result = 0
	for i in range(3-1):

		g = math.exp(-0.1*(i+1)*x[0])-math.exp(-0.1*(i+1)*x[1])-math.exp(((-0.1*(i+1))-math.exp(-1*(i+1)))*x[2])

		result = result + g**2

	return round(result,2)


# Brent Function
def F10(x):
	result = 0
	result = result + ((x[0]+10)**2) + ((x[1]+10)**2) + math.exp((-1*x[0]**2)-(1*x[1]**2))
	return result


def getFunctionDetails(a):

    # [name, lb, ub, dim]
    param = {  0: ["F1",-100,100,30],
               1: ["F2",-35,35,10],
               2: ["F3",-10,10,10],
               3: ["F4",-500,500,2],
               4: ["F5",-4.5,4.5,2],
               5: ["F6",-2*math.pi,2*math.pi,2],
               6: ["F7",-100,100,2],
               7: ["F8",-10,10,2],
               8: ["F9",-0.9,11.2,3],
               9: ["F10",-10,10,2],
            }
    return param.get(a, "nothing")
