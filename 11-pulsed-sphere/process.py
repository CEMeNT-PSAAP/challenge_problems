import matplotlib.pyplot as plt
import h5py

# Get results
with h5py.File("output.h5", "r") as f:
    t = f["tallies/mesh_tally_0/grid/t"][:]
    dt = t[1:] - t[:-1]
    t_mid = 0.5 * (t[1:] + t[:-1])
    K = len(t) - 1

    phi = f["tallies/mesh_tally_0/flux/mean"][:]
    phi_sd = f["tallies/mesh_tally_0/flux/sdev"][:]

    # Normalize
    for k in range(K):
        phi[k] /= dt[k]
        phi_sd[k] /= dt[k]
    
    t_cell = f["tallies/cell_tally_0/grid/t"][:]
    t_cell_mid = 0.5 * (t_cell[1:] + t_cell[:-1])
    dt_cell = t_cell[1:] - t_cell[:-1]
    K_cell = len(t) - 1
    phi_cell = f["tallies/cell_tally_0/flux/mean"][:]
    phi_cell_sd = f["tallies/cell_tally_0/flux/sdev"][:]

    # Normalize
    for k in range(K_cell):
        phi_cell[k] /= dt_cell[k]
        phi_cell_sd[k] /= dt_cell[k]

plt.plot(t_cell_mid, phi_cell)
plt.yscale("log")
plt.show()
