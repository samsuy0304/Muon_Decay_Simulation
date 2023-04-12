# PHSX815_Project3

This repository contains the code for parameter estimation of muon decay times. The code uses `matplotlib` and `scipy` libraries to run. Libraries can be installed from resepctive websites.

### Details

`Muon.py`: Simulates muon decays using exponential randm sampling. Stores the values in text files under `Data_Files`.

`Parameter_Estimaation.py`: Uses `scipy.optamize` to perform maximum likelihood estimation.

### How to Run the Code 

To simulate the muon decay use:
```
python Muon.py -seed [-seed number] -output -events [#Events] -p [% -ve muons] -avg [life avg muon] -pife [life positive muon] -nife [life negative muon]

```

To use `Parameter_Estimation.py` you must edit the `InputFile` to your newly simulated data. 

```
python Parameter_Estimation.py
```
