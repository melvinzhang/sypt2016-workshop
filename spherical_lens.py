import numpy as np
import matplotlib.pyplot as plt

# global parameters
n, a, b, c, xf= 1.5 , 1. , 2., 1. , 100

# function for semi-convex lens equation
def semiConvexLens (y, a, b, c):
    x = np.sqrt( a**2 * (c**2 - (y**2 / b**2)) )    # (x^2 / a^2) + (y^2 / b^2) = c^2
    normalgradient = (a**2 / b**2) * (y/x)          # gradient of normal
    angleofincidence = np.arctan ( normalgradient ) # angle of incidence
    return x , normalgradient , angleofincidence

# create array for y values of lens profile
ylens = np.linspace (-c*b, c*b, 100)
# create array for y values of incident ray on second interface
y0 = np.linspace (-0.5*c*b,0.5*c*b,6)

# compute x values, gradient of normal and angle of incidence at intersection
xlens , temp1 , temp2 = semiConvexLens (ylens, a, b, c)   # for lens profile
x0 , m, thetaI = semiConvexLens (y0, a, b, c)             # for incident ray

# compute angle of refraction
thetaR = np.arcsin ((1./n) * np.sin(thetaI))

# compute gradient of refracted ray
gradient_outRay = np.tan(thetaR - thetaI)

# compute yvalues of refracted ray
y_OutRay = y0 + gradient_outRay * (xf - x0)

# plot lens profile with title and axis
plt.figure(1, figsize = (10,6) )
plt.plot(xlens, ylens, "k-")
plt.plot([0,0], [-c*b, c*b], "k-")
plt.title("Spherical Lens Abberation")
plt.axis([-5, 18, -0.5-c*b, 0.5+c*b])

# plot several rays
for i in range(len(x0)):
    plt.plot([-10, x0[i]], [y0[i], y0[i]], "m-")
    plt.plot([x0[i], xf], [y0[i], y_OutRay[i]], "m-")

# save plot to file
plt.savefig("Spherical-lens-abberation.png")

# display plot on screen
plt.show()
