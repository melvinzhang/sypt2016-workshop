import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

# get external data
tdata, ydata = np.loadtxt( "paper-drop-data1.csv" , skiprows=1 , unpack=True, delimiter = ";", dtype=float)

# global parameters
grav , mass = 9.8 , 7.e-3 
yinitial = ydata[0]

# define fitting function
def quadraticDrag ( t , b ):
    return yinitial - (mass / b) * np.log( np.cosh(t * np.sqrt(grav * b / mass) ) )

# fit data using SciPy's Levenburg-Marquart method
b0 = 10.0      # initial guess for fitting parameter
b , nlcov = scipy.optimize.curve_fit (quadraticDrag, tdata, ydata, b0, sigma=None)
# b is the (best) fit parameter from scipy.optimize.curve_fit

# b_stddev is the standard deviation of the fit parameter
b_stddev = np.sqrt( nlcov[0][0] )  

# create array using fitting function
ytheory2 = quadraticDrag( tdata, b)

# plotting
plt.figure(1, figsize = (12,8) )

plt.plot(tdata, ydata, "ro", label="data")
plt.plot(tdata, ytheory2, "b-", label="theory")
plt.xlabel("t")
plt.ylabel("y")
plt.title("Graph of displacement against time\n Data + model with drag coefficient b = %1.3f" %b)
plt.legend(loc="upper right")
plt.axhline(color = "gray", zorder=-1)
plt.axvline(color = "gray", zorder=-1)

# save plot to file
plt.savefig("Fit3.png")

plt.show()