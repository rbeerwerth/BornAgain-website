import numpy as np
import bornagain as ba
from bornagain import deg, nm
import matplotlib
import matplotlib.pyplot as plt

# parameters of 3D particle arrangement
particle_radius = 2.5*nm
lattice_length = 10.0*nm

# mesocrystal size
meso_height = 50.0*nm
meso_width = 100.0*nm
meso_length = meso_width

datafile = "fake_data.npy"


def get_sample():
    # Defining Materials
    m_air = ba.HomogeneousMaterial("Air", 0.0, 0.0)
    m_particle = ba.HomogeneousMaterial("Particle", 0.0006, 2e-08)
    m_substrate = ba.HomogeneousMaterial("Substrate", 6e-06, 2e-08)

    # Defining Layers
    l_air = ba.Layer(m_air)
    l_substrate = ba.Layer(m_substrate)

    # Spherical particles, form the base of the mesocrystal
    ff_sphere = ba.FormFactorFullSphere(particle_radius)
    sphere = ba.Particle(m_particle, ff_sphere)

    # mesocrystal lattice (cubic lattice for this example)
    lattice_a = ba.kvector_t(lattice_length, 0.0, 0.0)
    lattice_b = ba.kvector_t(0.0, lattice_length, 0.0)
    lattice_c = ba.kvector_t(0.0, 0.0, lattice_length)
    lattice = ba.Lattice(lattice_a, lattice_b, lattice_c)

    # crystal structure
    crystal = ba.Crystal(sphere, lattice)
    # uncomment to add variance of displacement in each dimension (sigma^2)
    # crystal.setDWFactor(2)    #  for BornAgain 1.16 and below
    # crystal.setPositionVariance(2)    # for BornAgain 1.17+

    # mesocrystal
    meso_ff = ba.FormFactorLorentz(meso_width, meso_height)                 # Lorentz
    meso = ba.MesoCrystal(crystal, meso_ff)

    layout = ba.ParticleLayout()
    layout.addParticle(meso)

    # Adding layouts to layers
    l_air.addLayout(layout)

    # Defining Multilayers
    multilayer = ba.MultiLayer()
    multilayer.addLayer(l_air)
    multilayer.addLayer(l_substrate)
    # print(multilayer.parametersToString())
    return multilayer


def get_simulation():
    simulation = ba.GISASSimulation()
    simulation.setDetectorParameters(400, -2.0*deg, 2.0*deg, 400, 0.0*deg, 3.0*deg)
    
    simulation.setBeamParameters(0.1*nm, 0.2*deg, 0.0*deg)
    simulation.setBeamIntensity(1.0e+06)
    # simulation.getOptions().setMonteCarloIntegration(True, 20)  # uncomment for large mesocrystals
    simulation.setTerminalProgressMonitor()
    return simulation


def run_simulation():
    sample = get_sample()
    simulation = get_simulation()
    simulation.setSample(sample)
    simulation.runSimulation()
    return simulation.result()


def load_data(filename=datafile):
    """
    Loads experimental data and returns numpy array.
    """
    simulation = get_simulation()
    data = np.load(filename)       # this loads numpy binary format
    # data = np.loadtxt(filename)  # to  load ascii data

    # for any other format you can use fabio library as follows
    # import fabio
    # img = fabio.open(filename)
    # data = np.array(img.data, dtype='float')

    return ba.ConvertData(simulation, data, True)


