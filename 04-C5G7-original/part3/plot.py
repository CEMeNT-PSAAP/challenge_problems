import numpy as np
import matplotlib.pyplot as plt
import h5py, sys
from matplotlib import cm
from matplotlib import colors


# =============================================================================
# Plot results
# =============================================================================

# MPACT solution
data = np.loadtxt('mpact_output.txt')
t_ref = data[:,0]
phi_ref = data[:,1]

# Grids
with h5py.File("output.h5", "r") as f:
    t = f["tallies/mesh_tally_0/grid/t"][:]
    t_mid = 0.5 * (t[:-1] + t[1:])
    dt = t[1:] - t[:-1]

# Solution
with h5py.File("../part2/output.h5", "r") as f:
    norm = f["IC/fission"][()]
with h5py.File("output.h5", "r") as f:
    phi = f["tallies/mesh_tally_0/fission/mean"][:] / dt / norm
    phi_sd = f["tallies/mesh_tally_0/fission/sdev"][:] / dt / norm

plt.plot(t_ref, phi_ref,'r-', label='MPACT')
x = t_mid
y = phi
y_sd = phi_sd
plt.plot(x, y, 'bo', fillstyle='none',label='MC/DC')
plt.fill_between(x, y-y_sd, y+y_sd,alpha=0.2,color="b")
plt.xlim([0,8])
plt.xlabel('Time [s]')
plt.ylabel('Normalized fission rate')
plt.grid()
plt.legend()
#plt.savefig('C5G7-TD4-4.png', dpi=1200, bbox_inches='tight', pad_inches=0)
plt.show()
