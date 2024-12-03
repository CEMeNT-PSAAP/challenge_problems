import numpy as np
import mcdc, math

# =============================================================================
# Materials
# =============================================================================

mat_uo2 = mcdc.material(
    [
        ["O16", 0.04585265389377734],
        ["O17", 1.7419604031574338e-05],
        ["O18", 9.19424166352541e-05],
        ["U235", 0.0007217486041189947],
        ["U238", 0.02224950230720295],
    ]
)
mat_mox43 = mcdc.material(
    [
        ["O16", 0.04589711643122753],
        ["O17", 1.743649552488715e-05],
        ["O18", 9.203157163056531e-05],
        ["U235", 0.0003750264168772414],
        ["U238", 0.02262319599228636],
    ]
)
mat_mox7 = mcdc.material(
    [
        ["O16", 0.04583036614158277],
        ["O17", 1.741113682662514e-05],
        ["O18", 9.189772587857765e-05],
        ["U235", 0.0005581382302893396],
        ["U238", 0.022404154012604437],
    ]
)
mat_mox87 = mcdc.material(
    [
        ["O16", 0.04585265389377734],
        ["O17", 1.7419604031574338e-05],
        ["O18", 9.19424166352541e-05],
        ["U235", 0.0007217486041189947],
        ["U238", 0.02224950230720295],
    ]
)
mat_gt = mcdc.material(
    [
        ["H1", 0.050347844752850625],
        ["H2", 7.842394716362082e-06],
        ["O16", 0.025117935412784034],
        ["O17", 9.542402714463945e-06],
        ["O18", 5.03657582849965e-05],
    ]
)
mat_fc = mcdc.material(
    [
        ["H1", 0.050347844752850625],
        ["H2", 7.842394716362082e-06],
        ["O16", 0.025117935412784034],
        ["O17", 9.542402714463945e-06],
        ["O18", 5.03657582849965e-05],
    ]
)
mat_cr = mcdc.material(
    [
        ['Ag107', 0.023523285675833942],
        ['Ag109', 0.02185429814297804],
        ['In113', 0.0003421922042655644],
        ['In115', 0.007651085167039375],
        ['Cd106', 3.38816276451386e-05],
        ['Cd108', 2.4166172970990425e-05],
        ['Cd110', 0.0003393605596264083],
        ['Cd111', 0.0003482051612205208],
        ['Cd112', 0.0006561061533306398],
        ['Cd113', 0.00033274751904988726],
        ['Cd114', 0.0007825159207295705],
        ['Cd116', 0.00020443276053837845],
    ]
)
mat_mod = mcdc.material(
    [
        ["H1", 0.050347844752850625],
        ["H2", 7.842394716362082e-06],
        ["O16", 0.025117935412784034],
        ["O17", 9.542402714463945e-06],
        ["O18", 5.03657582849965e-05],
    ]
)

# =============================================================================
# Pin cells
# =============================================================================

# Design parameters
pitch = 1.26
radius = 0.54
core_height = 128.52
reflector_thickness = 21.42

# Control rod banks fractions
#   All out: 0.0
#   All in : 1.0
cr1 = 0.854
cr2 = 0.0
cr3 = 0.0
cr4 = 0.65

# Tips of the control rod banks
cr1_bottom = core_height * (0.5 - cr1)
cr2_bottom = core_height * (0.5 - cr2)
cr3_bottom = core_height * (0.5 - cr3)
cr4_bottom = core_height * (0.5 - cr4)
cr1_top = cr1_bottom + core_height
cr2_top = cr2_bottom + core_height
cr3_top = cr3_bottom + core_height
cr4_top = cr4_bottom + core_height

# Surfaces
cy = mcdc.surface("cylinder-z", center=[0.0, 0.0], radius=radius)
# Control rod top and bottom tips
z1_top = mcdc.surface("plane-z", z=cr1_top)
z1_bottom = mcdc.surface("plane-z", z=cr1_bottom)
z2_top = mcdc.surface("plane-z", z=cr2_top)
z2_bottom = mcdc.surface("plane-z", z=cr2_bottom)
z3_top = mcdc.surface("plane-z", z=cr3_top)
z3_bottom = mcdc.surface("plane-z", z=cr3_bottom)
z4_top = mcdc.surface("plane-z", z=cr4_top)
z4_bottom = mcdc.surface("plane-z", z=cr4_bottom)
# Fuel top
#   (Bottom is bounded by the universe cell)
zf = mcdc.surface("plane-z", z=0.5 * core_height)

# Fission chamber pin
fc = mcdc.cell(-cy, mat_fc)
mod = mcdc.cell(+cy, mat_mod)
fission_chamber = mcdc.universe([fc, mod])

# Fuel rods
uo2 = mcdc.cell(-cy & -zf, mat_uo2)
mox4 = mcdc.cell(-cy & -zf, mat_mox43)
mox7 = mcdc.cell(-cy & -zf, mat_mox7)
mox8 = mcdc.cell(-cy & -zf, mat_mox87)
moda = mcdc.cell(-cy & +zf, mat_mod)  # Water above pin
fuel_uo2 = mcdc.universe([uo2, mod, moda])
fuel_mox43 = mcdc.universe([mox4, mod, moda])
fuel_mox7 = mcdc.universe([mox7, mod, moda])
fuel_mox87 = mcdc.universe([mox8, mod, moda])

