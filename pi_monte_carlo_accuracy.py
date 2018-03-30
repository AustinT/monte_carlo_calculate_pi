import numpy as np
import matplotlib.pyplot as plt
from pi_monte_carlo import estimate_pi

estimates = []
num_points_array = [int(i) for i in np.logspace(1, 6, 16)]

for num_pts in num_points_array:
    arr = []
    for i in range(20):
        arr.append(estimate_pi(num_pts))
    estimates.append(arr)
estimates = np.array(estimates)

estimates_mean = np.average(estimates, axis=1)
estimates_std = np.std(estimates, axis=1)

plt.plot(num_points_array, [np.pi]*len(num_points_array), 'k-')
plt.plot(num_points_array, estimates_mean, 'b-')
plt.fill_between(num_points_array, estimates_mean - estimates_std,
    estimates_mean + estimates_std, facecolor='b', alpha=0.2)
plt.title("Predicted pi value vs number of points in simulation"
          "\n(with std)")
plt.xscale('log')
plt.xlabel("Number of points")
plt.ylabel("Predicted Value of Pi")
plt.show()