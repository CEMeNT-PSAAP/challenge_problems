import mcdc, h5py, math
import numpy as np

# ======================================================================================
# Materials
# ======================================================================================

# Load material data
lib = h5py.File("../../data/MGXS-C5G7.h5", "r")

# Setter
def set_mat(mat, frac):
    capture = mat[0]['capture'][:] * frac[0]
    scatter = mat[0]['scatter'][:] * frac[0]
    fission = mat[0]['fission'][:] * frac[0]
    nu_p = mat[0]['nu_p'][:] * frac[0]
    nu_d = mat[0]['nu_d'][:] * frac[0]
    chi_p = mat[0]['chi_p'][:] * frac[0]
    chi_d = mat[0]['chi_d'][:] * frac[0]
    speed = mat[0]['speed'][:] * frac[0]
    decay = mat[0]['decay'][:] * frac[0]
    for i in range(1, len(mat)):
        capture += mat[i]['capture'][:] * frac[i]
        scatter += mat[i]['scatter'][:] * frac[i]
        fission += mat[i]['fission'][:] * frac[i]
        nu_p += mat[i]['nu_p'][:] * frac[i]
        nu_d += mat[i]['nu_d'][:] * frac[i]
        chi_p += mat[i]['chi_p'][:] * frac[i]
        chi_d += mat[i]['chi_d'][:] * frac[i]
        speed += mat[i]['speed'][:] * frac[i]
        decay += mat[i]['decay'][:] * frac[i]
    return mcdc.material(
        capture=capture,
        scatter=scatter,
        fission=fission,
        nu_p=nu_p,
        nu_d=nu_d,
        chi_p=chi_p,
        chi_d=chi_d,
        speed=speed,
        decay=decay,
    )

# Materials
m_helium = set_mat([lib["gt"]], [1.0])
m_inconel = set_mat([lib["gt"]], [1.0])
m_ss302 = set_mat([lib["gt"]], [1.0])
m_ss304 = set_mat([lib["gt"]], [1.0])
m_csteel = set_mat([lib["gt"]], [1.0])
m_zr4 = set_mat([lib["gt"]], [1.0])
m_m5 = set_mat([lib["gt"]], [1.0])
m_water = set_mat([lib["mod"], lib['cr']], [0.97, 0.03])
m_fuel31 = set_mat([lib["uo2"]], [1.0])
m_fuel24 = set_mat([lib["mox87"]], [1.0])
m_fuel16 = set_mat([lib["mox43"]], [1.0])
m_cr = set_mat([lib["cr"]], [2.0])

# ======================================================================================
# Geometry
# ======================================================================================

# --------------------------------------------------------------------------------------
# Surfaces
# --------------------------------------------------------------------------------------

s1 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.405765) # Name: Pellet OR
s2 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.06459) # Name: FR Plenum Spring OR
s3 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.41402) # Name: Clad IR
s4 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.47498) # Name: Clad OR
s5 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.5715) # Name: GT IR (above dashpot)
s6 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.61214) # Name: GT OR (above dashpot)
s7 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.50419) # Name: GT IR (at dashpot)
s8 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=0.61214) # Name: GT OR (at dashpot)
s20 = mcdc.surface('plane-x', x=-0.62208) # Name: minimum x
s21 = mcdc.surface('plane-x', x=0.62208) # Name: maximum x
s22 = mcdc.surface('plane-y', y=-0.62208) # Name: minimum y
s23 = mcdc.surface('plane-y', y=0.62208) # Name: maximum y
s24 = mcdc.surface('plane-x', x=-10.70864) # Name: minimum x
s25 = mcdc.surface('plane-x', x=10.70864) # Name: maximum x
s26 = mcdc.surface('plane-y', y=-10.70864) # Name: minimum y
s27 = mcdc.surface('plane-y', y=10.70864) # Name: maximum y
s28 = mcdc.surface('plane-x', x=-10.73635) # Name: minimum x
s29 = mcdc.surface('plane-x', x=10.73635) # Name: maximum x
s30 = mcdc.surface('plane-y', y=-10.73635) # Name: minimum y
s31 = mcdc.surface('plane-y', y=10.73635) # Name: maximum y
s32 = mcdc.surface('plane-z', z=-16.6205) # Name: bot support plate
s33 = mcdc.surface('plane-z', z=-11.6205) # Name: top support plate
s34 = mcdc.surface('plane-z', z=-1.4604999999999997) # Name: bottom FR
s35 = mcdc.surface('plane-z', z=2.220446049250313e-16) # Name: bot active core
s36 = mcdc.surface('plane-z', z=199.9996) # Name: top active core
s38 = mcdc.surface('plane-z', z=4.5395) # Name: bottom grid 1
s39 = mcdc.surface('plane-z', z=8.9845) # Name: top of grid 1
s40 = mcdc.surface('plane-z', z=55.40325) # Name: bottom grid 2
s41 = mcdc.surface('plane-z', z=59.84825) # Name: top of grid 2
s42 = mcdc.surface('plane-z', z=106.26700000000001) # Name: bottom grid 3
s43 = mcdc.surface('plane-z', z=110.71200000000002) # Name: top of grid 3
s44 = mcdc.surface('plane-z', z=157.13075) # Name: bottom grid 4
s45 = mcdc.surface('plane-z', z=161.57575) # Name: top of grid 4
s46 = mcdc.surface('plane-z', z=207.99450000000002) # Name: bottom grid 5
s47 = mcdc.surface('plane-z', z=212.4395) # Name: top of grid 5
s48 = mcdc.surface('plane-z', z=46.079) # Name: top dashpot
s49 = mcdc.surface('plane-z', z=213.48953999999998) # Name: top pin plenum
s50 = mcdc.surface('plane-z', z=214.4395) # Name: top FR
s51 = mcdc.surface('plane-z', z=217.78449999999998) # Name: bottom upper nozzle
s52 = mcdc.surface('plane-z', z=226.61149999999998) # Name: top upper nozzle
s71 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=93.98) # Name: core barrel IR
s72 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=99.06) # Name: core barrel OR
s78 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=122.555) # Name: RPV IR
s79 = mcdc.surface('cylinder-z', center=[0.0, 0.0], radius=133.35, bc='vacuum') # Name: RPV OR
s80 = mcdc.surface('plane-z', z=246.61149999999998, bc='vacuum') # Name: upper problem boundary
s81 = mcdc.surface('plane-z', z=-36.6205, bc='vacuum') # Name: lower problem boundary
s82 = mcdc.surface('cylinder-z', center=[-9.816879130434781, -6.155027391304348], radius=0.506426304347826)
s83 = mcdc.surface('cylinder-z', center=[-4.518880869565217, -6.155027391304348], radius=0.506426304347826)
s84 = mcdc.surface('cylinder-z', center=[0.9349408695652173, -6.155027391304348], radius=0.506426304347826)
s85 = mcdc.surface('cylinder-z', center=[6.155027391304348, -6.155027391304348], radius=1.1686760869565216)
s86 = mcdc.surface('cylinder-z', center=[6.155027391304348, -0.9349408695652173], radius=0.506426304347826)
s87 = mcdc.surface('cylinder-z', center=[6.155027391304348, 4.518880869565216], radius=0.506426304347826)
s88 = mcdc.surface('cylinder-z', center=[6.155027391304348, 9.816879130434781], radius=0.506426304347826)
s89 = mcdc.surface('cylinder-z', center=[2.5710873913043475, -2.5710873913043475], radius=0.506426304347826)
s90 = mcdc.surface('cylinder-z', center=[-2.0257052173913053, -1.246587826086957], radius=0.506426304347826)
s91 = mcdc.surface('cylinder-z', center=[1.2465878260869552, 2.0257052173913035], radius=0.506426304347826)
s92 = mcdc.surface('cylinder-z', center=[-6.544586086956521, 0.0], radius=0.506426304347826)
s93 = mcdc.surface('cylinder-z', center=[0.0, 6.544586086956521], radius=0.506426304347826)
s94 = mcdc.surface('cylinder-z', center=[-9.816879130434781, 8.49237956521739], radius=0.506426304347826)
s95 = mcdc.surface('cylinder-z', center=[6.155027391304348, -6.155027391304348], radius=0.506426304347826)
s96 = mcdc.surface('cylinder-z', center=[2.726910869565218, 1.402411304347826], radius=0.506426304347826)
s97 = mcdc.surface('cylinder-z', center=[-1.5582347826086949, -2.726910869565218], radius=0.506426304347826)
s98 = mcdc.surface('cylinder-z', center=[6.232939130434779, 0.0], radius=0.506426304347826)
s99 = mcdc.surface('cylinder-z', center=[6.232939130434779, 5.2200865217391295], radius=0.506426304347826)
s100 = mcdc.surface('cylinder-z', center=[6.232939130434779, 10.440173043478259], radius=0.506426304347826)
s101 = mcdc.surface('cylinder-z', center=[6.232939130434779, -5.2200865217391295], radius=0.506426304347826)
s102 = mcdc.surface('cylinder-z', center=[6.232939130434779, -10.440173043478259], radius=0.506426304347826)
s103 = mcdc.surface('cylinder-z', center=[1.5582347826086949, 2.6100432608695647], radius=0.506426304347826)
s104 = mcdc.surface('cylinder-z', center=[1.5582347826086949, 7.830129782608694], radius=0.506426304347826)
s105 = mcdc.surface('cylinder-z', center=[1.5582347826086949, -2.6100432608695647], radius=0.506426304347826)
s106 = mcdc.surface('cylinder-z', center=[1.5582347826086949, -7.830129782608694], radius=0.506426304347826)
s107 = mcdc.surface('cylinder-z', center=[-2.726910869565218, 5.921292173913042], radius=0.506426304347826)
s108 = mcdc.surface('cylinder-z', center=[-2.726910869565218, -5.921292173913042], radius=0.506426304347826)
s109 = mcdc.surface('cylinder-z', center=[6.232939130434779, -11.063466956521738], radius=0.506426304347826)
s110 = mcdc.surface('cylinder-z', center=[6.232939130434779, -5.84338043478261], radius=0.506426304347826)
s111 = mcdc.surface('cylinder-z', center=[6.232939130434779, -0.6232939130434794], radius=0.506426304347826)
s112 = mcdc.surface('cylinder-z', center=[6.232939130434779, 4.596792608695651], radius=0.506426304347826)
s113 = mcdc.surface('cylinder-z', center=[6.232939130434779, 9.816879130434778], radius=0.506426304347826)
s114 = mcdc.surface('cylinder-z', center=[1.5582347826086949, -8.453423695652173], radius=0.506426304347826)
s115 = mcdc.surface('cylinder-z', center=[1.5582347826086949, -3.2333371739130428], radius=0.506426304347826)
s116 = mcdc.surface('cylinder-z', center=[1.5582347826086949, 7.206835869565214], radius=0.506426304347826)
s117 = mcdc.surface('cylinder-z', center=[-0.15582347826087073, 1.6361465217391302], radius=0.506426304347826)
s118 = mcdc.surface('cylinder-z', center=[-3.5060282608695648, -7.089968260869565], radius=0.506426304347826)
s119 = mcdc.surface('cylinder-z', center=[6.232939130434779, 11.063466956521738], radius=0.506426304347826)
s120 = mcdc.surface('cylinder-z', center=[6.232939130434779, 5.84338043478261], radius=0.506426304347826)
s121 = mcdc.surface('cylinder-z', center=[6.232939130434779, 0.6232939130434794], radius=0.506426304347826)
s122 = mcdc.surface('cylinder-z', center=[6.232939130434779, -4.596792608695651], radius=0.506426304347826)
s123 = mcdc.surface('cylinder-z', center=[6.232939130434779, -9.816879130434778], radius=0.506426304347826)
s124 = mcdc.surface('cylinder-z', center=[1.5582347826086949, 8.453423695652173], radius=0.506426304347826)
s125 = mcdc.surface('cylinder-z', center=[1.5582347826086949, 3.2333371739130428], radius=0.506426304347826)
s126 = mcdc.surface('cylinder-z', center=[1.5582347826086949, -7.206835869565214], radius=0.506426304347826)
s127 = mcdc.surface('cylinder-z', center=[-0.15582347826087073, -1.6361465217391302], radius=0.506426304347826)
s128 = mcdc.surface('cylinder-z', center=[-3.5060282608695648, 7.089968260869565], radius=0.506426304347826)
s129 = mcdc.surface('cylinder-z', center=[4.674704347826085, -3.1164695652173915], radius=0.506426304347826)

