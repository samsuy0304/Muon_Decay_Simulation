#! /usr/bin/env python3

import math
import numpy as np
import sys

#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            raise ValueError("Probability must be between 0 and 1.")
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0

    # function returns a random double (0 to infty) according to an exponential distribution
    def Exponential(self, beta=1.):
      # make sure beta is consistent with an exponential
      if beta <= 0.:
        beta = 1.

      R = self.rand();

      while R <= 0.:
        R = self.rand()

      X = -math.log(R)*beta

      return X
    
    # Function returns a random number of success after n trials according to binomial.
    def Binomial(self, n, p):
        #Check the validity of the inputs.
        if n < 0 or p < 0 or p > 1:
            return None
        #Generate a random number which will determine the highest number of successes.
        cdf = 0.
        x = 0
        u = self.rand()
        while cdf < u:
            x += 1
            cdf += math.comb(n, x)*(p**x)*((1-p)**(n-x))
        return x

    # Returns a random integer that is index of the categories provided in the probability list.
    #p is list of probability [0.5,0.5] for a coint toss
    def Categorical(self, p):
    # cumulative probability to create a map of the categories
        cdf = np.cumsum(p)
        # generate a random cdf for for an item.
        rcdf = self.rand()
        # find the corresponding outcome
        for i, val in enumerate(cdf):
            if rcdf <= val:
                return i


    def Random_Range(self, a, b,N):
        norm_range = abs(b - a)
        rand_nums = [self.rand() for _ in range(N)]
        return [(n * norm_range) + min(a, b) for n in rand_nums]