# Control rods and guide tubes
cr1 = mcdc.cell(-cy & +z1_bottom & -z1_top, mat_cr)
gt1_lower = mcdc.cell(-cy & -z1_bottom, mat_gt)
gt1_upper = mcdc.cell(-cy & +z1_top, mat_gt)
#
cr2 = mcdc.cell(-cy & +z2_bottom & -z2_top, mat_cr)
gt2_lower = mcdc.cell(-cy & -z2_bottom, mat_gt)
gt2_upper = mcdc.cell(-cy & +z2_top, mat_gt)
#
cr3 = mcdc.cell(-cy & +z3_bottom & -z3_top, mat_cr)
gt3_lower = mcdc.cell(-cy & -z3_bottom, mat_gt)
gt3_upper = mcdc.cell(-cy & +z3_top, mat_gt)
#
cr4 = mcdc.cell(-cy & +z4_bottom & -z4_top, mat_cr)
gt4_lower = mcdc.cell(-cy & -z4_bottom, mat_gt)
gt4_upper = mcdc.cell(-cy & +z4_top, mat_gt)
#
control_rod1 = mcdc.universe([cr1, gt1_lower, gt1_upper, mod])
control_rod2 = mcdc.universe([cr2, gt2_lower, gt2_upper, mod])
control_rod3 = mcdc.universe([cr3, gt3_lower, gt3_upper, mod])
control_rod4 = mcdc.universe([cr4, gt4_lower, gt4_upper, mod])

# =============================================================================
# Fuel lattices
# =============================================================================

# UO2 lattice 1
u = fuel_uo2
c = control_rod1
f = fission_chamber
lattice_1 = mcdc.lattice(
    x=[-pitch * 17 / 2, pitch, 17],
    y=[-pitch * 17 / 2, pitch, 17],
    universes=[
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, c, u, u, c, u, u, c, u, u, u, u, u],
        [u, u, u, c, u, u, u, u, u, u, u, u, u, c, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, c, u, u, c, u, u, c, u, u, c, u, u, c, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, c, u, u, c, u, u, f, u, u, c, u, u, c, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, c, u, u, c, u, u, c, u, u, c, u, u, c, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, c, u, u, u, u, u, u, u, u, u, c, u, u, u],
        [u, u, u, u, u, c, u, u, c, u, u, c, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    ],
)

# MOX lattice 2
l = fuel_mox43
m = fuel_mox7
n = fuel_mox87
c = control_rod2
f = fission_chamber
lattice_2 = mcdc.lattice(
    x=[-pitch * 17 / 2, pitch, 17],
    y=[-pitch * 17 / 2, pitch, 17],
    universes=[
        [l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l],
        [l, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, l],
        [l, m, m, m, m, c, m, m, c, m, m, c, m, m, m, m, l],
        [l, m, m, c, m, n, n, n, n, n, n, n, m, c, m, m, l],
        [l, m, m, m, n, n, n, n, n, n, n, n, n, m, m, m, l],
        [l, m, c, n, n, c, n, n, c, n, n, c, n, n, c, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, c, n, n, c, n, n, f, n, n, c, n, n, c, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, c, n, n, c, n, n, c, n, n, c, n, n, c, m, l],
        [l, m, m, m, n, n, n, n, n, n, n, n, n, m, m, m, l],
        [l, m, m, c, m, n, n, n, n, n, n, n, m, c, m, m, l],
        [l, m, m, m, m, c, m, m, c, m, m, c, m, m, m, m, l],
        [l, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, l],
        [l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l],
    ],
)

# MOX lattice 3
l = fuel_mox43
m = fuel_mox7
n = fuel_mox87
c = control_rod3
f = fission_chamber
lattice_3 = mcdc.lattice(
    x=[-pitch * 17 / 2, pitch, 17],
    y=[-pitch * 17 / 2, pitch, 17],
    universes=[
        [l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l],
        [l, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, l],
        [l, m, m, m, m, c, m, m, c, m, m, c, m, m, m, m, l],
        [l, m, m, c, m, n, n, n, n, n, n, n, m, c, m, m, l],
        [l, m, m, m, n, n, n, n, n, n, n, n, n, m, m, m, l],
        [l, m, c, n, n, c, n, n, c, n, n, c, n, n, c, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, c, n, n, c, n, n, f, n, n, c, n, n, c, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, m, n, n, n, n, n, n, n, n, n, n, n, m, m, l],
        [l, m, c, n, n, c, n, n, c, n, n, c, n, n, c, m, l],
        [l, m, m, m, n, n, n, n, n, n, n, n, n, m, m, m, l],
        [l, m, m, c, m, n, n, n, n, n, n, n, m, c, m, m, l],
        [l, m, m, m, m, c, m, m, c, m, m, c, m, m, m, m, l],
        [l, m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, l],
        [l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l],
    ],
)