# --------------------------------------------------------------------------------------
# Moving control rods
# --------------------------------------------------------------------------------------

config = {}

# Design spec.
config['top'] = 199.9996
config['bottom'] = 2.220446049250313e-16
config['length'] = config['top'] - config['bottom']

# Problem spec.
config['time'] = 0.0
config['frac_r'] = 1.0
config['frac_rx'] = 1.0
config['frac_s'] = 1.0
config['frac_sx2'] = 0.65
config['frac_sx3'] = 1.0
cases = ['r', 'rx', 's', 'sx2', 'sx3']

# All cases
for case in cases:
    # The CR tip positions
    z_top = config['top'] + (1.0 - config[f'frac_{case}']) * config['length']
    z_bottom = z_top - config['length']

    # The CR tip surfaces
    s_top = mcdc.surface("plane-z", z=z_top)
    s_bottom = mcdc.surface("plane-z", z=z_bottom)

    # CR region
    cr_region = +s_bottom & -s_top

    # CR and water cells
    cell_cr = mcdc.cell(cr_region, fill=m_cr)
    cell_water = mcdc.cell(~cr_region, fill=m_water)

    # Universe
    univ_cr_water = mcdc.universe([cell_cr, cell_water])

    # Universe cells
    config[f'cell_cr_water_{case}'] = mcdc.cell(fill=univ_cr_water)
    config[f'cell_cr_water_tube_{case}'] = mcdc.cell(-s5, fill=univ_cr_water)
    config[f'cell_cr_water_dashpot_{case}'] = mcdc.cell(-s7, fill=univ_cr_water)

    # Continue to Moving control rods - Level 1

# --------------------------------------------------------------------------------------
# Cells - Level 0
# --------------------------------------------------------------------------------------

