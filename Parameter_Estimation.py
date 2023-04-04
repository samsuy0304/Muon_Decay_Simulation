#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import statistics
import sys
from scipy.optimize import minimize


    
# User Defined Functions

def Average(lst):
    return sum(lst) / len(lst)

def likelihood(alpha, data):
    # Calculate the likelihood of observing the data given the decay rate parameter alpha
    p = []
    for i in data:
        pi = np.exp(-alpha * i)
        p.append(pi)
    likelihood = np.prod(p)
    return likelihood



def CreateLabels(m,d):
    n = m.split("/")
    y = n[1].split("_")
    k = str(len(d))
    g = y[1].replace(k,"")
    return g

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
    return tt, tt2
if __name__ == "__main__":
   
    
    Nmeas = 10
    InputFile = "Data_Files/Sim_0.21000_2e-06_2.4e-06.txt"
    times1 = []
    times_avg1 = []
    times2 = []
    times_avg2 = []

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options] -meas [No. of meas] -I1 [input file1]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    if '-meas' in sys.argv:
        index = sys.argv.index('-meas')
        Nmeas = int(sys.argv[index + 1])

    if '-I1' in sys.argv:
        index = sys.argv.index('-I1')
        InputFile = "Data_Files/"+sys.argv[index + 1]


    
    print("Got the values")

    
    
    times1, times_avg1 = ReadFile(InputFile)
    print("Read Input1")



    variance = statistics.variance(times_avg1)
    q25 = np.quantile(times_avg1, 0.25)
    q50 = np.quantile(times_avg1, 0.5)
    q75 = np.quantile(times_avg1, 0.75)

    print("Calculated the quandrants")

    plt.hist(times_avg1, 50, density = True, facecolor='r', alpha=0.75, label="NP= "+CreateLabels(InputFile,times_avg1))
    plt.axvline(q25, color='m', linestyle='dashed', linewidth=1, label ="NP= "+CreateLabels(InputFile,times_avg1)+'Q25')
    plt.axvline(q50, color='k', linestyle='dashed', linewidth=1, label ="NP= "+CreateLabels(InputFile,times_avg1)+'Q50')
    plt.axvline(q75, color='y', linestyle='dashed', linewidth=1, label ="NP= "+CreateLabels(InputFile,times_avg1)+'Q75')
    plt.axvline(Average(times_avg1), color='b', linestyle='dashed', linewidth=1, label="NP= "+CreateLabels(InputFile,times_avg1))
    
    
    plt.title('Decay Times with Different NP values (NP = #Negativ Muons/ #Total Muons')
    plt.xlabel('Time')
    plt.ylabel('Probability')
    plt.legend()
    plt.savefig(InputFile+"Times_avg_HistogramPlot.png")
    

    nll = lambda alpha: likelihood(alpha,times_avg1)

    # Use maximum likelihood estimation to find the value of lambda that maximizes the likelihood
    result = minimize(nll, x0=[2.6e-6])
    print(result)
    lambda_hat = result.x[0]
    print(f"Estimated lambda: {lambda_hat}")
