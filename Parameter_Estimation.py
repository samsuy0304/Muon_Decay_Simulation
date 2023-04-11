#! /usr/bin/env python

# Necessary Libraries
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import expon
    
# User Defined Functions
def Average(lst):
    return sum(lst) / len(lst)

# Define the log-likelihood function for an exponential distribution
def log_likelihood(params, data):
    rate = params[0]
    log_likelihood = np.sum(np.log(rate) - rate * data)
    return -log_likelihood


def ReadFile(m):
    tt=[]
    tt2=[]
    need_rate = True
    with open(m) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
        
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                tt.append(float(v))

            t_avg /= Nmeas
            tt2.append(t_avg)
    ifile.close()
    tt = np.array(tt)
    return tt, tt2


InputFile = "Data_Files/Sim_0.21000_2e-06_2.4e-06.txt"
t, Average = ReadFile(InputFile)

plt.hist(t,50)
# Minimize function to find the MLE for the rate parameter
result = minimize(log_likelihood, [2], args=(t,))
rate_mle = result.x[0]

print(f"MLE for rate: {rate_mle:.2f}")