c1 = mcdc.cell(fill=m_water) # Name: water pin
c2 = mcdc.cell(-s5, fill=m_water) # Name: GT empty (0)
c3 = mcdc.cell(+s5 & -s6, fill=m_zr4) # Name: GT empty (1)
c4 = mcdc.cell(+s6, fill=m_water) # Name: GT empty (last)
c5 = mcdc.cell(-s5, fill=m_water) # Name: GT empty grid (bottom) (0)
c6 = mcdc.cell(+s5 & -s6, fill=m_zr4) # Name: GT empty grid (bottom) (1)
c7 = mcdc.cell(+s6 & +s20 & -s21 & +s22 & -s23, fill=m_water) # Name: GT empty grid (bottom) (last)
c8 = mcdc.cell(-s20 | +s21 | -s22 | +s23, fill=m_inconel) # Name: GT empty grid (bottom) (grid)
c9 = mcdc.cell(-s5, fill=m_water) # Name: GT empty grid (intermediate) (0)
c10 = mcdc.cell(+s5 & -s6, fill=m_zr4) # Name: GT empty grid (intermediate) (1)
c11 = mcdc.cell(+s6 & +s20 & -s21 & +s22 & -s23, fill=m_water) # Name: GT empty grid (intermediate) (last)
c12 = mcdc.cell(-s20 | +s21 | -s22 | +s23, fill=m_zr4) # Name: GT empty grid (intermediate) (grid)
c16 = mcdc.cell(-s7, fill=m_water) # Name: GT empty at dashpot (0)
c17 = mcdc.cell(+s7 & -s8, fill=m_zr4) # Name: GT empty at dashpot (1)
c18 = mcdc.cell(+s8, fill=m_water) # Name: GT empty at dashpot (last)
c19 = mcdc.cell(-s7, fill=m_water) # Name: GT empty at dashpot grid (bottom) (0)
c20 = mcdc.cell(+s7 & -s8, fill=m_zr4) # Name: GT empty at dashpot grid (bottom) (1)
c21 = mcdc.cell(+s8 & +s20 & -s21 & +s22 & -s23, fill=m_water) # Name: GT empty at dashpot grid (bottom) (last)
c22 = mcdc.cell(-s20 | +s21 | -s22 | +s23, fill=m_inconel) # Name: GT empty at dashpot grid (bottom) (grid)
c585 = mcdc.cell(-s4, fill=m_ss304) # Name: SS pin (0)
c586 = mcdc.cell(+s4, fill=m_water) # Name: SS pin (last)
c587 = mcdc.cell(-s4, fill=m_m5) # Name: end plug (0)
c588 = mcdc.cell(+s4, fill=m_water) # Name: end plug (last)
c589 = mcdc.cell(-s2, fill=m_ss302) # Name: pin plenum (0)
c590 = mcdc.cell(+s2 & -s3, fill=m_helium) # Name: pin plenum (1)
c591 = mcdc.cell(+s3 & -s4, fill=m_m5) # Name: pin plenum (2)
c592 = mcdc.cell(+s4, fill=m_water) # Name: pin plenum (last)
c593 = mcdc.cell(-s2, fill=m_inconel) # Name: pin plenum grid (intermediate) (0)
c594 = mcdc.cell(+s2 & -s3, fill=m_helium) # Name: pin plenum grid (intermediate) (1)
c595 = mcdc.cell(+s3 & -s4, fill=m_zr4) # Name: pin plenum grid (intermediate) (2)
c596 = mcdc.cell(+s4 & +s20 & -s21 & +s22 & -s23, fill=m_water) # Name: pin plenum grid (intermediate) (last)
c597 = mcdc.cell(-s20 | +s21 | -s22 | +s23, fill=m_zr4) # Name: pin plenum grid (intermediate) (grid)
c598 = mcdc.cell(-s3, fill=m_helium) # Name: Outside pin (0)
c599 = mcdc.cell(+s3 & -s4, fill=m_m5) # Name: Outside pin (1)
c600 = mcdc.cell(+s4, fill=m_water) # Name: Outside pin (last)
c601 = mcdc.cell(-s3, fill=m_helium) # Name: Outside pin grid (bottom) (0)
c602 = mcdc.cell(+s3 & -s4, fill=m_m5) # Name: Outside pin grid (bottom) (1)
c603 = mcdc.cell(+s4 & +s20 & -s21 & +s22 & -s23, fill=m_water) # Name: Outside pin grid (bottom) (last)
c604 = mcdc.cell(-s20 | +s21 | -s22 | +s23, fill=m_inconel) # Name: Outside pin grid (bottom) (grid)
c605 = mcdc.cell(-s3, fill=m_helium) # Name: Outside pin grid (intermediate) (0)
c606 = mcdc.cell(+s3 & -s4, fill=m_m5) # Name: Outside pin grid (intermediate) (1)
c607 = mcdc.cell(+s4 & +s20 & -s21 & +s22 & -s23, fill=m_water) # Name: Outside pin grid (intermediate) (last)
c608 = mcdc.cell(-s20 | +s21 | -s22 | +s23, fill=m_zr4) # Name: Outside pin grid (intermediate) (grid)
c623 = mcdc.cell(-s1, fill=m_fuel16) # Name: Fuel pin (1.6%) stack (i)
c650 = mcdc.cell(-s1, fill=m_fuel24) # Name: Fuel pin (2.4%) stack (i)
c677 = mcdc.cell(-s1, fill=m_fuel31) # Name: Fuel pin (3.1%) stack (i)
c691 = mcdc.cell(-s28 | +s29 | -s30 | +s31, fill=m_water) # Name: Assembly (1.6%) no BAs lattice outer water
c692 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & -s38, fill=m_water) # Name: Assembly (1.6%) no BAs lattice axial (0)
c693 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s38 & -s39, fill=m_inconel) # Name: Assembly (1.6%) no BAs lattice axial (1)
c694 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s39 & -s40, fill=m_water) # Name: Assembly (1.6%) no BAs lattice axial (2)
c695 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s40 & -s41, fill=m_zr4) # Name: Assembly (1.6%) no BAs lattice axial (3)
c696 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s41 & -s42, fill=m_water) # Name: Assembly (1.6%) no BAs lattice axial (4)
c697 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s42 & -s43, fill=m_zr4) # Name: Assembly (1.6%) no BAs lattice axial (5)
c698 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s43 & -s44, fill=m_water) # Name: Assembly (1.6%) no BAs lattice axial (6)
c699 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s44 & -s45, fill=m_zr4) # Name: Assembly (1.6%) no BAs lattice axial (7)
c700 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s45 & -s46, fill=m_water) # Name: Assembly (1.6%) no BAs lattice axial (8)
c701 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s46 & -s47, fill=m_zr4) # Name: Assembly (1.6%) no BAs lattice axial (9)
c702 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s47, fill=m_water) # Name: Assembly (1.6%) no BAs lattice axial (last)
c925 = mcdc.cell(-s28 | +s29 | -s30 | +s31, fill=m_water) # Name: Assembly (2.4%) no BAs lattice outer water
c926 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & -s38, fill=m_water) # Name: Assembly (2.4%) no BAs lattice axial (0)
c927 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s38 & -s39, fill=m_inconel) # Name: Assembly (2.4%) no BAs lattice axial (1)
c928 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s39 & -s40, fill=m_water) # Name: Assembly (2.4%) no BAs lattice axial (2)
c929 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s40 & -s41, fill=m_zr4) # Name: Assembly (2.4%) no BAs lattice axial (3)
c930 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s41 & -s42, fill=m_water) # Name: Assembly (2.4%) no BAs lattice axial (4)
c931 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s42 & -s43, fill=m_zr4) # Name: Assembly (2.4%) no BAs lattice axial (5)
c932 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s43 & -s44, fill=m_water) # Name: Assembly (2.4%) no BAs lattice axial (6)
c933 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s44 & -s45, fill=m_zr4) # Name: Assembly (2.4%) no BAs lattice axial (7)
c934 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s45 & -s46, fill=m_water) # Name: Assembly (2.4%) no BAs lattice axial (8)
c935 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s46 & -s47, fill=m_zr4) # Name: Assembly (2.4%) no BAs lattice axial (9)
c936 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s47, fill=m_water) # Name: Assembly (2.4%) no BAs lattice axial (last)
c977 = mcdc.cell(-s28 | +s29 | -s30 | +s31, fill=m_water) # Name: Assembly (3.1%) no BAs lattice outer water
c978 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & -s38, fill=m_water) # Name: Assembly (3.1%) no BAs lattice axial (0)
c979 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s38 & -s39, fill=m_inconel) # Name: Assembly (3.1%) no BAs lattice axial (1)
c980 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s39 & -s40, fill=m_water) # Name: Assembly (3.1%) no BAs lattice axial (2)
c981 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s40 & -s41, fill=m_zr4) # Name: Assembly (3.1%) no BAs lattice axial (3)
c982 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s41 & -s42, fill=m_water) # Name: Assembly (3.1%) no BAs lattice axial (4)
c983 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s42 & -s43, fill=m_zr4) # Name: Assembly (3.1%) no BAs lattice axial (5)
c984 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s43 & -s44, fill=m_water) # Name: Assembly (3.1%) no BAs lattice axial (6)
c985 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s44 & -s45, fill=m_zr4) # Name: Assembly (3.1%) no BAs lattice axial (7)
c986 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s45 & -s46, fill=m_water) # Name: Assembly (3.1%) no BAs lattice axial (8)
c987 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s46 & -s47, fill=m_zr4) # Name: Assembly (3.1%) no BAs lattice axial (9)
c988 = mcdc.cell(+s28 & -s29 & +s30 & -s31 & (-s24 | +s25 | -s26 | +s27) & +s47, fill=m_water) # Name: Assembly (3.1%) no BAs lattice axial (last)
c1028 = mcdc.cell(-s82, fill=m_water)
c1029 = mcdc.cell(-s83, fill=m_water)
c1030 = mcdc.cell(-s84, fill=m_water)
c1031 = mcdc.cell(-s85, fill=m_water)
c1032 = mcdc.cell(-s86, fill=m_water)
c1033 = mcdc.cell(-s87, fill=m_water)
c1034 = mcdc.cell(-s88, fill=m_water)
c1035 = mcdc.cell(-s89, fill=m_water)
c1036 = mcdc.cell(-s90, fill=m_water)
c1037 = mcdc.cell(-s91, fill=m_water)
c1038 = mcdc.cell(-s92, fill=m_water)
c1039 = mcdc.cell(-s93, fill=m_water)
c1040 = mcdc.cell(-s94, fill=m_water)
c1041 = mcdc.cell(+s82 & +s83 & +s84 & +s85 & +s86 & +s87 & +s88 & +s89 & +s90 & +s91 & +s92 & +s93 & +s94, fill=m_ss304) # Name: reflector NW SS
c1042 = mcdc.cell(-s95, fill=m_water)
c1043 = mcdc.cell(-s96, fill=m_water)
c1044 = mcdc.cell(-s97, fill=m_water)
c1045 = mcdc.cell(+s95 & +s96 & +s97, fill=m_ss304) # Name: reflector 1,1 SS
c1046 = mcdc.cell(-s98, fill=m_water)
c1047 = mcdc.cell(-s99, fill=m_water)
c1048 = mcdc.cell(-s100, fill=m_water)
c1049 = mcdc.cell(-s101, fill=m_water)
c1050 = mcdc.cell(-s102, fill=m_water)
c1051 = mcdc.cell(-s103, fill=m_water)
c1052 = mcdc.cell(-s104, fill=m_water)
c1053 = mcdc.cell(-s105, fill=m_water)
c1054 = mcdc.cell(-s106, fill=m_water)
c1055 = mcdc.cell(-s107, fill=m_water)
c1056 = mcdc.cell(-s108, fill=m_water)
c1057 = mcdc.cell(+s98 & +s99 & +s100 & +s101 & +s102 & +s103 & +s104 & +s105 & +s106 & +s107 & +s108, fill=m_ss304) # Name: reflector 4,0 SS
c1058 = mcdc.cell(-s109, fill=m_water)
c1059 = mcdc.cell(-s110, fill=m_water)
c1060 = mcdc.cell(-s111, fill=m_water)
c1061 = mcdc.cell(-s112, fill=m_water)
c1062 = mcdc.cell(-s113, fill=m_water)
c1063 = mcdc.cell(-s114, fill=m_water)
c1064 = mcdc.cell(-s115, fill=m_water)
c1065 = mcdc.cell(-s116, fill=m_water)
c1066 = mcdc.cell(-s117, fill=m_water)
c1067 = mcdc.cell(-s118, fill=m_water)
c1068 = mcdc.cell(+s109 & +s110 & +s111 & +s112 & +s113 & +s114 & +s115 & +s116 & +s117 & +s118, fill=m_ss304) # Name: reflector 3,0 SS
c1069 = mcdc.cell(-s119, fill=m_water)
c1070 = mcdc.cell(-s120, fill=m_water)
c1071 = mcdc.cell(-s121, fill=m_water)
c1072 = mcdc.cell(-s122, fill=m_water)
c1073 = mcdc.cell(-s123, fill=m_water)
c1074 = mcdc.cell(-s124, fill=m_water)
c1075 = mcdc.cell(-s125, fill=m_water)
c1076 = mcdc.cell(-s126, fill=m_water)
c1077 = mcdc.cell(-s127, fill=m_water)
c1078 = mcdc.cell(-s128, fill=m_water)
c1079 = mcdc.cell(+s119 & +s120 & +s121 & +s122 & +s123 & +s124 & +s125 & +s126 & +s127 & +s128, fill=m_ss304) # Name: reflector 5,0 SS
c1080 = mcdc.cell(-s129, fill=m_water)
c1081 = mcdc.cell(+s129, fill=m_ss304) # Name: reflector 2,0 SS
c1104 = mcdc.cell(fill=m_ss304) # Name: heavy reflector
c1106 = mcdc.cell(+s71 & -s72 & +s81 & -s80, fill=m_ss304) # Name: core barrel
c1107 = mcdc.cell(+s72 & -s78 & +s81 & -s80, fill=m_water) # Name: downcomer
c1108 = mcdc.cell(+s78 & -s79 & +s81 & -s80, fill=m_csteel) # Name: reactor pressure vessel

