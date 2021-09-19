## @file Plot.py
#  @author Mehak Khan
#  @brief Implements a library module for plotting points in 2D space
#  @date 3rd February 2021
#  @details The library module aids in plotting points on a graph with
#   the use of python's matplotlib

import matplotlib.pyplot as plt


## @brief Plots 3 graphs of motion simulation
#  @param w The list for the x and y coordinate values
#  @param t The list for the time values
def plot(w, t):
    if (not (len(w) == len(t))):
        raise ValueError
    x = []
    y = []
    for i in range(len(w)):
        x.append(w[i][0])
        y.append(w[i][1])

    graphs, ax = plt.subplots(3)
    graphs.suptitle("Motion Simulation")

    ax[0].plot(t, x)
    ax[1].plot(t, y)
    ax[2].plot(x, y)

    plots = ax.flat
    plots[0].set(ylabel='x(m)')
    plots[1].set(ylabel='y(m)')
    plots[2].set(ylabel='y(m)')
    plots[2].set(xlabel='x(m)')
    plt.show()
