#! /usr/bin/env python
# imports of external packages to use in our code
import sys
# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# import our Generator class file
sys.path.append(".")
#User Defined
from Generator import Decay

def Average(lst):
    return sum(lst) / len(lst)
## Main File for the program

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: Muon.py -seed [-seed number] -output -events [#Events] -p [% -ve muons] -avg [life avg muon] -pife [life positive muon] -nife [life negative muon]" % sys.argv[0])
        sys.exit(1)
    
    # Predefined Constants

    seed = 5555;
    events = 1000;
    p = [0.5,0.5];
    lifetime_neg = 2.0e-6;
    lifetime_pos = 2.4e-6;
    avg_muon = 2.4e-6
    meas = 10

    if '-seed' in sys.argv:
        index = sys.argv.index('-seed')
        seed = int(sys.argv[index + 1])

    if '-events' in sys.argv:
        index = sys.argv.index('-events')
        events = int(sys.argv[index + 1])

    if '-meas' in sys.argv:
        index = sys.argv.index('-meas')
        meas = int(sys.argv[index + 1])

    if '-p' in sys.argv:
        index = sys.argv.index('-p')
        p = [float(sys.argv[index + 1]),1-float(sys.argv[index + 1])]

    if '-pife' in sys.argv:
        index = sys.argv.index('-pife')
        lifetime_pos = float(sys.argv[index + 1])

    if '-avg' in sys.argv:
        index = sys.argv.index('-avg')
        avg_muon = float(sys.argv[index + 1])

    if '-nife' in sys.argv:
        index = sys.argv.index('-nife')
        lifetime_neg = float(sys.argv[index + 1])

    if '-output' in sys.argv:
        doOutputFile = True


    # Use the seed value in your code
    print("Using seed:", seed)
    print("Using No. of Events:", events)
    print("Using Distribution of -/+ muon", p)
    print("Using Positive Muon Lifetime:", lifetime_pos)
    print("Using Negative Muon Lifetime", lifetime_neg)



    Tests= Decay(seed, events, p, lifetime_neg, lifetime_pos)


    ln, lp, lm = Tests.Time(meas)
    
    Filename = "Data_Files/"+ "Sim_"+str(p[0])+'_'+str(events)+"_"+str(lifetime_neg)+"_"+str(lifetime_pos)+"Meas"+str(meas)+".txt"

    
    if doOutputFile:
        outfile = open(Filename, 'w')
        outfile.write(str(lifetime_neg)+" \n")
        for e in range(0,len(lm)):
            #outfile.write(str(Average(lm[e]))+" ")
            for t in range(0,meas):
                #pass
                outfile.write(str(lm[e][t])+" ")
            outfile.write("\n")
        outfile.close()


     