# --------------------------------------------------------------------------------------
# Universes - Level 1
# --------------------------------------------------------------------------------------

u1 = mcdc.universe([c1])
u150 = mcdc.universe([c1028, c1029, c1030, c1031, c1032, c1033, c1034, c1035, c1036, c1037, c1038, c1039, c1040, c1041])
u151 = mcdc.universe([c1042, c1043, c1044, c1045])
u152 = mcdc.universe([c1046, c1047, c1048, c1049, c1050, c1051, c1052, c1053, c1054, c1055, c1056, c1057])
u153 = mcdc.universe([c1058, c1059, c1060, c1061, c1062, c1063, c1064, c1065, c1066, c1067, c1068])
u154 = mcdc.universe([c1069, c1070, c1071, c1072, c1073, c1074, c1075, c1076, c1077, c1078, c1079])
u155 = mcdc.universe([c1080, c1081])
u178 = mcdc.universe([c1104])
u2 = mcdc.universe([c2, c3, c4])
u3 = mcdc.universe([c5, c6, c7, c8])
u4 = mcdc.universe([c9, c10, c11, c12])
u6 = mcdc.universe([c16, c17, c18])
u7 = mcdc.universe([c19, c20, c21, c22])
u82 = mcdc.universe([c585, c586])
u83 = mcdc.universe([c587, c588])
u84 = mcdc.universe([c589, c590, c591, c592])
u85 = mcdc.universe([c593, c594, c595, c596, c597])
u86 = mcdc.universe([c598, c599, c600])
u87 = mcdc.universe([c601, c602, c603, c604])
u88 = mcdc.universe([c605, c606, c607, c608])

# --------------------------------------------------------------------------------------
# Cells - Level 1
# --------------------------------------------------------------------------------------

