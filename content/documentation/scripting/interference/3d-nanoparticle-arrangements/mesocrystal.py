import numpy
import bornagain as ba
from bornagain import deg, nm

# parameters of 3D particle arrangement
particle_radius = 2.5*nm
lattice_length = 10.0*nm

# mesocrystal size
meso_height = 50.0*nm
meso_width = 100.0*nm
meso_length = meso_width


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
    # meso_ff = ba.FormFactorBox(meso_length, meso_width, meso_height)      # Box
    # meso_ff = ba.FormFactorCylinder(meso_width/2.0, meso_height)          # Cylinder
    # meso_ff = ba.FormFactorTruncatedSphere(meso_width/2.0, meso_height)   # Tr. Sphere
    # meso_ff = ba.FormFactorGauss(meso_width, meso_height)                 # Gauss
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


if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result, intensity_max=1e+06)
