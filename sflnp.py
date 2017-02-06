# Simple Feedforward Learning Network in Python (SFLNP)
#
# Most of my algorithm development is with Matlab.
# Want to teach myself Python.
# So writing this simple network as a self-teaching tool.
#
# To Do:
#           Regularization
#           Use MNIST dataset
#           Hyperparameter selection
#           Minibatch
#           Display intermediate calculations
#           Overall, better design and better phython code :)
#

# External modules.
import numpy as np
import matplotlib.pylab as pl

# Modules specific to this program.
import get_data as gd
import init_network as ik
import training_iteration as ti

# Initialize the number of iterations to run and
# the size of the minibatch for each iteration.
iters = 200
minibatch = 1

# Get the input data and the expected output values.
inval, expected_val = gd.get_data()

# Initialize the network matrices.
A2, A3, A4, b2, b3, b4 = ik.init_network(inval.shape[1], expected_val.shape[1])

# Run the feedforward network.
yout = np.empty((iters,expected_val.shape[1],))
for i in range(iters):

    # One training iteration over the data in the minibatch.
    zout = ti.training_iteration(inval, expected_val, A2, A3, A4, b2, b3, b4, inval.shape[0], minibatch)
    
    # Save to plot later.
    for j in range(expected_val.shape[1]):
        yout[i][j] = zout[j]

# Plot some results
pl.plot(yout)
pl.show()