# UO2 lattice 4
u = fuel_uo2
c = control_rod4
f = fission_chamber
lattice_4 = mcdc.lattice(
    x=[-pitch * 17 / 2, pitch, 17],
    y=[-pitch * 17 / 2, pitch, 17],
    universes=[
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, c, u, u, c, u, u, c, u, u, u, u, u],
        [u, u, u, c, u, u, u, u, u, u, u, u, u, c, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, c, u, u, c, u, u, c, u, u, c, u, u, c, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, c, u, u, c, u, u, f, u, u, c, u, u, c, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, c, u, u, c, u, u, c, u, u, c, u, u, c, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, c, u, u, u, u, u, u, u, u, u, c, u, u, u],
        [u, u, u, u, u, c, u, u, c, u, u, c, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
        [u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u],
    ],
)

# =============================================================================
# Assemblies and core
# =============================================================================

# Surfaces
x0 = mcdc.surface("plane-x", x=0.0, bc="reflective")
x1 = mcdc.surface("plane-x", x=pitch * 17)
x2 = mcdc.surface("plane-x", x=pitch * 17 * 2)
x3 = mcdc.surface("plane-x", x=pitch * 17 * 3, bc="vacuum")

y0 = mcdc.surface("plane-y", y=-pitch * 17 * 3, bc="vacuum")
y1 = mcdc.surface("plane-y", y=-pitch * 17 * 2)
y2 = mcdc.surface("plane-y", y=-pitch * 17)
y3 = mcdc.surface("plane-y", y=0.0, bc="reflective")

z0 = mcdc.surface("plane-z", z=-(core_height / 2 + reflector_thickness), bc="vacuum")
z1 = mcdc.surface("plane-z", z=-(core_height / 2))
z2 = mcdc.surface("plane-z", z=(core_height / 2 + reflector_thickness), bc="vacuum")

# Assembly cells
center = np.array([pitch * 17 / 2, -pitch * 17 / 2, 0.0])
assembly_1 = mcdc.cell(+x0 & -x1 & +y2 & -y3 & +z1 & -z2, lattice_1, translation=center)

center += np.array([pitch * 17, 0.0, 0.0])
assembly_2 = mcdc.cell(+x1 & -x2 & +y2 & -y3 & +z1 & -z2, lattice_2, translation=center)

center += np.array([-pitch * 17, -pitch * 17, 0.0])
assembly_3 = mcdc.cell(+x0 & -x1 & +y1 & -y2 & +z1 & -z2, lattice_3, translation=center)

center += np.array([pitch * 17, 0.0, 0.0])
assembly_4 = mcdc.cell(+x1 & -x2 & +y1 & -y2 & +z1 & -z2, lattice_4, translation=center)

# Bottom reflector cell
reflector_bottom = mcdc.cell(+x0 & -x3 & +y0 & -y3 & +z0 & -z1, mat_mod)

# Side reflectors
reflector_south = mcdc.cell(+x0 & -x3 & +y0 & -y1 & +z1 & -z2, mat_mod)
reflector_east = mcdc.cell(+x2 & -x3 & +y1 & -y3 & +z1 & -z2, mat_mod)

# Root universe
mcdc.universe(
    [
        assembly_1,
        assembly_2,
        assembly_3,
        assembly_4,
        reflector_bottom,
        reflector_south,
        reflector_east,
    ],
    root=True,
)

# =============================================================================
# Set source
# =============================================================================
# In the center of Assembly one, at highest energy, for the first 15 seconds

mcdc.source(
    point=[pitch * 17 / 2, -pitch * 17 / 2, 0.0],
    energy=np.array([[1e6 - 1, 1e6 + 1], [1.0, 1.0]]),
    isotropic=True,
)

# =============================================================================
# Set tally, setting, and run mcdc
# =============================================================================

# Tally
mcdc.tally.mesh_tally(
    scores=["fission"],
    x=np.linspace(0.0, pitch * 17 * 2, 17 * 2 + 1),
    y=np.linspace(-pitch * 17 * 2, 0.0, 17 * 2 + 1),
    z=np.linspace(-(core_height / 2), (core_height / 2), int(math.ceil(core_height / pitch)) + 1),
)
mcdc.tally.mesh_tally(
    scores=["flux"],
    x=np.linspace(0.0, pitch * 17 * 3, 17 * 3 + 1),
    y=np.linspace(-pitch * 17 * 3, 0.0, 17 * 3 + 1),
    z=np.linspace(-(core_height / 2 + reflector_thickness), (core_height / 2 + reflector_thickness), int(math.ceil((core_height + 2.0 * reflector_thickness) / pitch)) + 1),
    E=np.array([0.0, 0.625, 2e7]),
)

# Setting
mcdc.setting(N_particle=1e5)
mcdc.eigenmode(N_inactive=30, N_active=50, gyration_radius="all")
mcdc.population_control()

# Run
mcdc.run()