c30 = mcdc.cell(-s32, fill=u1) # Name: GT empty stack (0)
c31 = mcdc.cell(+s32 & -s33, fill=u1) # Name: GT empty stack (1)
c32 = mcdc.cell(+s33 & -s34, fill=u1) # Name: GT empty stack (2)
c33 = mcdc.cell(+s34 & -s35, fill=u6) # Name: GT empty stack (3)
c34 = mcdc.cell(+s35 & -s38, fill=u6) # Name: GT empty stack (4)
c35 = mcdc.cell(+s38 & -s39, fill=u7) # Name: GT empty stack (5)
c36 = mcdc.cell(+s39 & -s48, fill=u6) # Name: GT empty stack (6)
c37 = mcdc.cell(+s48 & -s40, fill=u2) # Name: GT empty stack (7)
c38 = mcdc.cell(+s40 & -s41, fill=u4) # Name: GT empty stack (8)
c39 = mcdc.cell(+s41 & -s42, fill=u2) # Name: GT empty stack (9)
c40 = mcdc.cell(+s42 & -s43, fill=u4) # Name: GT empty stack (10)
c41 = mcdc.cell(+s43 & -s44, fill=u2) # Name: GT empty stack (11)
c42 = mcdc.cell(+s44 & -s45, fill=u4) # Name: GT empty stack (12)
c43 = mcdc.cell(+s45 & -s36, fill=u2) # Name: GT empty stack (13)
c44 = mcdc.cell(+s36 & -s46, fill=u2) # Name: GT empty stack (14)
c45 = mcdc.cell(+s46 & -s47, fill=u4) # Name: GT empty stack (15)
c46 = mcdc.cell(+s47 & -s49, fill=u2) # Name: GT empty stack (16)
c47 = mcdc.cell(+s49 & -s50, fill=u2) # Name: GT empty stack (17)
c48 = mcdc.cell(+s50 & -s51, fill=u2) # Name: GT empty stack (18)
c49 = mcdc.cell(+s51 & -s52, fill=u1) # Name: GT empty stack (19)
c50 = mcdc.cell(+s52, fill=u1) # Name: GT empty stack (20)
c51 = mcdc.cell(-s32, fill=u1) # Name: GT empty instr (0)
c52 = mcdc.cell(+s32 & -s33, fill=u1) # Name: GT empty instr (1)
c53 = mcdc.cell(+s33 & -s34, fill=u1) # Name: GT empty instr (2)
c54 = mcdc.cell(+s34 & -s35, fill=u2) # Name: GT empty instr (3)
c55 = mcdc.cell(+s35 & -s38, fill=u2) # Name: GT empty instr (4)
c56 = mcdc.cell(+s38 & -s39, fill=u3) # Name: GT empty instr (5)
c57 = mcdc.cell(+s39 & -s48, fill=u2) # Name: GT empty instr (6)
c58 = mcdc.cell(+s48 & -s40, fill=u2) # Name: GT empty instr (7)
c59 = mcdc.cell(+s40 & -s41, fill=u4) # Name: GT empty instr (8)
c60 = mcdc.cell(+s41 & -s42, fill=u2) # Name: GT empty instr (9)
c61 = mcdc.cell(+s42 & -s43, fill=u4) # Name: GT empty instr (10)
c62 = mcdc.cell(+s43 & -s44, fill=u2) # Name: GT empty instr (11)
c63 = mcdc.cell(+s44 & -s45, fill=u4) # Name: GT empty instr (12)
c64 = mcdc.cell(+s45 & -s36, fill=u2) # Name: GT empty instr (13)
c65 = mcdc.cell(+s36 & -s46, fill=u2) # Name: GT empty instr (14)
c66 = mcdc.cell(+s46 & -s47, fill=u4) # Name: GT empty instr (15)
c67 = mcdc.cell(+s47 & -s49, fill=u2) # Name: GT empty instr (16)
c68 = mcdc.cell(+s49 & -s50, fill=u2) # Name: GT empty instr (17)
c69 = mcdc.cell(+s50 & -s51, fill=u2) # Name: GT empty instr (18)
c70 = mcdc.cell(+s51 & -s52, fill=u1) # Name: GT empty instr (19)
c71 = mcdc.cell(+s52, fill=u1) # Name: GT empty instr (20)
c613 = mcdc.cell(-s38 & +s1, fill=u86) # Name: Fuel pin (1.6%) stack (o0)
c614 = mcdc.cell(+s38 & -s39 & +s1, fill=u87) # Name: Fuel pin (1.6%) stack (o1)
c615 = mcdc.cell(+s39 & -s48 & +s1, fill=u86) # Name: Fuel pin (1.6%) stack (o2)
c616 = mcdc.cell(+s48 & -s40 & +s1, fill=u86) # Name: Fuel pin (1.6%) stack (o3)
c617 = mcdc.cell(+s40 & -s41 & +s1, fill=u88) # Name: Fuel pin (1.6%) stack (o4)
c618 = mcdc.cell(+s41 & -s42 & +s1, fill=u86) # Name: Fuel pin (1.6%) stack (o5)
c619 = mcdc.cell(+s42 & -s43 & +s1, fill=u88) # Name: Fuel pin (1.6%) stack (o6)
c620 = mcdc.cell(+s43 & -s44 & +s1, fill=u86) # Name: Fuel pin (1.6%) stack (o7)
c621 = mcdc.cell(+s44 & -s45 & +s1, fill=u88) # Name: Fuel pin (1.6%) stack (o8)
c622 = mcdc.cell(+s45 & +s1, fill=u86) # Name: Fuel pin (1.6%) stack (o9)
c624 = mcdc.cell(-s32, fill=u1) # Name: Fuel (1.6%) stack (0)
c625 = mcdc.cell(+s32 & -s33, fill=u82) # Name: Fuel (1.6%) stack (1)
c626 = mcdc.cell(+s33 & -s34, fill=u82) # Name: Fuel (1.6%) stack (2)
c627 = mcdc.cell(+s34 & -s35, fill=u83) # Name: Fuel (1.6%) stack (3)
c629 = mcdc.cell(+s36 & -s46, fill=u84) # Name: Fuel (1.6%) stack (5)
c630 = mcdc.cell(+s46 & -s47, fill=u85) # Name: Fuel (1.6%) stack (6)
c631 = mcdc.cell(+s47 & -s49, fill=u84) # Name: Fuel (1.6%) stack (7)
c632 = mcdc.cell(+s49 & -s50, fill=u83) # Name: Fuel (1.6%) stack (8)
c633 = mcdc.cell(+s50 & -s51, fill=u1) # Name: Fuel (1.6%) stack (9)
c634 = mcdc.cell(+s51 & -s52, fill=u82) # Name: Fuel (1.6%) stack (10)
c635 = mcdc.cell(+s52, fill=u1) # Name: Fuel (1.6%) stack (11)
c640 = mcdc.cell(-s38 & +s1, fill=u86) # Name: Fuel pin (2.4%) stack (o0)
c641 = mcdc.cell(+s38 & -s39 & +s1, fill=u87) # Name: Fuel pin (2.4%) stack (o1)
c642 = mcdc.cell(+s39 & -s48 & +s1, fill=u86) # Name: Fuel pin (2.4%) stack (o2)
c643 = mcdc.cell(+s48 & -s40 & +s1, fill=u86) # Name: Fuel pin (2.4%) stack (o3)
c644 = mcdc.cell(+s40 & -s41 & +s1, fill=u88) # Name: Fuel pin (2.4%) stack (o4)
c645 = mcdc.cell(+s41 & -s42 & +s1, fill=u86) # Name: Fuel pin (2.4%) stack (o5)
c646 = mcdc.cell(+s42 & -s43 & +s1, fill=u88) # Name: Fuel pin (2.4%) stack (o6)
c647 = mcdc.cell(+s43 & -s44 & +s1, fill=u86) # Name: Fuel pin (2.4%) stack (o7)
c648 = mcdc.cell(+s44 & -s45 & +s1, fill=u88) # Name: Fuel pin (2.4%) stack (o8)
c649 = mcdc.cell(+s45 & +s1, fill=u86) # Name: Fuel pin (2.4%) stack (o9)
c651 = mcdc.cell(-s32, fill=u1) # Name: Fuel (2.4%) stack (0)
c652 = mcdc.cell(+s32 & -s33, fill=u82) # Name: Fuel (2.4%) stack (1)
c653 = mcdc.cell(+s33 & -s34, fill=u82) # Name: Fuel (2.4%) stack (2)
c654 = mcdc.cell(+s34 & -s35, fill=u83) # Name: Fuel (2.4%) stack (3)
c656 = mcdc.cell(+s36 & -s46, fill=u84) # Name: Fuel (2.4%) stack (5)
c657 = mcdc.cell(+s46 & -s47, fill=u85) # Name: Fuel (2.4%) stack (6)
c658 = mcdc.cell(+s47 & -s49, fill=u84) # Name: Fuel (2.4%) stack (7)
c659 = mcdc.cell(+s49 & -s50, fill=u83) # Name: Fuel (2.4%) stack (8)
c660 = mcdc.cell(+s50 & -s51, fill=u1) # Name: Fuel (2.4%) stack (9)
c661 = mcdc.cell(+s51 & -s52, fill=u82) # Name: Fuel (2.4%) stack (10)
c662 = mcdc.cell(+s52, fill=u1) # Name: Fuel (2.4%) stack (11)
c667 = mcdc.cell(-s38 & +s1, fill=u86) # Name: Fuel pin (3.1%) stack (o0)
c668 = mcdc.cell(+s38 & -s39 & +s1, fill=u87) # Name: Fuel pin (3.1%) stack (o1)
c669 = mcdc.cell(+s39 & -s48 & +s1, fill=u86) # Name: Fuel pin (3.1%) stack (o2)
c670 = mcdc.cell(+s48 & -s40 & +s1, fill=u86) # Name: Fuel pin (3.1%) stack (o3)
c671 = mcdc.cell(+s40 & -s41 & +s1, fill=u88) # Name: Fuel pin (3.1%) stack (o4)
c672 = mcdc.cell(+s41 & -s42 & +s1, fill=u86) # Name: Fuel pin (3.1%) stack (o5)
c673 = mcdc.cell(+s42 & -s43 & +s1, fill=u88) # Name: Fuel pin (3.1%) stack (o6)
c674 = mcdc.cell(+s43 & -s44 & +s1, fill=u86) # Name: Fuel pin (3.1%) stack (o7)
c675 = mcdc.cell(+s44 & -s45 & +s1, fill=u88) # Name: Fuel pin (3.1%) stack (o8)
c676 = mcdc.cell(+s45 & +s1, fill=u86) # Name: Fuel pin (3.1%) stack (o9)
c678 = mcdc.cell(-s32, fill=u1) # Name: Fuel (3.1%) stack (0)
c679 = mcdc.cell(+s32 & -s33, fill=u82) # Name: Fuel (3.1%) stack (1)
c680 = mcdc.cell(+s33 & -s34, fill=u82) # Name: Fuel (3.1%) stack (2)
c681 = mcdc.cell(+s34 & -s35, fill=u83) # Name: Fuel (3.1%) stack (3)
c683 = mcdc.cell(+s36 & -s46, fill=u84) # Name: Fuel (3.1%) stack (5)
c684 = mcdc.cell(+s46 & -s47, fill=u85) # Name: Fuel (3.1%) stack (6)
c685 = mcdc.cell(+s47 & -s49, fill=u84) # Name: Fuel (3.1%) stack (7)
c686 = mcdc.cell(+s49 & -s50, fill=u83) # Name: Fuel (3.1%) stack (8)
c687 = mcdc.cell(+s50 & -s51, fill=u1) # Name: Fuel (3.1%) stack (9)
c688 = mcdc.cell(+s51 & -s52, fill=u82) # Name: Fuel (3.1%) stack (10)
c689 = mcdc.cell(+s52, fill=u1) # Name: Fuel (3.1%) stack (11)
c1082 = mcdc.cell(fill=u150, rotation=[-0.0, -0.0, 90.0]) # Name: reflector NE
c1083 = mcdc.cell(fill=u150, rotation=[-0.0, -0.0, -90.0]) # Name: reflector SW
c1084 = mcdc.cell(fill=u150, rotation=[-0.0, -0.0, -180.0]) # Name: reflector SE
c1085 = mcdc.cell(fill=u155, rotation=[-0.0, -180.0, 90.0]) # Name: reflector 0,2
c1086 = mcdc.cell(fill=u154, rotation=[-0.0, -0.0, 90.0]) # Name: reflector 0,3
c1087 = mcdc.cell(fill=u152, rotation=[-0.0, -0.0, 90.0]) # Name: reflector 0,4
c1088 = mcdc.cell(fill=u153, rotation=[-0.0, -0.0, 90.0]) # Name: reflector 0,5
c1089 = mcdc.cell(fill=u155, rotation=[-0.0, -0.0, 90.0]) # Name: reflector 0,6
c1090 = mcdc.cell(fill=u151, rotation=[-0.0, -0.0, 90.0]) # Name: reflector 1,7
c1091 = mcdc.cell(fill=u155, rotation=[-0.0, -180.0, -0.0]) # Name: reflector 2,8
c1092 = mcdc.cell(fill=u153, rotation=[-0.0, -180.0, -0.0]) # Name: reflector 3,8
c1093 = mcdc.cell(fill=u152, rotation=[-0.0, -180.0, -0.0]) # Name: reflector 4,8
c1094 = mcdc.cell(fill=u153, rotation=[-0.0, -0.0, -180.0]) # Name: reflector 5,8
c1095 = mcdc.cell(fill=u155, rotation=[-180.0, -0.0, -0.0]) # Name: reflector 6,0
c1096 = mcdc.cell(fill=u155, rotation=[-0.0, -0.0, -180.0]) # Name: reflector 6,8
c1097 = mcdc.cell(fill=u151, rotation=[-180.0, -0.0, -0.0]) # Name: reflector 7,1
c1098 = mcdc.cell(fill=u151, rotation=[-0.0, -0.0, -180.0]) # Name: reflector 7,7
c1099 = mcdc.cell(fill=u155, rotation=[-0.0, -0.0, -90.0]) # Name: reflector 8,2
c1100 = mcdc.cell(fill=u153, rotation=[-0.0, -0.0, -90.0]) # Name: reflector 8,3
c1101 = mcdc.cell(fill=u152, rotation=[-0.0, -0.0, -90.0]) # Name: reflector 8,4
c1102 = mcdc.cell(fill=u154, rotation=[-0.0, -0.0, -90.0]) # Name: reflector 8,5
c1103 = mcdc.cell(fill=u155, rotation=[-0.0, -0.0, -180.0]) # Name: reflector 8,6