def plot(fontsize=16):
    """
    Creates 4 plots: 2D experiment, 2D simulation, slice along Qz and slice along Qy
    """
    plt.style.use('seaborn-talk')
    matplotlib. rcParams['xtick.labelsize'] = fontsize
    matplotlib. rcParams['ytick.labelsize'] = fontsize
    data = load_data()
    plt.figure(figsize=(22, 17))
    zmin = 0.1
    zmax = 2.0e+06
    qz_slice = 0.4
    qy_slice = 0.64
    # ====================
    # Experiment 2D
    # ====================
    plt.subplot(2, 2, 1)
    ba.plot_colormap(data, units=ba.AxesUnits.QSPACE, zmin=zmin, zmax=zmax)
    plt.axhline(y=qz_slice, color='0.5', linestyle='--', linewidth=1)
    plt.axvline(x=qy_slice, color='0.5', linestyle='--', linewidth=1)
    plt.title("Experiment", fontsize=fontsize)
    # ax.tick_params(axis='both', which='major', labelsize=fontsize)
    # ====================
    # Simulation 2D
    # ====================
    result = run_simulation()
    axes_labels = ba.get_axes_labels(result, ba.AxesUnits.QSPACE)
    plt.subplot(2, 2, 2)
    ba.plot_colormap(result, units=ba.AxesUnits.QSPACE, zmin=zmin, zmax=zmax)
    plt.axhline(y=qz_slice, color='0.5', linestyle='--', linewidth=1)
    plt.axvline(x=qy_slice, color='0.5', linestyle='--', linewidth=1)
    plt.title("BornAgain simulation", fontsize=fontsize)
    # ====================
    # projection along Qz
    # ====================
    plt.subplot(2, 2, 3)
    exp_qz = data.histogram2d(ba.AxesUnits.QSPACE).projectionY(qy_slice)
    sim_qz = result.histogram2d(ba.AxesUnits.QSPACE).projectionY(qy_slice)
    plt.semilogy(exp_qz.getBinCenters(), exp_qz.getBinValues(), color='k', marker='.',
                 markersize=5, linestyle='None', label="Experiment")
    plt.semilogy(sim_qz.getBinCenters(), sim_qz.getBinValues(), color='g', linewidth=2,
                 label="Simulation")
    # plt.xlim(0.1, 1.21)    # uncomment and edit to set x axis limits
    # plt.ylim(0.5, zmax)    # uncomment and edit to set y axis limits
    plt.xlabel(axes_labels[1], fontsize=fontsize)
    plt.ylabel(r'$\mathrm{I(Q_z)}$, a.u.', fontsize=fontsize)
    plt.legend(fontsize=fontsize)
    plt.title(r"Slice along $Q_z$", fontsize=fontsize)
    # =====================
    # projection along Qy
    # =====================
    plt.subplot(2, 2, 4)
    exp_qy = data.histogram2d(ba.AxesUnits.QSPACE).projectionX(qz_slice)
    sim_qy = result.histogram2d(ba.AxesUnits.QSPACE).projectionX(qz_slice)
    plt.semilogy(exp_qy.getBinCenters(), exp_qy.getBinValues(), color='k', marker='.',
                 markersize=5, linestyle='None', label="Experiment")
    plt.semilogy(sim_qy.getBinCenters(), sim_qy.getBinValues(), color='g',
                 linewidth=2, label="Simulation")
    # plt.xlim(-0.81, 0.71)        # uncomment and edit to set x axis limits
    # plt.ylim(0.5, zmax)          # uncomment and edit to set y axis limits
    plt.xlabel(axes_labels[0], fontsize=fontsize)
    plt.ylabel(r'$\mathrm{I(Q_y)}$, a.u.', fontsize=fontsize)
    plt.legend(fontsize=fontsize)
    plt.title(r"Slice along $Q_y$", fontsize=fontsize)

    # plt.savefig("{}.png".format("my_meso"))   # uncomment to save figure

    # uncomment to save slices to text files
    # np.savetxt("{}_slice_qz.txt".format("my_meso"), np.column_stack([sim_qz.getBinCenters(), sim_qz.getBinValues()]))
    # np.savetxt("{}_slice_qy.txt".format("my_meso"), np.column_stack([sim_qy.getBinCenters(), sim_qy.getBinValues()]))

    plt.show()


if __name__ == '__main__':
    plot()
