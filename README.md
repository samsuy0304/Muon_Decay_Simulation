# Muon Decay Simulation

This repository contains code for simulating muon decay times and performing parameter estimation using Python. The simulation generates synthetic data for muon decays, which can be utilized for educational purposes, particularly in scenarios where students might not have sufficient time to collect experimental data.

## Overview

This project is aimed at providing students with a tool to experience parameter estimation and chi-square testing in the context of muon decay experiments. The code utilizes the `matplotlib` and `scipy` libraries, which are essential for running the simulation and performing parameter estimation.

### Files

- **Muon.py**: This script simulates muon decays using exponential random sampling. It generates synthetic data and stores the values in text files under the directory `Data_Files`.
- **Parameter_Estimation.py**: This script uses `scipy.optimize` to perform maximum likelihood estimation based on the simulated data.

## How to Run the Code

1. To simulate muon decay, execute the following command:

```
python Muon.py -seed [-seed number] -output -events [#Events] -p [% -ve muons] -avg [life avg muon] -pife [life positive muon] -nife [life negative muon]
```
* seed: Optional parameter to specify the seed number for random sampling.
* events: Number of events to simulate.
* p: Percentage of negative muons.
* avg: Average life of muons.
* pife: Life of positive muons.
* nife: Life of negative muons.

After simulating the data, you need to edit the input file for Parameter_Estimation.py with your newly generated data.

Run the parameter estimation script using the following command:
```
python Parameter_Estimation.py

```
## Dependencies
Make sure you have installed the following libraries:

* `matplotlib`
* `scipy`
