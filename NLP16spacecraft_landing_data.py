"""Data and visualization for the spacecraft landing optimization project.

The optimization itself is intentionally not implemented here.
After solving it, call plot_trajectory(p, f), where
    p.shape == (3, K + 1)  # positions at discretization points
    f.shape == (3, K)      # thrust vectors during intervals
"""

import numpy as np
import matplotlib.pyplot as plt

# Model parameters (same values as in spacecraft_landing_data.m)
h = 1.0
g = 0.1
m = 10.0
Fmax = 10.0
p0 = np.array([50.0, 50.0, 100.0])
v0 = np.array([-10.0, 0.0, -10.0])
alpha = 0.5
gamma = 1.0
K = 35


def plot_trajectory(p, f):
    """Plot the glide cone, trajectory and thrust vectors (MATLAB equivalent).

    Parameters
    ----------
    p : array-like of shape (3, K + 1)
        Spacecraft positions at the K+1 discrete time points.
    f : array-like of shape (3, K)
        Thrust vectors applied during the K time intervals.
    """
    p = np.asarray(p, dtype=float)
    f = np.asarray(f, dtype=float)
    if p.shape != (3, K + 1):
        raise ValueError(f"Expected p.shape == (3, {K+1}), got {p.shape}")
    if f.shape != (3, K):
        raise ValueError(f"Expected f.shape == (3, {K}), got {f.shape}")

    # Plot the glide cone (equivalent to the supplied MATLAB plotting code).
    x = np.linspace(-40, 55, 30)
    y = np.linspace(0, 55, 30)
    X, Y = np.meshgrid(x, y)
    Z = alpha * np.sqrt(X**2 + Y**2)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="autumn", alpha=0.55,
                    linewidth=0, antialiased=True)
    ax.set_xlim(-40, 55)
    ax.set_ylim(0, 55)
    ax.set_zlim(0, 105)

    # Insert the optimized variables: positions p and thrust f.
    ax.plot(p[0, :], p[1, :], p[2, :], color="blue", linewidth=1.5,
            label="Trajectory")
    ax.quiver(p[0, :K], p[1, :K], p[2, :K],
              f[0, :], f[1, :], f[2, :],
              length=0.3, normalize=False, color="black", linewidth=1.0)

    ax.set_xlabel("p1")
    ax.set_ylabel("p2")
    ax.set_zlabel("p3")
    ax.set_title("Spacecraft landing trajectory and thrust")
    ax.legend()
    plt.tight_layout()
    plt.show()
    return fig, ax


# After solving the optimization problem, use:
# plot_trajectory(p, f)
