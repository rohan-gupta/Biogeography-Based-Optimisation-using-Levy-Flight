# -*- coding: utf-8 -*-
"""

This is the code for Biogeography-Based Optimization (BBO)
@author: Dan Simon
Reference: D. Simon, Biogeography-Based Optimization, IEEE Transactions on Evolutionary Computation, in print (2008).
Coded by: Raju Pal (emailid: raju3131.pal@gmail.com) and Himanshu Mittal (emailid: himanshu.mittal224@gmail.com)

-- ClearDups File: Function for removing the duplicates in the Population

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import random

def ClearDups(Population, PopSize, dim, MaxParValue, MinParValue):

    for i in range(PopSize):
        Chrom1 = numpy.sort(Population[i,:]);
        for j in range(i+1,PopSize):
            Chrom2 = numpy.sort(Population[j,:]);
            if Chrom1 is Chrom2:
                parnum = numpy.ceil(dim * random.random());
                Population[j,parnum] = MinParValue + (MaxParValue - MinParValue) * random.random();
    return Population
                