# --------------------------------------------------------------------------------------
# Moving control rods - Level 1
# --------------------------------------------------------------------------------------

for case in cases:
    cell_cr_water = config[f'cell_cr_water_{case}']
    cell_cr_water_tube = config[f'cell_cr_water_tube_{case}']
    cell_cr_water_dashpot = config[f'cell_cr_water_dashpot_{case}']

    # Universes - Level 1
    u1_ = mcdc.universe([cell_cr_water])
    u2_ = mcdc.universe([cell_cr_water_tube, c3, c4])
    u4_ = mcdc.universe([cell_cr_water_tube, c10, c11, c12])
    u6_ = mcdc.universe([cell_cr_water_dashpot, c17, c18])
    u7_ = mcdc.universe([cell_cr_water_dashpot, c20, c21, c22])

    # Cells - Level 1
    c30_ = mcdc.cell(-s32, fill=u1_)
    c31_ = mcdc.cell(+s32 & -s33, fill=u1_)
    c32_ = mcdc.cell(+s33 & -s34, fill=u1_)
    c33_ = mcdc.cell(+s34 & -s35, fill=u6_)
    c34_ = mcdc.cell(+s35 & -s38, fill=u6_)
    c35_ = mcdc.cell(+s38 & -s39, fill=u7_)
    c36_ = mcdc.cell(+s39 & -s48, fill=u6_)
    c37_ = mcdc.cell(+s48 & -s40, fill=u2_)
    c38_ = mcdc.cell(+s40 & -s41, fill=u4_)
    c39_ = mcdc.cell(+s41 & -s42, fill=u2_)
    c40_ = mcdc.cell(+s42 & -s43, fill=u4_)
    c41_ = mcdc.cell(+s43 & -s44, fill=u2_)
    c42_ = mcdc.cell(+s44 & -s45, fill=u4_)
    c43_ = mcdc.cell(+s45 & -s36, fill=u2_)
    c44_ = mcdc.cell(+s36 & -s46, fill=u2_)
    c45_ = mcdc.cell(+s46 & -s47, fill=u4_)
    c46_ = mcdc.cell(+s47 & -s49, fill=u2_)
    c47_ = mcdc.cell(+s49 & -s50, fill=u2_)
    c48_ = mcdc.cell(+s50 & -s51, fill=u2_)
    c49_ = mcdc.cell(+s51 & -s52, fill=u1_)
    c50_ = mcdc.cell(+s52, fill=u1_)

    # Universes - Level 2
    config[f'u10_{case}'] = mcdc.universe([c30_, c31_, c32_, c33_, c34_, c35_, c36_, c37_, c38_, c39_, c40_, c41_, c42_, c43_, c44_, c45_, c46_, c47_, c48_, c49_, c50_])

    # Continue to Lattices - Level 3

