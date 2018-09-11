import math as m
import numpy as np

#THIS FUNCTION ACCEPTS THE NUMBER OF STEPS AND DIMENSION OF A SINGLE POPULANT IN THE PROBLEM
#WE WANT 30 STEPS SINCE THERE ARE 30 POPULANTS
#THE DIMENSION IS VARYING ACCORDING TO THE OPTIMIZATION FUNCTION
def levyflight(steps,dim):

    beta = 3/2;

    numerator = m.gamma(1 + beta) * m.sin(m.pi * beta/2);
    denominator = m.gamma((1+beta)/2) * beta * 2**((beta-1)/2);
    sigma = (numerator/denominator)**(1/beta);

    u = (sigma**2) * np.random.randn(steps,dim) + 0;
    v = np.random.randn(steps,dim);

    z = (u/(v**(1/beta)))/100;

    return z
