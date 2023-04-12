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

#Observed Data
InputFile1 = "Data_Files/Sim_0.2_1000_2e-06_2.4e-06Meas1.txt"
Obs_t, Obs_avg = ReadFile(InputFile1)

#True Values 
InputFile2 = "Data_Files/Sim_0.2_1000_2e-06_2.4e-06Meas10.txt"
True_t, True_avg = ReadFile(InputFile2)
print(len(Obs_t), len(True_t))

Nmeas = len(True_t)/len(True_avg)
plt.hist(Obs_t,50,density=True, alpha = 0.5, facecolor = 'r')
plt.hist(True_avg,50,density =True, alpha = 1, facecolor = 'b')
plt.show()

plt.hist2d(True_avg,Obs_t, density = True)
plt.show()
# Minimize function to find the MLE for the rate parameter
result = minimize(log_likelihood, [2], args=(Obs_t,))
rate_mle = result.x[0]


# Estimate the 95% confidence interval for the rate parameter
se = 1/np.sqrt(Nmeas * rate_mle)
rate_ci_low = rate_mle- 1.96 * se
rate_ci_high = rate_mle+ 1.96 * se

print(f"MLE for rate: {rate_mle:.2f}")