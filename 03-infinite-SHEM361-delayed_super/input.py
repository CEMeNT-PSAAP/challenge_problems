import numpy as np
import mcdc

# =============================================================================
# Set model
# =============================================================================
# The infinite homogenous medium is modeled with reflecting slab

# Materials
with np.load("SHEM-361.npz") as data:
    SigmaC = data["SigmaC"] * 1.27  # /cm
    SigmaS = data["SigmaS"]
    SigmaF = data["SigmaF"]
    nu_p = data["nu_p"]
    nu_d = data["nu_d"]
    chi_p = data["chi_p"]
    chi_d = data["chi_d"]
    G = data["G"]
    speed = data["v"]
    lamd = data["lamd"]
#
m = mcdc.material(
    capture=SigmaC,
    scatter=SigmaS,
    fission=SigmaF,
    nu_p=nu_p,
    chi_p=chi_p,
    nu_d=nu_d,
    chi_d=chi_d,
    decay=lamd,
    speed=speed,
)

# Surfaces
s1 = mcdc.surface("plane-x", x=-1e10, bc="reflective")
s2 = mcdc.surface("plane-x", x=1e10, bc="reflective")

# Cells
c = mcdc.cell(+s1 & -s2, m)

# =============================================================================
# Set source
# =============================================================================
# At highest group

energy = np.zeros(G)
energy[-1] = 1.0
source = mcdc.source(energy=energy)

# =============================================================================
# Set tally, setting, and run mcdc
# =============================================================================

time_grid = np.insert(np.logspace(-8, 1, 100), 0, 0.0)

# Tally
mcdc.tally.mesh_tally(
    scores=["flux"], t=time_grid, g="all"
)
mcdc.tally.mesh_tally(
    scores=["density"],
    t=time_grid,
)

# Setting
mcdc.setting(N_particle=1e3, active_bank_buff=10000)

# Run
mcdc.run()
