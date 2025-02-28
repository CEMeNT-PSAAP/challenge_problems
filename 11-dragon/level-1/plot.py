import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import h5py
import matplotlib.animation as animation


# =============================================================================
# Plot results
# =============================================================================

# Results
with h5py.File("output.h5", "r") as f:
    tallies = f["tallies/mesh_tally_0"]
    flux = tallies["flux"]
    fission = tallies["fission"]
    grid = tallies["grid"]
    z = grid["z"][:]
    z_mid = 0.5 * (z[:-1] + z[1:])
    y = grid["y"][:]
    y_mid = 0.5 * (y[:-1] + y[1:])
    t = grid["t"][:]
    t_mid = 0.5 * (t[:-1] + t[1:])
    t_mid = 0.5 * (t[:-1] + t[1:])
    Z, Y = np.meshgrid(y_mid, z_mid)

    # print(y_mid, x_mid)

    phi = flux["mean"][:]
    phi_sd = flux["sdev"][:]

    fission_rate = fission["mean"][:]


flux_max = np.max(phi)
fission_max = np.max(fission_rate)

# ============ ANIMATION ===================


fig, ax = plt.subplots()
cax1 = ax.pcolormesh(Z, Y, phi[0], vmin=0, vmax=flux_max)
text1 = ax.text(0.02, 1.02, "", transform=ax.transAxes)
ax.set_aspect("equal", "box")
ax.set_xlabel("$z$ [cm]")
ax.set_ylabel("$y$ [cm]")


def animate(i):
    cax1.set_array(phi[i])
    cax1.set_clim(0, flux_max)
    text1.set_text(r"$t \in [%.1f,%.1f]$ s" % (t[i], t[i + 1]))


anim = animation.FuncAnimation(fig, animate, interval=200, frames=len(t) - 1)
anim.save('dragon_flux.gif')





fig, ax = plt.subplots()
cax1 = ax.pcolormesh(Z, Y, fission_rate[0], vmin=0, vmax=fission_max)
text1 = ax.text(0.02, 1.02, "", transform=ax.transAxes)
ax.set_aspect("equal", "box")
ax.set_xlabel("$z$ [cm]")
ax.set_ylabel("$y$ [cm]")


def animate(i):
    cax1.set_array(fission_rate[i])
    cax1.set_clim(0, fission_max)
    text1.set_text(r"$t \in [%.1f,%.1f]$ s" % (t[i], t[i + 1]))


anim = animation.FuncAnimation(fig, animate, interval=200, frames=len(t) - 1)
anim.save('dragon_fission.gif')