# --------------------------------------------------------------------------------------
# Universes - Level 2
# --------------------------------------------------------------------------------------

u10 = mcdc.universe([c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49, c50])
u11 = mcdc.universe([c51, c52, c53, c54, c55, c56, c57, c58, c59, c60, c61, c62, c63, c64, c65, c66, c67, c68, c69, c70, c71])
u156 = mcdc.universe([c1082])
u157 = mcdc.universe([c1083])
u158 = mcdc.universe([c1084])
u159 = mcdc.universe([c1085])
u160 = mcdc.universe([c1086])
u161 = mcdc.universe([c1087])
u162 = mcdc.universe([c1088])
u163 = mcdc.universe([c1089])
u164 = mcdc.universe([c1090])
u165 = mcdc.universe([c1091])
u166 = mcdc.universe([c1092])
u167 = mcdc.universe([c1093])
u168 = mcdc.universe([c1094])
u169 = mcdc.universe([c1095])
u170 = mcdc.universe([c1096])
u171 = mcdc.universe([c1097])
u172 = mcdc.universe([c1098])
u173 = mcdc.universe([c1099])
u174 = mcdc.universe([c1100])
u175 = mcdc.universe([c1101])
u176 = mcdc.universe([c1102])
u177 = mcdc.universe([c1103])
u90 = mcdc.universe([c613, c614, c615, c616, c617, c618, c619, c620, c621, c622, c623])
u93 = mcdc.universe([c640, c641, c642, c643, c644, c645, c646, c647, c648, c649, c650])
u96 = mcdc.universe([c667, c668, c669, c670, c671, c672, c673, c674, c675, c676, c677])

# --------------------------------------------------------------------------------------
# Cells - Level 2
# --------------------------------------------------------------------------------------

c628 = mcdc.cell(+s35 & -s36, fill=u90) # Name: Fuel (1.6%) stack (4)
c655 = mcdc.cell(+s35 & -s36, fill=u93) # Name: Fuel (2.4%) stack (4)
c682 = mcdc.cell(+s35 & -s36, fill=u96) # Name: Fuel (3.1%) stack (4)

# --------------------------------------------------------------------------------------
# Universes - Level 3
# --------------------------------------------------------------------------------------

u91 = mcdc.universe([c624, c625, c626, c627, c628, c629, c630, c631, c632, c633, c634, c635])
u94 = mcdc.universe([c651, c652, c653, c654, c655, c656, c657, c658, c659, c660, c661, c662])
u97 = mcdc.universe([c678, c679, c680, c681, c682, c683, c684, c685, c686, c687, c688, c689])

# --------------------------------------------------------------------------------------
# Lattices - Level 3
# --------------------------------------------------------------------------------------

u10r = config['u10_r']
u10rx = config['u10_rx']
u10s = config['u10_s']
u10sx2 = config['u10_sx2']
u10sx3 = config['u10_sx3']

# Lattice name: Assembly (1.6%) no BAs
l98 = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91, u91, u91, u91],
        [u91, u91, u91, u10, u91, u91, u91, u91, u91, u91, u91, u91, u91, u10, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10, u91, u91, u10, u91, u91, u11, u91, u91, u10, u91, u91, u10, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u10, u91, u91, u91, u91, u91, u91, u91, u91, u91, u10, u91, u91, u91],
        [u91, u91, u91, u91, u91, u10, u91, u91, u10, u91, u91, u10, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
    ],
)

# Lattice name: Assembly (1.6%) no BAs, with regulating rods
l98r = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91, u91, u91, u91],
        [u91, u91, u91, u10r, u91, u91, u91, u91, u91, u91, u91, u91, u91, u10r, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10r, u91, u91, u10r, u91, u91, u11, u91, u91, u10r, u91, u91, u10r, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u10r, u91, u91, u91, u91, u91, u91, u91, u91, u91, u10r, u91, u91, u91],
        [u91, u91, u91, u91, u91, u10r, u91, u91, u10r, u91, u91, u10r, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
    ],
)

# Lattice name: Assembly (1.6%) no BAs, with stuck regulating rods
l98rx = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u91, u91, u91],
        [u91, u91, u91, u10rx, u91, u91, u91, u91, u91, u91, u91, u91, u91, u10rx, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10rx, u91, u91, u10rx, u91, u91, u11, u91, u91, u10rx, u91, u91, u10rx, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u10rx, u91, u91, u91, u91, u91, u91, u91, u91, u91, u10rx, u91, u91, u91],
        [u91, u91, u91, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u10rx, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
        [u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91, u91],
    ],
)

# Lattice name: Assembly (2.4%) no BAs
l134 = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94, u94, u94, u94],
        [u94, u94, u94, u10, u94, u94, u94, u94, u94, u94, u94, u94, u94, u10, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10, u94, u94, u10, u94, u94, u11, u94, u94, u10, u94, u94, u10, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u10, u94, u94, u94, u94, u94, u94, u94, u94, u94, u10, u94, u94, u94],
        [u94, u94, u94, u94, u94, u10, u94, u94, u10, u94, u94, u10, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
    ],
)

# Lattice name: Assembly (2.4%) no BAs, with safety rods
l134s = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94, u94, u94, u94],
        [u94, u94, u94, u10s, u94, u94, u94, u94, u94, u94, u94, u94, u94, u10s, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10s, u94, u94, u10s, u94, u94, u11, u94, u94, u10s, u94, u94, u10s, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u10s, u94, u94, u94, u94, u94, u94, u94, u94, u94, u10s, u94, u94, u94],
        [u94, u94, u94, u94, u94, u10s, u94, u94, u10s, u94, u94, u10s, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
    ],
)

# Lattice name: Assembly (2.4%) no BAs, with stuck safety rods
l134sx = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u94, u94, u94],
        [u94, u94, u94, u10sx2, u94, u94, u94, u94, u94, u94, u94, u94, u94, u10sx2, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u11, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u10sx2, u94, u94, u94, u94, u94, u94, u94, u94, u94, u10sx2, u94, u94, u94],
        [u94, u94, u94, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u10sx2, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
        [u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94, u94],
    ],
)

# Lattice name: Assembly (3.1%) no BAs
l142 = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97, u97, u97, u97],
        [u97, u97, u97, u10, u97, u97, u97, u97, u97, u97, u97, u97, u97, u10, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10, u97, u97, u10, u97, u97, u11, u97, u97, u10, u97, u97, u10, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u10, u97, u97, u97, u97, u97, u97, u97, u97, u97, u10, u97, u97, u97],
        [u97, u97, u97, u97, u97, u10, u97, u97, u10, u97, u97, u10, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
    ],
)

