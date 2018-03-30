import numpy as np
import matplotlib.pyplot as plt

def estimate_pi(n, plot=False):
    pts = np.random.random((n, 2))

    norm = np.linalg.norm(pts, axis=-1)
    frac_in_circle = np.average(norm <= 1)
    pi_est = frac_in_circle * 4
    
    if plot:
        plt.plot(pts[:, 0], pts[:, 1], ',')
        
        x = np.linspace(0, 1, 100)
        y = np.sqrt(1-x**2)
        plt.plot(x, y, 'g-')
        plt.fill_between(x, 0, y, facecolor='g', alpha=0.2)
        plt.title("Monte Carlo Estimate of Pi with {} points: {}".format(n, pi_est))
        
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    return pi_est
    
if __name__ == "__main__":
    n = int(input("Input a number of points to sample: "))
    estimate_pi(n, plot=True)