# Lattice name: Assembly (3.1%) no BAs, with safety rods
l142s = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97, u97, u97, u97],
        [u97, u97, u97, u10s, u97, u97, u97, u97, u97, u97, u97, u97, u97, u10s, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10s, u97, u97, u10s, u97, u97, u11, u97, u97, u10s, u97, u97, u10s, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u10s, u97, u97, u97, u97, u97, u97, u97, u97, u97, u10s, u97, u97, u97],
        [u97, u97, u97, u97, u97, u10s, u97, u97, u10s, u97, u97, u10s, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
    ],
)

# Lattice name: Assembly (3.1%) no BAs, with stuck safety rods
l142sx = mcdc.lattice(
    x = [-10.70864, 1.25984, 17],
    y = [-10.70864, 1.25984, 17],
    universes = [
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u97, u97, u97],
        [u97, u97, u97, u10sx3, u97, u97, u97, u97, u97, u97, u97, u97, u97, u10sx3, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u11, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u10sx3, u97, u97, u97, u97, u97, u97, u97, u97, u97, u10sx3, u97, u97, u97],
        [u97, u97, u97, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u10sx3, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
        [u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97, u97],
    ],
)

# --------------------------------------------------------------------------------------
# Cells - Level 3
# --------------------------------------------------------------------------------------

c690 = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l98) # Name: Assembly (1.6%) no BAs lattice
c690r = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l98r) # Name: Assembly (1.6%) no BAs lattice, with regulating rods
c690rx = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l98rx) # Name: Assembly (1.6%) no BAs lattice, with stuck regulating rods
c924 = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l134) # Name: Assembly (2.4%) no BAs lattice
c924s = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l134s) # Name: Assembly (2.4%) no BAs lattice, with safety rods
c924sx = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l134sx) # Name: Assembly (2.4%) no BAs lattice, with stuck safety rods
c976 = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l142) # Name: Assembly (3.1%) no BAs lattice
c976s = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l142s) # Name: Assembly (3.1%) no BAs lattice, with safety rods
c976sx = mcdc.cell(+s24 & -s25 & +s26 & -s27, fill=l142sx) # Name: Assembly (3.1%) no BAs lattice, with stuck safety rods

# --------------------------------------------------------------------------------------
# Universes - Level 4
# --------------------------------------------------------------------------------------

u135 = mcdc.universe([c924, c925, c926, c927, c928, c929, c930, c931, c932, c933, c934, c935, c936])
u135s = mcdc.universe([c924s, c925, c926, c927, c928, c929, c930, c931, c932, c933, c934, c935, c936])
u135sx = mcdc.universe([c924sx, c925, c926, c927, c928, c929, c930, c931, c932, c933, c934, c935, c936])
u143 = mcdc.universe([c976, c977, c978, c979, c980, c981, c982, c983, c984, c985, c986, c987, c988])
u143s = mcdc.universe([c976s, c977, c978, c979, c980, c981, c982, c983, c984, c985, c986, c987, c988])
u143sx = mcdc.universe([c976sx, c977, c978, c979, c980, c981, c982, c983, c984, c985, c986, c987, c988])
u99 = mcdc.universe([c690, c691, c692, c693, c694, c695, c696, c697, c698, c699, c700, c701, c702])
u99r = mcdc.universe([c690r, c691, c692, c693, c694, c695, c696, c697, c698, c699, c700, c701, c702])
u99rx = mcdc.universe([c690rx, c691, c692, c693, c694, c695, c696, c697, c698, c699, c700, c701, c702])

# --------------------------------------------------------------------------------------
# Lattices - Level 4
# --------------------------------------------------------------------------------------

# Lattice name: Main core
l179 = mcdc.lattice(
    x = [-96.76637999999998, 21.503639999999997, 9],
    y = [-96.76637999999998, 21.503639999999997, 9],
    universes = [
        [u178, u178,  u159,   u160,  u161,   u162,  u163,  u178,  u178],
        [u178, u151,  u150,   u143,  u143sx, u143,  u156,  u164,  u178],
        [u155, u150,  u143,   u135s, u99,    u135s, u143,  u156,  u165],
        [u153, u143,  u135s,  u99,   u99r,   u99,   u135s, u143,  u166],
        [u152, u143s, u99,    u99r,  u135,   u99rx, u99,   u143s, u167],
        [u154, u143,  u135sx, u99,   u99r,   u99,   u135s, u143,  u168],
        [u169, u157,  u143,   u135s, u99,    u135s, u143,  u158,  u170],
        [u178, u171,  u157,   u143,  u143s,  u143,  u158,  u172,  u178],
        [u178, u178,  u173,   u174,  u175,   u176,  u177,  u178,  u178],
    ],
)

# --------------------------------------------------------------------------------------
# Cells - Level 4
# --------------------------------------------------------------------------------------

c1105 = mcdc.cell(-s71 & +s81 & -s80, fill=l179) # Name: Main core

# --------------------------------------------------------------------------------------
# Universes - Level 5
# --------------------------------------------------------------------------------------

u0 = mcdc.universe([c1105, c1106, c1107, c1108], root=True)

# =============================================================================
# Set source
# =============================================================================
# In the center, highest energy

energy = np.zeros(7)
energy[0] = 1.0

source = mcdc.source(
    point=[0.0, 0.0, 100.0], energy=energy
)

# =============================================================================
# Set tally, setting, and run mcdc
# =============================================================================

# Tally
xmin = -133.35
xmax = 133.35
xmin_core = -96.76637999999998
xmax_core = 96.76637999999998
Nx = 9 * 17
#
x_grid = np.linspace(xmin_core, xmax_core, Nx + 1)
pitch = x_grid[1] - x_grid[0]
x_grid_right = np.append(np.arange(xmax_core, xmax, pitch), xmax)[1:]
x_grid_left = np.flip(np.append(np.arange(xmin_core, xmin, -pitch), xmin))[:-1]
x_grid = np.concatenate((x_grid_left, x_grid, x_grid_right))
#
xf_grid = np.linspace(xmin_core, xmax_core, Nx + 1)
#
zmin = -36.6205
zmax = 246.61149999999998
zmin_core = config['bottom']
zmax_core = config['top']
Nz = math.ceil((zmax - zmin)/pitch)
Nz_core = math.ceil((zmax_core - zmin_core)/pitch)
#
z_grid = np.linspace(zmin, zmax, Nz + 1)
zf_grid = np.linspace(zmin_core, zmax_core, Nz_core + 1)

mcdc.tally.mesh_tally(
    scores=["fission"],
    x=xf_grid,
    y=xf_grid,
    z=zf_grid,
)
mcdc.tally.mesh_tally(
    scores=["flux"],
    x=x_grid,
    y=x_grid,
    z=z_grid,
    g=np.array([-0.5, 4.5, 6.5])
)

# Setting
mcdc.setting(N_particle=1e3)
mcdc.eigenmode(N_inactive=50, N_active=150, gyration_radius="all")
mcdc.population_control()

# Run
mcdc.run()

'''
colors = {
    m_helium: "azure",
    m_inconel: "gray",
    m_ss302: "sienna",
    m_ss304: "tan",
    m_csteel: "olive",
    m_zr4: "slategray",
    m_m5: "black",
    m_fuel31: "red",
    m_fuel24: "orange",
    m_fuel16: "gold",
    m_water: 'blue',
    m_cr: 'green',
}
mcdc.visualize('xy', x=[-150, 150], y=[-150, 150], z=100.0, pixels=(1000, 1000), colors=colors)
mcdc.visualize('xz', x=[-150, 150], z=[-37, 247], y=0.0, pixels=(1000, 1000), colors=colors)
'''
